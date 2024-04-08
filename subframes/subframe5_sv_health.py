from dataclasses import dataclass
from .utils import calculate_parity_bits, gps_time, int_to_bits, random_bits

def create_subframe5_sv_health(page, date):
    week_number, time_of_week = gps_time(date)

    word1 = Subframe5_Word1()
    word2 = Subframe5_Word2(time_of_week, [ 0, 0 ], word1.parity[-2], word1.parity[-1])
    word3 = Subframe5_Word3(page, word2.parity[-2], word2.parity[-1])
    word4 = Subframe5_Word4(word3.parity[-2], word3.parity[-1])
    word5 = Subframe5_Word5(word4.parity[-2], word4.parity[-1])
    word6 = Subframe5_Word6(word5.parity[-2], word5.parity[-1])
    word7 = Subframe5_Word7(word6.parity[-2], word6.parity[-1])
    word8 = Subframe5_Word8(word7.parity[-2], word7.parity[-1])
    word9 = Subframe5_Word9(word8.parity[-2], word8.parity[-1])
    word10 = Subframe5_Word10([ 0, 0 ], word9.parity[-2], word9.parity[-1])

    return Subframe5(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10)

@dataclass
class Subframe5_Word1:
    preamble          = [ 1, 0, 0, 0, 1, 0, 1, 1 ]
    reserved          = random_bits(16)
    parity: list[int] # 6 bits

    def __init__(self):
        self.parity = calculate_parity_bits(data_bits=self.preamble + self.reserved, previous_D29=0, previous_D30=0, first_word=True)

