from dataclasses import dataclass
from .utils import calculate_parity_bits, gps_time, int_to_bits, random_bits

def create_subframe4_sv_health(date):
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
    as_flag_sv_config1 = random_bits(4)
    as_flag_sv_config2 = random_bits(4)
    as_flag_sv_config3 = random_bits(4)
    as_flag_sv_config4 = random_bits(4)
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.unknown + self.as_flag_sv_config1 + self.as_flag_sv_config2 + self.as_flag_sv_config3 + self.as_flag_sv_config4, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word4:
    as_flag_sv_config5 = random_bits(4)
    as_flag_sv_config6 = random_bits(4)
    as_flag_sv_config7 = random_bits(4)
    as_flag_sv_config8 = random_bits(4)
    as_flag_sv_config9 = random_bits(4)
    as_flag_sv_config10 = random_bits(4)
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.as_flag_sv_config5 + self.as_flag_sv_config6 + self.as_flag_sv_config7 + self.as_flag_sv_config8 + self.as_flag_sv_config9 + self.as_flag_sv_config10, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word5:
    as_flag_sv_config11 = random_bits(4)
    as_flag_sv_config12 = random_bits(4)
    as_flag_sv_config13 = random_bits(4)
    as_flag_sv_config14 = random_bits(4)
    as_flag_sv_config15 = random_bits(4)
    as_flag_sv_config16 = random_bits(4)
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.as_flag_sv_config11 + self.as_flag_sv_config12 + self.as_flag_sv_config13 + self.as_flag_sv_config14 + self.as_flag_sv_config15 + self.as_flag_sv_config16, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word6:
    as_flag_sv_config17 = random_bits(4)
    as_flag_sv_config18 = random_bits(4)
    as_flag_sv_config19 = random_bits(4)
    as_flag_sv_config20 = random_bits(4)
    as_flag_sv_config21 = random_bits(4)
    as_flag_sv_config22 = random_bits(4)
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.as_flag_sv_config17 + self.as_flag_sv_config18 + self.as_flag_sv_config19 + self.as_flag_sv_config20 + self.as_flag_sv_config21 + self.as_flag_sv_config22, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word7:
    as_flag_sv_config23 = random_bits(4)
    as_flag_sv_config24 = random_bits(4)
    as_flag_sv_config25 = random_bits(4)
    as_flag_sv_config26 = random_bits(4)
    as_flag_sv_config27 = random_bits(4)
    as_flag_sv_config28 = random_bits(4)
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.as_flag_sv_config23 + self.as_flag_sv_config24 + self.as_flag_sv_config25 + self.as_flag_sv_config26 + self.as_flag_sv_config27 + self.as_flag_sv_config28, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word8:
    as_flag_sv_config29 = random_bits(4)
    as_flag_sv_config30 = random_bits(4)
    as_flag_sv_config31 = random_bits(4)
    as_flag_sv_config32 = random_bits(4)
    unknown = random_bits(8)
    parity: list[int]   # 6 bits

    def __init__(self, D29, D30):   
        self.parity = calculate_parity_bits(data_bits=self.as_flag_sv_config29 + self.as_flag_sv_config30 + self.as_flag_sv_config31 + self.as_flag_sv_config32 + self.unknown, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word9:
    sv_25 = random_bits(6)
    sv_26 = random_bits(6)
    sv_27 = random_bits(6)
    sv_28 = random_bits(6)
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.sv_25 + self.sv_26 + self.sv_27 + self.sv_28, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word10:
    sv_29 = random_bits(6)
    sv_30 = random_bits(6)
    sv_31 = random_bits(6)
    sv_32 = random_bits(6)
    parity:      list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.sv_29 + self.sv_30 + self.sv_31 + self.sv_32, previous_D29=D29, previous_D30=D30, first_word=False)

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
        self.data += word3.unknown + word3.as_flag_sv_config1 + word3.as_flag_sv_config2 + word3.as_flag_sv_config3 + word3.as_flag_sv_config4 + word3.parity
        self.data += word4.as_flag_sv_config5 + word4.as_flag_sv_config6 + word4.as_flag_sv_config7 + word4.as_flag_sv_config8 + word4.as_flag_sv_config9 + word4.as_flag_sv_config10 + word4.parity
        self.data += word5.as_flag_sv_config11 + word5.as_flag_sv_config12 + word5.as_flag_sv_config13 + word5.as_flag_sv_config14 + word5.as_flag_sv_config15 + word5.as_flag_sv_config16 + word5.parity
        self.data += word6.as_flag_sv_config17 + word6.as_flag_sv_config18 + word6.as_flag_sv_config19 + word6.as_flag_sv_config20 + word6.as_flag_sv_config21 + word6.as_flag_sv_config22 + word6.parity
        self.data += word7.as_flag_sv_config23 + word7.as_flag_sv_config24 + word7.as_flag_sv_config25 + word7.as_flag_sv_config26 + word7.as_flag_sv_config27 + word7.as_flag_sv_config28 + word7.parity
        self.data += word8.as_flag_sv_config29 + word8.as_flag_sv_config30 + word8.as_flag_sv_config31 + word8.as_flag_sv_config32 + word8.unknown + word8.parity
        self.data += word9.sv_25 + word9.sv_26 + word9.sv_27 + word9.sv_28 + word9.parity
        self.data += word10.sv_29 + word10.sv_30 + word10.sv_31 + word10.sv_32 + word10.parity

    def __str__(self):
        return f"""{''.join(map(str, (self.word1.preamble + self.word1.reserved + self.word1.parity)))}
{''.join(map(str, (self.word2.time_of_week + self.word2.alert_flag + self.word2.anti_spoofing + self.word2.subframe_id + self.word2.parity_bits + self.word2.parity)))}
{''.join(map(str, (self.word3.unknown + self.word3.as_flag_sv_config1 + self.word3.as_flag_sv_config2 + self.word3.as_flag_sv_config3 + self.word3.as_flag_sv_config4 + self.word3.parity)))}
{''.join(map(str, (self.word4.as_flag_sv_config5 + self.word4.as_flag_sv_config6 + self.word4.as_flag_sv_config7 + self.word4.as_flag_sv_config8 + self.word4.as_flag_sv_config9 + self.word4.as_flag_sv_config10 + self.word4.parity)))}
{''.join(map(str, (self.word5.as_flag_sv_config11 + self.word5.as_flag_sv_config12 + self.word5.as_flag_sv_config13 + self.word5.as_flag_sv_config14 + self.word5.as_flag_sv_config15 + self.word5.as_flag_sv_config16 + self.word5.parity)))}
{''.join(map(str, (self.word6.as_flag_sv_config17 + self.word6.as_flag_sv_config18 + self.word6.as_flag_sv_config19 + self.word6.as_flag_sv_config20 + self.word6.as_flag_sv_config21 + self.word6.as_flag_sv_config22 + self.word6.parity)))}
{''.join(map(str, (self.word7.as_flag_sv_config23 + self.word7.as_flag_sv_config24 + self.word7.as_flag_sv_config25 + self.word7.as_flag_sv_config26 + self.word7.as_flag_sv_config27 + self.word7.as_flag_sv_config28 + self.word7.parity)))}
{''.join(map(str, (self.word8.as_flag_sv_config29 + self.word8.as_flag_sv_config30 + self.word8.as_flag_sv_config31 + self.word8.as_flag_sv_config32 + self.word8.unknown + self.word8.parity)))}
{''.join(map(str, (self.word9.sv_25 + self.word9.sv_26 + self.word9.sv_27 + self.word9.sv_28 + self.word9.parity)))}
{''.join(map(str, (self.word10.sv_29 + self.word10.sv_30 + self.word10.sv_31 + self.word10.sv_32 + self.word10.parity)))}"""