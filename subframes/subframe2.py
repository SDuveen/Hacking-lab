from dataclasses import dataclass
from .utils import calculate_parity_bits, gps_time, int_to_bits

def create_subframe2(date):
    week_number, time_of_week = gps_time(date)

    word1 = Subframe2_Word1()
    word2 = Subframe2_Word2(time_of_week, [0, 0], word1.parity[-2], word1.parity[-1])
    word3 = Subframe2_Word3(word2.parity[-2], word2.parity[-1])
    word4 = Subframe2_Word4(word3.parity[-2], word3.parity[-1])
    word5 = Subframe2_Word5(word4.parity[-2], word4.parity[-1])
    word6 = Subframe2_Word6(word5.parity[-2], word5.parity[-1])
    word7 = Subframe2_Word7(word6.parity[-2], word6.parity[-1])
    word8 = Subframe2_Word8(word7.parity[-2], word7.parity[-1])
    word9 = Subframe2_Word9(word8.parity[-2], word8.parity[-1])
    word10 = Subframe2_Word10(word9.parity[-2], word9.parity[-1])

    return Subframe2(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10)

@dataclass
class Subframe2_Word1:
    preamble          = [ 1, 0, 0, 0, 1, 0, 1, 1 ]
    reserved          = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int] # 6 bits

    def __init__(self):
        self.parity = calculate_parity_bits(data_bits=self.preamble + self.reserved, previous_D29=0, previous_D30=0, first_word=True)

@dataclass
class Subframe2_Word2:
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
class Subframe2_Word3:
    issue_of_data_ephemeris = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    c_rs                    = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int]       # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.issue_of_data_ephemeris + self.c_rs, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe2_Word4:
    delta_n = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    m_0_msb = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.delta_n + self.m_0_msb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe2_Word5:
    m0_lsb = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.m0_lsb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe2_Word6:
    c_uc = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    e_msb = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.c_uc + self.e_msb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe2_Word7:
    e_lsb = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.e_lsb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe2_Word8:
    c_us = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    sqrt_a_msb = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int]   # 6 bits

    def __init__(self, D29, D30):   
        self.parity = calculate_parity_bits(data_bits=self.c_us + self.sqrt_a_msb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe2_Word9:
    sqrt_a_lsb = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.sqrt_a_lsb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe2_Word10:
    t_oe = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    fit_interval_flag = [ 0 ]
    age_of_data_offset = [ 0, 0, 0, 0, 0, 0, 0 ]
    parity:      list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.t_oe + self.fit_interval_flag + self.age_of_data_offset, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe2:
    word1: Subframe2_Word1
    word2: Subframe2_Word2
    word3: Subframe2_Word3
    word4: Subframe2_Word4
    word5: Subframe2_Word5
    word6: Subframe2_Word6
    word7: Subframe2_Word7
    word8: Subframe2_Word8
    word9: Subframe2_Word9
    word10: Subframe2_Word10

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
        self.data += word3.issue_of_data_ephemeris + word3.c_rs + word3.parity
        self.data += word4.delta_n + word4.m_0_msb + word4.parity
        self.data += word5.m0_lsb + word5.parity
        self.data += word6.c_uc + word6.e_msb + word6.parity
        self.data += word7.e_lsb + word7.parity
        self.data += word8.c_us + word8.sqrt_a_msb + word8.parity
        self.data += word9.sqrt_a_lsb + word9.parity
        self.data += word10.t_oe + word10.fit_interval_flag + word10.age_of_data_offset + word10.parity

    def __str__(self):
        return f"""{''.join(map(str, (self.word1.preamble + self.word1.reserved + self.word1.parity)))}
{''.join(map(str, (self.word2.time_of_week + self.word2.alert_flag + self.word2.anti_spoofing + self.word2.subframe_id + self.word2.parity_bits + self.word2.parity)))}
{''.join(map(str, (self.word3.issue_of_data_ephemeris + self.word3.c_rs + self.word3.parity)))}
{''.join(map(str, (self.word4.delta_n + self.word4.m_0_msb + self.word4.parity)))}
{''.join(map(str, (self.word5.m0_lsb + self.word5.parity)))}
{''.join(map(str, (self.word6.c_uc + self.word6.e_msb + self.word6.parity)))}
{''.join(map(str, (self.word7.e_lsb + self.word7.parity)))}
{''.join(map(str, (self.word8.c_us + self.word8.sqrt_a_msb + self.word8.parity)))}
{''.join(map(str, (self.word9.sqrt_a_lsb + self.word9.parity)))}
{''.join(map(str, (self.word10.t_oe + self.word10.fit_interval_flag + self.word10.age_of_data_offset + self.word10.parity)))}"""