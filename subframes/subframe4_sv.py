from dataclasses import dataclass
from .utils import calculate_parity_bits, gps_time, int_to_bits

def create_subframe4_sv(page, date):
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
    sv_id:   list[int] # 6 bits
    eccentricity = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
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

        self.parity = calculate_parity_bits(data_bits=self.data_id + self.sv_id + self.eccentricity, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word4:
    time_of_ephemeris = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    delta_inclination = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.time_of_ephemeris + self.delta_inclination, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word5:
    rate_of_right_ascension = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    sv_health               = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.rate_of_right_ascension + self.sv_health, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word6:
    sqrt_a = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.sqrt_a, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word7:
    longitude_of_ascension_node = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity:     list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.longitude_of_ascension_node, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word8:
    argument_of_perigee = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int]   # 6 bits

    def __init__(self, D29, D30):   
        self.parity = calculate_parity_bits(data_bits=self.argument_of_perigee, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word9:
    mean_anomaly = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    parity: list[int] # 6 bits

    def __init__(self, D29, D30):
        self.parity = calculate_parity_bits(data_bits=self.mean_anomaly, previous_D29=D29, previous_D30=D30, first_word=False)

@dataclass
class Subframe4_Word10:
    a_f0_msb = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    a_f1     = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    a_f0_lsb = [ 0, 0, 0 ]
    parity_bits: list[int] # 2 bits
    parity:      list[int] # 6 bits

    def __init__(self, parity_bits, D29, D30):
        self.parity_bits = parity_bits
        self.parity = calculate_parity_bits(data_bits=self.a_f0_msb + self.a_f1 + self.a_f0_lsb + self.parity_bits, previous_D29=D29, previous_D30=D30, first_word=False)

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
        self.data += word3.sv_id + word3.eccentricity + word3.parity
        self.data += word4.time_of_ephemeris + word4.delta_inclination + word4.parity
        self.data += word5.rate_of_right_ascension + word5.sv_health + word5.parity
        self.data += word6.sqrt_a + word6.parity
        self.data += word7.longitude_of_ascension_node + word7.parity
        self.data += word8.argument_of_perigee + word8.parity
        self.data += word9.mean_anomaly + word9.parity
        self.data += word10.a_f0_msb + word10.a_f1 + word10.a_f0_lsb + word10.parity_bits + word10.parity

    def __str__(self):
        return f"""{''.join(map(str, (self.word1.preamble + self.word1.reserved + self.word1.parity)))}
{''.join(map(str, (self.word2.time_of_week + self.word2.alert_flag + self.word2.anti_spoofing + self.word2.subframe_id + self.word2.parity_bits + self.word2.parity)))}
{''.join(map(str, (self.word3.data_id + self.word3.sv_id + self.word3.eccentricity + self.word3.parity)))}
{''.join(map(str, (self.word4.time_of_ephemeris + self.word4.delta_inclination + self.word4.parity)))}
{''.join(map(str, (self.word5.rate_of_right_ascension + self.word5.sv_health + self.word5.parity)))}
{''.join(map(str, (self.word6.sqrt_a + self.word6.parity)))}
{''.join(map(str, (self.word7.longitude_of_ascension_node + self.word7.parity)))}
{''.join(map(str, (self.word8.argument_of_perigee + self.word8.parity)))}
{''.join(map(str, (self.word9.mean_anomaly + self.word9.parity)))}
{''.join(map(str, (self.word10.a_f0_msb + self.word10.a_f1 + self.word10.a_f0_lsb + self.word10.parity_bits + self.word10.parity)))}"""