@dataclass
class Subframe5_Word2:
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
class Subframe5_Word3:
    data_id = random_bits(2)
    sv_id:   list[int] # 6 bits
    t_oe = random_bits(8)
    wn_a = random_bits(8)
    parity: list[int] # 6 bits

    def __init__(self, page, D29, D30):
        self.sv_id = {
            1: [ 0, 0, 0, 0, 0, 1 ],
            2: [ 0, 0, 0, 0, 1, 0 ],
            3: [ 0, 0, 0, 0, 1, 1 ],
            4: [ 0, 0, 0, 1, 0, 0 ],
            5: [ 0, 0, 0, 1, 0, 1 ],
            6: [ 0, 0, 0, 1, 1, 0 ],
            7: [ 0, 0, 0, 1, 1, 1 ],
            8: [ 0, 0, 1, 0, 0, 0 ],
            9: [ 0, 0, 1, 0, 0, 1 ],
            10: [ 0, 0, 1, 0, 1, 0 ],
            11: [ 0, 0, 1, 0, 1, 1 ],
            12: [ 0, 0, 1, 1, 0, 0 ],
            13: [ 0, 0, 1, 1, 0, 1 ],
            14: [ 0, 0, 1, 1, 1, 0 ],
            15: [ 0, 0, 1, 1, 1, 1 ],
            16: [ 0, 1, 0, 0, 0, 0 ],
            17: [ 0, 1, 0, 0, 0, 1 ],
            18: [ 0, 1, 0, 0, 1, 0 ],
            19: [ 0, 1, 0, 0, 1, 1 ],
            20: [ 0, 1, 0, 1, 0, 0 ],
            21: [ 0, 1, 0, 1, 0, 1 ],
            22: [ 0, 1, 0, 1, 1, 0 ],
            23: [ 0, 1, 0, 1, 1, 1 ], 
            24: [ 0, 1, 1, 0, 0, 0 ],
            25: [ 1, 1, 0, 0, 1, 1 ],
        }[page]

        self.parity = calculate_parity_bits(data_bits=self.data_id + self.sv_id + self.t_oe + self.wn_a, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe5_Word4:
    sv_1 = random_bits(6)
    sv_2 = random_bits(6)
    sv_3 = random_bits(6)
    sv_4 = random_bits(6)
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.sv_1 + self.sv_2 + self.sv_3 + self.sv_4, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe5_Word5:
    sv_5 = random_bits(6)
    sv_6 = random_bits(6)
    sv_7 = random_bits(6)
    sv_8 = random_bits(6)
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.sv_5 + self.sv_6 + self.sv_7 + self.sv_8, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe5_Word6:
    sv_9  = random_bits(6)
    sv_10 = random_bits(6)
    sv_11 = random_bits(6)
    sv_12 = random_bits(6)
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.sv_9 + self.sv_10 + self.sv_11 + self.sv_12, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe5_Word7:
    sv_13 = random_bits(6)
    sv_14 = random_bits(6)
    sv_15 = random_bits(6)
    sv_16 = random_bits(6)
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.sv_13 + self.sv_14 + self.sv_15 + self.sv_16, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe5_Word8:
    sv_17 = random_bits(6)
    sv_18 = random_bits(6)
    sv_19 = random_bits(6)
    sv_20 = random_bits(6)
    parity: list[int]   # 6 bits

    def __init__(self, D29, D30):   
        self.parity = calculate_parity_bits(data_bits=self.sv_17 + self.sv_18 + self.sv_19 + self.sv_20, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe5_Word9:
    sv_21 = random_bits(6)
    sv_22 = random_bits(6)
    sv_23 = random_bits(6)
    sv_24 = random_bits(6)
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.sv_21 + self.sv_22 + self.sv_23 + self.sv_24, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe5_Word10:
    reserved = random_bits(6)
    reserved_system_use = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity_bits: list[int] # 2 bits
    parity:      list[int] # 6 bits

    def __init__(self, parity_bits, D29, D30):
        self.parity_bits = parity_bits
        self.parity = calculate_parity_bits(data_bits=self.reserved + self.reserved_system_use + self.parity_bits, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe5:
    word1: Subframe5_Word1
    word2: Subframe5_Word2
    word3: Subframe5_Word3
    word4: Subframe5_Word4
    word5: Subframe5_Word5
    word6: Subframe5_Word6
    word7: Subframe5_Word7
    word8: Subframe5_Word8
    word9: Subframe5_Word9
    word10: Subframe5_Word10

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
        self.data += word3.data_id + word3.sv_id + word3.t_oe + word3.wn_a + word3.parity
        self.data += word4.sv_1 + word4.sv_2 + word4.sv_3 + word4.sv_4 + word4.parity
        self.data += word5.sv_5 + word5.sv_6 + word5.sv_7 + word5.sv_8 + word5.parity
        self.data += word6.sv_9 + word6.sv_10 + word6.sv_11 + word6.sv_12 + word6.parity
        self.data += word7.sv_13 + word7.sv_14 + word7.sv_15 + word7.sv_16 + word7.parity
        self.data += word8.sv_17 + word8.sv_18 + word8.sv_19 + word8.sv_20 + word8.parity
        self.data += word9.sv_21 + word9.sv_22 + word9.sv_23 + word9.sv_24 + word9.parity
        self.data += word10.reserved + word10.reserved_system_use + word10.parity_bits + word10.parity

    def __str__(self):
        return f"""{''.join(map(str, (self.word1.preamble + self.word1.reserved + self.word1.parity)))}
{''.join(map(str, (self.word2.time_of_week + self.word2.alert_flag + self.word2.anti_spoofing + self.word2.subframe_id + self.word2.parity_bits + self.word2.parity)))}
{''.join(map(str, (self.word3.data_id + self.word3.sv_id + self.word3.t_oe + self.word3.wn_a + self.word3.parity)))}
{''.join(map(str, (self.word4.sv_1 + self.word4.sv_2 + self.word4.sv_3 + self.word4.sv_4 + self.word4.parity)))}
{''.join(map(str, (self.word5.sv_5 + self.word5.sv_6 + self.word5.sv_7 + self.word5.sv_8 + self.word5.parity)))}
{''.join(map(str, (self.word6.sv_9 + self.word6.sv_10 + self.word6.sv_11 + self.word6.sv_12 + self.word6.parity)))}
{''.join(map(str, (self.word7.sv_13 + self.word7.sv_14 + self.word7.sv_15 + self.word7.sv_16 + self.word7.parity)))}
{''.join(map(str, (self.word8.sv_17 + self.word8.sv_18 + self.word8.sv_19 + self.word8.sv_20 + self.word8.parity)))}
{''.join(map(str, (self.word9.sv_21 + self.word9.sv_22 + self.word9.sv_23 + self.word9.sv_24 + self.word9.parity)))}
{''.join(map(str, (self.word10.reserved + self.word10.reserved_system_use + self.word10.parity_bits + self.word10.parity)))}"""