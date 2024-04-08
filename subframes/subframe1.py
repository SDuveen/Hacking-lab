from dataclasses import dataclass
from .utils import calculate_parity_bits, gps_time, int_to_bits

def create_subframe1(date):
    week_number, time_of_week = gps_time(date)

    word1 = Subframe1_Word1()
    word2 = Subframe1_Word2(time_of_week, [ 0, 0 ], word1.parity[-2], word1.parity[-1])
    word3 = Subframe1_Word3(week_number, word2.parity[-2], word2.parity[-1])
    word4 = Subframe1_Word4(word3.parity[-2], word3.parity[-1])
    word5 = Subframe1_Word5(word4.parity[-2], word4.parity[-1])
    word6 = Subframe1_Word6(word5.parity[-2], word5.parity[-1])
    word7 = Subframe1_Word7(word6.parity[-2], word6.parity[-1])
    word8 = Subframe1_Word8(word7.parity[-2], word7.parity[-1])
    word9 = Subframe1_Word9(word8.parity[-2], word8.parity[-1])
    word10 = Subframe1_Word10([ 0, 0 ], word9.parity[-2], word9.parity[-1])

    return Subframe1(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10)

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
    t_gd = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
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
    a_f2 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    a_f1 = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.a_f2 + self.a_f1, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe1_Word10:
    a_f0 = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity_bits: list[int] # 2 bits
    parity:      list[int] # 6 bits

    def __init__(self, parity_bits, D29, D30):
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

    def __str__(self):
        return f"""{''.join(map(str, (self.word1.preamble + self.word1.reserved + self.word1.parity)))}
{''.join(map(str, (self.word2.time_of_week + self.word2.alert_flag + self.word2.anti_spoofing + self.word2.subframe_id + self.word2.parity_bits + self.word2.parity)))}
{''.join(map(str, (self.word3.week_number + self.word3.p_or_ca_code + self.word3.ura_index + self.word3.sv_health + self.word3.issue_of_data_clock + self.word3.parity)))}
{''.join(map(str, (self.word4.use_p_code + self.word4.reserved + self.word4.parity)))}
{''.join(map(str, (self.word5.reserved + self.word5.parity)))}
{''.join(map(str, (self.word6.reserved + self.word6.parity)))}
{''.join(map(str, (self.word7.reserved + self.word7.t_gd + self.word7.parity)))}
{''.join(map(str, (self.word8.issue_of_data_clock + self.word8.time_of_clock + self.word8.parity)))}
{''.join(map(str, (self.word9.a_f2 + self.word9.a_f1 + self.word9.parity)))}
{''.join(map(str, (self.word10.a_f0 + self.word10.parity_bits + self.word10.parity)))}"""