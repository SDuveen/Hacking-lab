from dataclasses import dataclass
from .utils import calculate_parity_bits, gps_time, int_to_bits, random_bits

def create_subframe3(date):
    week_number, time_of_week = gps_time(date)

    word1 = Subframe3_Word1()
    word2 = Subframe3_Word2(time_of_week, [0, 0], word1.parity[-2], word1.parity[-1])
    word3 = Subframe3_Word3(word2.parity[-2], word2.parity[-1])
    word4 = Subframe3_Word4(word3.parity[-2], word3.parity[-1])
    word5 = Subframe3_Word5(word4.parity[-2], word4.parity[-1])
    word6 = Subframe3_Word6(word5.parity[-2], word5.parity[-1])
    word7 = Subframe3_Word7(word6.parity[-2], word6.parity[-1])
    word8 = Subframe3_Word8(word7.parity[-2], word7.parity[-1])
    word9 = Subframe3_Word9(word8.parity[-2], word8.parity[-1])
    word10 = Subframe3_Word10([0, 0], word9.parity[-2], word9.parity[-1])

    return Subframe3(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10)

@dataclass
class Subframe3_Word1:
    preamble          = [ 1, 0, 0, 0, 1, 0, 1, 1 ]
    reserved          = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int] # 6 bits

    def __init__(self):
        self.parity = calculate_parity_bits(data_bits=self.preamble + self.reserved, previous_D29=0, previous_D30=0, first_word=True)

@dataclass
class Subframe3_Word2:
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
class Subframe3_Word3:
    c_ic        = random_bits(16)
    omega_0_msb = random_bits(8)
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.c_ic + self.omega_0_msb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe3_Word4:
    omega_0_lsb = random_bits(24)
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.omega_0_lsb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe3_Word5:
    c_is    = random_bits(16)
    i_0_msb = random_bits(8)
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.c_is + self.i_0_msb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe3_Word6:
    i_0_lsb = random_bits(24)
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.i_0_lsb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe3_Word7:
    c_rc = random_bits(16)
    omega_msb = random_bits(8)
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.c_rc + self.omega_msb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe3_Word8:
    omega_lsb = random_bits(24)
    parity: list[int]   # 6 bits

    def __init__(self, D29, D30):   
        self.parity = calculate_parity_bits(data_bits=self.omega_lsb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe3_Word9:
    ascension_rate = random_bits(24)
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.ascension_rate, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe3_Word10:
    issue_of_data_ephemeris = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    idot = random_bits(14)
    parity_bits: list[int] # 2 bits
    parity:      list[int] # 6 bits

    def __init__(self, parity_bits, D29, D30):
        self.parity_bits = parity_bits
        self.parity = calculate_parity_bits(data_bits=self.issue_of_data_ephemeris + self.idot + self.parity_bits, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe3:
    word1: Subframe3_Word1
    word2: Subframe3_Word2
    word3: Subframe3_Word3
    word4: Subframe3_Word4
    word5: Subframe3_Word5
    word6: Subframe3_Word6
    word7: Subframe3_Word7
    word8: Subframe3_Word8
    word9: Subframe3_Word9
    word10: Subframe3_Word10

    def __init__(self, word1, word2, word3, word4, word5, word6, word7, word8, word9, word10):
        self.word1 = word1
        self.word2 = word2
        self.word3 = word3
        self.word4 = word4
        self.word5 = word5
        self.word6 = word6
        self.word7 = word7
        self.word8 = word8
        self.word9 = word9
        self.word10 = word10

        self.data = []
        self.data += self.word1.preamble + self.word1.reserved + self.word1.parity
        self.data += self.word2.time_of_week + self.word2.alert_flag + self.word2.anti_spoofing + self.word2.subframe_id + self.word2.parity_bits + self.word2.parity
        self.data += self.word3.c_ic + self.word3.omega_0_msb + self.word3.parity
        self.data += self.word4.omega_0_lsb + self.word4.parity
        self.data += self.word5.c_is + self.word5.i_0_msb + self.word5.parity
        self.data += self.word6.i_0_lsb + self.word6.parity
        self.data += self.word7.c_rc + self.word7.omega_msb + self.word7.parity
        self.data += self.word8.omega_lsb + self.word8.parity
        self.data += self.word9.ascension_rate + self.word9.parity
        self.data += self.word10.issue_of_data_ephemeris + self.word10.idot + self.word10.parity_bits + self.word10.parity

    def __str__(self):
        return f"""{''.join(map(str, (self.word1.preamble + self.word1.reserved + self.word1.parity)))}
{''.join(map(str, (self.word2.time_of_week + self.word2.alert_flag + self.word2.anti_spoofing + self.word2.subframe_id + self.word2.parity_bits + self.word2.parity)))}
{''.join(map(str, (self.word3.c_ic + self.word3.omega_0_msb + self.word3.parity)))}
{''.join(map(str, (self.word4.omega_0_lsb + self.word4.parity)))}
{''.join(map(str, (self.word5.c_is + self.word5.i_0_msb + self.word5.parity)))}
{''.join(map(str, (self.word6.i_0_lsb + self.word6.parity)))}
{''.join(map(str, (self.word7.c_rc + self.word7.omega_msb + self.word7.parity)))}
{''.join(map(str, (self.word8.omega_lsb + self.word8.parity)))}
{''.join(map(str, (self.word9.ascension_rate + self.word9.parity)))}
{''.join(map(str, (self.word10.issue_of_data_ephemeris + self.word10.idot + self.word10.parity_bits + self.word10.parity)))}"""