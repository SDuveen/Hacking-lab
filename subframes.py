from dataclasses import dataclass
from datetime import datetime, timedelta

ZERO_POINT = datetime.strptime('1980-01-06T00:00Z', '%Y-%m-%dT%H:%MZ')
TOTAL_LEAP_SECONDS_UNTIL_NOW = 18
MAX_GPS_WEEK = 1024

def gps_time(date = datetime.now()):
    begin_of_week = (date - timedelta(days=date.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
    begin_of_gps_week = begin_of_week - timedelta(seconds=TOTAL_LEAP_SECONDS_UNTIL_NOW)

    week_number = int((begin_of_gps_week - ZERO_POINT).total_seconds() / (7 * 24 * 3600)) % MAX_GPS_WEEK
    time_of_week = int((date - begin_of_gps_week).total_seconds() // 1.5)

    return week_number, time_of_week

def calculate_parity_bits(data_bits, previous_D29, previous_D30, first_word=False):
    D25 = data_bits[0] ^ data_bits[1] ^ data_bits[2] ^ data_bits[4] ^ data_bits[5] ^ data_bits[9] ^ data_bits[10] ^ data_bits[11] ^ data_bits[12] ^ data_bits[13] ^ data_bits[16] ^ data_bits[17] ^ data_bits[19] ^ data_bits[22]
    D26 = data_bits[1] ^ data_bits[2] ^ data_bits[3] ^ data_bits[5] ^ data_bits[6] ^ data_bits[10] ^ data_bits[11] ^ data_bits[12] ^ data_bits[13] ^ data_bits[14] ^ data_bits[17] ^ data_bits[18] ^ data_bits[20] ^ data_bits[23]
    D27 = data_bits[0] ^ data_bits[2] ^ data_bits[3] ^ data_bits[4] ^ data_bits[6] ^ data_bits[7] ^ data_bits[11] ^ data_bits[12] ^ data_bits[13] ^ data_bits[14] ^ data_bits[15] ^ data_bits[18] ^ data_bits[19] ^ data_bits[21]
    D28 = data_bits[1] ^ data_bits[3] ^ data_bits[4] ^ data_bits[5] ^ data_bits[7] ^ data_bits[8] ^ data_bits[12] ^ data_bits[13] ^ data_bits[14] ^ data_bits[15] ^ data_bits[16] ^ data_bits[19] ^ data_bits[20] ^ data_bits[22]
    D29 = data_bits[0] ^ data_bits[2] ^ data_bits[4] ^ data_bits[5] ^ data_bits[6] ^ data_bits[8] ^ data_bits[9] ^ data_bits[13] ^ data_bits[14] ^ data_bits[15] ^ data_bits[16] ^ data_bits[17] ^ data_bits[20] ^ data_bits[21] ^ data_bits[23]
    D30 = data_bits[2] ^ data_bits[4] ^ data_bits[5] ^ data_bits[7] ^ data_bits[8] ^ data_bits[9] ^ data_bits[10] ^ data_bits[12] ^ data_bits[14] ^ data_bits[18] ^ data_bits[21] ^ data_bits[22] ^ data_bits[23]

    if not first_word:
        D25 ^= previous_D29
        D26 ^= previous_D30
        D27 ^= previous_D29
        D28 ^= previous_D30
        D29 ^= previous_D30
        D30 ^= previous_D29

    return [D25, D26, D27, D28, D29, D30]

def create_subframe1(t_gd, a_f2, a_f1, a_f0):
    week_number, time_of_week = gps_time()

    word1 = Subframe1_Word1()
    word2 = Subframe1_Word2(time_of_week, [ 0, 0 ], word1.parity[-2], word1.parity[-1])
    word3 = Subframe1_Word3(week_number, word2.parity[-2], word2.parity[-1])
    word4 = Subframe1_Word4(word3.parity[-2], word3.parity[-1])
    word5 = Subframe1_Word5(word4.parity[-2], word4.parity[-1])
    word6 = Subframe1_Word6(word5.parity[-2], word5.parity[-1])
    word7 = Subframe1_Word7(t_gd, word6.parity[-2], word6.parity[-1])
    word8 = Subframe1_Word8(word7.parity[-2], word7.parity[-1])
    word9 = Subframe1_Word9(a_f2, a_f1, word8.parity[-2], word8.parity[-1])
    word10 = Subframe1_Word10(a_f0, [ 0, 0 ], word9.parity[-2], word9.parity[-1])

    return Subframe1(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10)

def int_to_bits(n, bits):
    return [int(x) for x in list(f'{n:0{bits}b}')][:bits]

@dataclass
class Subframe1_Word1:
    preamble          = [ 1, 0, 0, 0, 1, 0, 1, 1 ]
    reserved          = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int] # 6 bits

    def __init__(self):
        self.parity = calculate_parity_bits(data_bits=self.preamble + self.reserved, previous_D29=0, previous_D30=0, first_word=True)

@dataclass
class Subframe1_Word2:
    time_of_week:  list[int] # 17 bits
    alert_flag               = [ 0 ]
    anti_spoofing            = [ 0 ]
    subframe_id              = [ 0, 0, 1 ]
    parity_bits:   list[int] # 2 bits
    parity:        list[int] # 6 bits

    def __init__(self, time_of_week, parity_bits, D29, D30):
        self.time_of_week = int_to_bits(time_of_week, 17)
        self.parity_bits = parity_bits
        self.parity = calculate_parity_bits(data_bits=self.time_of_week + self.alert_flag + self.anti_spoofing + self.subframe_id + self.parity_bits, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe1_Word3:
    week_number:   list[int] # 10 bits
    p_or_ca_code = [ 1, 0 ]
    ura_index = [ 0, 0, 0, 0 ]
    sv_health = [ 0, 0, 0, 0, 0, 0 ]
    issue_of_data_clock = [ 0, 0 ]
    parity:              list[int] # 6 bits

    def __init__(self, week_number, D29, D30):
        self.week_number = int_to_bits(week_number, 10)
        self.parity = calculate_parity_bits(data_bits=self.week_number + self.p_or_ca_code + self.ura_index + self.sv_health + self.issue_of_data_clock, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe1_Word4:
    use_p_code = [ 0 ]
    reserved = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.use_p_code + self.reserved, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe1_Word5:
    reserved = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.reserved, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe1_Word6:
    reserved = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.reserved, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe1_Word7:
    reserved = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    t_gd:       list[int] # 8 bits
    parity:     list[int] # 6 bits

    def __init__(self, t_gd, D29, D30):
        self.t_gd = int_to_bits(t_gd, 8)
        self.parity = calculate_parity_bits(data_bits=self.reserved + self.t_gd, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe1_Word8:
    issue_of_data_clock = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    time_of_clock       = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int]   # 6 bits

    def __init__(self, D29, D30):   
        self.parity = calculate_parity_bits(data_bits=self.issue_of_data_clock + self.time_of_clock, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe1_Word9:
    a_f2:   list[int] # 8 bits
    a_f1:   list[int] # 16 bits
    parity: list[int] # 6 bits

    def __init__(self, a_f2, a_f1, D29, D30):
        self.a_f2 = int_to_bits(a_f2, 8)
        self.a_f1 = int_to_bits(a_f1, 16)
        self.parity = calculate_parity_bits(data_bits=self.a_f2 + self.a_f1, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe1_Word10:
    a_f0:        list[int] # 22 bits
    parity_bits: list[int] # 2 bits
    parity:      list[int] # 6 bits

    def __init__(self, a_f0, parity_bits, D29, D30):
        self.a_f0 = int_to_bits(a_f0, 22)
        self.parity_bits = parity_bits
        self.parity = calculate_parity_bits(data_bits=self.a_f0 + self.parity_bits, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe1:
    word1: Subframe1_Word1
    word2: Subframe1_Word2
    word3: Subframe1_Word3
    word4: Subframe1_Word4
    word5: Subframe1_Word5
    word6: Subframe1_Word6
    word7: Subframe1_Word7
    word8: Subframe1_Word8
    word9: Subframe1_Word9
    word10: Subframe1_Word10

    def __init__(self, word1, word2, word3, word4, word5, word6, word7, word8, word9, word10):
        self.data = []
        self.data += word1.preamble + word1.reserved + word1.parity
        self.data += word2.time_of_week + word2.alert_flag + word2.anti_spoofing + word2.subframe_id + word2.parity_bits + word2.parity
        self.data += word3.week_number + word3.p_or_ca_code + word3.ura_index + word3.sv_health + word3.issue_of_data_clock + word3.parity
        self.data += word4.use_p_code + word4.reserved + word4.parity
        self.data += word5.reserved + word5.parity
        self.data += word6.reserved + word6.parity
        self.data += word7.reserved + word7.t_gd + word7.parity
        self.data += word8.issue_of_data_clock + word8.time_of_clock + word8.parity
        self.data += word9.a_f2 + word9.a_f1 + word9.parity
        self.data += word10.a_f0 + word10.parity_bits + word10.parity

if __name__ == '__main__':
    subframe = create_subframe1(0, 0, 0, 0)

    # print the subframe data each line with 30 bits
    print('Subframe 1 data:')
    for i in range(0, len(subframe.data), 30):
        print(subframe.data[i:i+30])