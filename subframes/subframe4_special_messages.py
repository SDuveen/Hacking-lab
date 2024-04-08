from dataclasses import dataclass
from .utils import calculate_parity_bits, gps_time, int_to_bits

def create_subframe4_special_messages(page, date):
    week_number, time_of_week = gps_time(date)

    word1 = Subframe4_Word1()
    word2 = Subframe4_Word2(time_of_week, [ 0, 0 ], word1.parity[-2], word1.parity[-1])
    word3 = Subframe4_Word3(page, word2.parity[-2], word2.parity[-1])
    word4 = Subframe4_Word4(word3.parity[-2], word3.parity[-1])
    word5 = Subframe4_Word5(word4.parity[-2], word4.parity[-1])
    word6 = Subframe4_Word6(word5.parity[-2], word5.parity[-1])
    word7 = Subframe4_Word7(word6.parity[-2], word6.parity[-1])
    word8 = Subframe4_Word8(word7.parity[-2], word7.parity[-1])
    word9 = Subframe4_Word9(word8.parity[-2], word8.parity[-1])
    word10 = Subframe4_Word10([ 0, 0 ], word9.parity[-2], word9.parity[-1])

    return Subframe4(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10)

@dataclass
class Subframe4_Word1:
    preamble          = [ 1, 0, 0, 0, 1, 0, 1, 1 ]
    reserved          = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
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
    data_id = [ 0, 0 ]
    sv_id: list[int] # 6 bits
    char1 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    char2 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int] # 6 bits

    def __init__(self, page, D29, D30):
        self.sv_id = {
            1: [ 1, 1, 1, 0, 0, 1 ],
            2: [ 0, 1, 1, 0, 0, 1 ],
            3: [ 0, 1, 1, 0, 1, 0 ],
            4: [ 0, 1, 1, 0, 1, 1 ],
            5: [ 0, 1, 1, 1, 0, 0 ],
            6: [ 1, 1, 1, 0, 0, 1 ],
            7: [ 0, 1, 1, 1, 0, 1 ],
            8: [ 0, 1, 1, 1, 1, 0 ],
            9: [ 0, 1, 1, 1, 1, 1 ],
            10: [ 1, 0, 0, 0, 0, 0 ],
            11: [ 1, 1, 1, 0, 0, 1 ],
            12: [ 1, 1, 1, 1, 1, 0 ],
            13: [ 1, 1, 0, 1, 0, 0 ],
            14: [ 1, 1, 0, 1, 0, 1 ],
            15: [ 1, 1, 0, 1, 1, 0 ],
            16: [ 1, 1, 1, 0, 0, 1 ],
            17: [ 1, 1, 0, 1, 1, 1 ],
            18: [ 1, 1, 1, 0, 0, 0 ],
            19: [ 1, 1, 1, 0, 1, 0 ],
            20: [ 1, 1, 1, 0, 1, 1 ],
            21: [ 1, 1, 1, 0, 0, 1 ],
            22: [ 1, 1, 1, 1, 0, 0 ],
            23: [ 1, 1, 1, 1, 0, 1 ],
            24: [ 1, 1, 1, 1, 1, 0 ],
            25: [ 1, 1, 1, 1, 1, 1 ],
        }[page]

        self.parity = calculate_parity_bits(data_bits=self.data_id + self.sv_id + self.char1 + self.char2, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word4:
    char3 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    char4 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    char5 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.char3 + self.char4 + self.char5, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word5:
    char6 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    char7 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    char8 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.char6 + self.char7 + self.char8, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word6:
    char9 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    char10 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    char11 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.char9 + self.char10 + self.char11, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word7:
    char12 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    char13 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    char14 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.char12 + self.char13 + self.char14, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word8:
    char15 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    char16 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    char17 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.char15 + self.char16 + self.char17, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word9:
    char18 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    char19 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    char20 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.char18 + self.char19 + self.char20, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word10:
    char21 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    char22 = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    reserved = [ 0, 0, 0, 0, 0, 0 ]
    parity_bits: list[int] # 2 bits
    parity: list[int] # 6 bits

    def __init__(self, parity_bits, D29, D30):
        self.parity_bits = parity_bits
        self.parity = calculate_parity_bits(data_bits=self.char21 + self.char22 + self.reserved + self.parity_bits, previous_D29=D29, previous_D30=D30, first_word=False)


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
        self.data += word3.data_id + word3.sv_id + word3.char1 + word3.char2 + word3.parity
        self.data += word4.char3 + word4.char4 + word4.char5 + word4.parity
        self.data += word5.char6 + word5.char7 + word5.char8 + word5.parity
        self.data += word6.char9 + word6.char10 + word6.char11 + word6.parity
        self.data += word7.char12 + word7.char13 + word7.char14 + word7.parity
        self.data += word8.char15 + word8.char16 + word8.char17 + word8.parity
        self.data += word9.char18 + word9.char19 + word9.char20 + word9.parity
        self.data += word10.char21 + word10.char22 + word10.reserved + word10.parity_bits + word10.parity

    def __str__(self):
        return f"""{''.join(map(str, (self.word1.preamble + self.word1.reserved + self.word1.parity)))}
{''.join(map(str, (self.word2.time_of_week + self.word2.alert_flag + self.word2.anti_spoofing + self.word2.subframe_id + self.word2.parity_bits + self.word2.parity)))}
{''.join(map(str, (self.word3.data_id + self.word3.sv_id + self.word3.char1 + self.word3.char2 + self.word3.parity)))}
{''.join(map(str, (self.word4.char3 + self.word4.char4 + self.word4.char5 + self.word4.parity)))}
{''.join(map(str, (self.word5.char6 + self.word5.char7 + self.word5.char8 + self.word5.parity)))}
{''.join(map(str, (self.word6.char9 + self.word6.char10 + self.word6.char11 + self.word6.parity)))}
{''.join(map(str, (self.word7.char12 + self.word7.char13 + self.word7.char14 + self.word7.parity)))}
{''.join(map(str, (self.word8.char15 + self.word8.char16 + self.word8.char17 + self.word8.parity)))}
{''.join(map(str, (self.word9.char18 + self.word9.char19 + self.word9.char20 + self.word9.parity)))}
{''.join(map(str, (self.word10.char21 + self.word10.char22 + self.word10.reserved + self.word10.parity_bits + self.word10.parity)))}"""
