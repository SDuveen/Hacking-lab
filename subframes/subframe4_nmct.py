from dataclasses import dataclass
from .utils import calculate_parity_bits, gps_time, int_to_bits, random_bits

def create_subframe4_nmct(date):
    week_number, time_of_week = gps_time(date)

    word1 = Subframe4_Word1()
    word2 = Subframe4_Word2(time_of_week, [ 0, 0 ], word1.parity[-2], word1.parity[-1])
    word3 = Subframe4_Word3(word2.parity[-2], word2.parity[-1])
    word4 = Subframe4_Word4(word3.parity[-2], word3.parity[-1])
    word5 = Subframe4_Word5(word4.parity[-2], word4.parity[-1])
    word6 = Subframe4_Word6(word5.parity[-2], word5.parity[-1])
    word7 = Subframe4_Word7(word6.parity[-2], word6.parity[-1])
    word8 = Subframe4_Word8(word7.parity[-2], word7.parity[-1])
    word9 = Subframe4_Word9(word8.parity[-2], word8.parity[-1])
    word10 = Subframe4_Word10(word9.parity[-2], word9.parity[-1])

    return Subframe4(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10)

@dataclass
class Subframe4_Word1:
    preamble          = [ 1, 0, 0, 0, 1, 0, 1, 1 ]
    reserved          = random_bits(16)
    parity: list[int] # 6 bits

    def __init__(self):
        self.parity = calculate_parity_bits(data_bits=self.preamble + self.reserved, previous_D29=0, previous_D30=0, first_word=True)

@dataclass
class Subframe4_Word2:
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
class Subframe4_Word3:
    unknown = random_bits(8)
    ai = random_bits(2)
    erd1 = random_bits(6)
    erd2 = random_bits(6)
    erd3_msb = random_bits(2)
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.unknown + self.ai + self.erd1 + self.erd2 + self.erd3_msb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word4:
    erd3_lsb = random_bits(4)
    erd4 = random_bits(6)
    erd5 = random_bits(6)
    erd6 = random_bits(6)
    erd7_msb = random_bits(2)
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.erd3_lsb + self.erd4 + self.erd5 + self.erd6 + self.erd7_msb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word5:
    erd7_lsb = random_bits(4)
    erd8 = random_bits(6)
    erd9 = random_bits(6)
    erd10 = random_bits(6)
    erd11_msb = random_bits(2)
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.erd7_lsb + self.erd8 + self.erd9 + self.erd10 + self.erd11_msb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word6:
    erd11_lsb = random_bits(4)
    erd12 = random_bits(6)
    erd13 = random_bits(6)
    erd14 = random_bits(6)
    erd15_msb = random_bits(2)
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.erd11_lsb + self.erd12 + self.erd13 + self.erd14 + self.erd15_msb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word7:
    erd15_lsb = random_bits(4)
    erd16 = random_bits(6)
    erd17 = random_bits(6)
    erd18 = random_bits(6)
    erd19_msb = random_bits(2)
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.erd15_lsb + self.erd16 + self.erd17 + self.erd18 + self.erd19_msb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word8:
    erd19_lsb = random_bits(4)
    erd20 = random_bits(6)
    erd21 = random_bits(6)
    erd22 = random_bits(6)
    erd23_msb = random_bits(2)
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.erd19_lsb + self.erd20 + self.erd21 + self.erd22 + self.erd23_msb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word9:
    erd23_lsb = random_bits(4)
    erd24 = random_bits(6)
    erd25 = random_bits(6)
    erd26 = random_bits(6)
    erd27_msb = random_bits(2)
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.erd23_lsb + self.erd24 + self.erd25 + self.erd26 + self.erd27_msb, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word10:
    erd27_lsb = random_bits(4)
    erd28 = random_bits(6)
    erd29 = random_bits(6)
    erd30 = random_bits(6)
    unknown = random_bits(2)
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.erd27_lsb + self.erd28 + self.erd29 + self.erd30 + self.unknown, previous_D29=D29, previous_D30=D30, first_word=False)


@dataclass
class Subframe4:
    word1: Subframe4_Word1
    word2: Subframe4_Word2
    word3: Subframe4_Word3
    word4: Subframe4_Word4
    word5: Subframe4_Word5
    word6: Subframe4_Word6
    word7: Subframe4_Word7
    word8: Subframe4_Word8
    word9: Subframe4_Word9
    word10: Subframe4_Word10

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
        self.data += word3.unknown + word3.ai + word3.erd1 + word3.erd2 + word3.erd3_msb + word3.parity
        self.data += word4.erd3_lsb + word4.erd4 + word4.erd5 + word4.erd6 + word4.erd7_msb + word4.parity
        self.data += word5.erd7_lsb + word5.erd8 + word5.erd9 + word5.erd10 + word5.erd11_msb + word5.parity
        self.data += word6.erd11_lsb + word6.erd12 + word6.erd13 + word6.erd14 + word6.erd15_msb + word6.parity
        self.data += word7.erd15_lsb + word7.erd16 + word7.erd17 + word7.erd18 + word7.erd19_msb + word7.parity
        self.data += word8.erd19_lsb + word8.erd20 + word8.erd21 + word8.erd22 + word8.erd23_msb + word8.parity
        self.data += word9.erd23_lsb + word9.erd24 + word9.erd25 + word9.erd26 + word9.erd27_msb + word9.parity
        self.data += word10.erd27_lsb + word10.erd28 + word10.erd29 + word10.erd30 + word10.unknown + word10.parity

    def __str__(self):
        return f"""{''.join(map(str, (self.word1.preamble + self.word1.reserved + self.word1.parity)))}
{''.join(map(str, (self.word2.time_of_week + self.word2.alert_flag + self.word2.anti_spoofing + self.word2.subframe_id + self.word2.parity_bits + self.word2.parity)))}
{''.join(map(str, (self.word3.unknown + self.word3.ai + self.word3.erd1 + self.word3.erd2 + self.word3.erd3_msb + self.word3.parity)))}
{''.join(map(str, (self.word4.erd3_lsb + self.word4.erd4 + self.word4.erd5 + self.word4.erd6 + self.word4.erd7_msb + self.word4.parity)))}
{''.join(map(str, (self.word5.erd7_lsb + self.word5.erd8 + self.word5.erd9 + self.word5.erd10 + self.word5.erd11_msb + self.word5.parity)))}
{''.join(map(str, (self.word6.erd11_lsb + self.word6.erd12 + self.word6.erd13 + self.word6.erd14 + self.word6.erd15_msb + self.word6.parity)))}
{''.join(map(str, (self.word7.erd15_lsb + self.word7.erd16 + self.word7.erd17 + self.word7.erd18 + self.word7.erd19_msb + self.word7.parity)))}
{''.join(map(str, (self.word8.erd19_lsb + self.word8.erd20 + self.word8.erd21 + self.word8.erd22 + self.word8.erd23_msb + self.word8.parity)))}
{''.join(map(str, (self.word9.erd23_lsb + self.word9.erd24 + self.word9.erd25 + self.word9.erd26 + self.word9.erd27_msb + self.word9.parity)))}
{''.join(map(str, (self.word10.erd27_lsb + self.word10.erd28 + self.word10.erd29 + self.word10.erd30 + self.word10.unknown + self.word10.parity)))}"""
