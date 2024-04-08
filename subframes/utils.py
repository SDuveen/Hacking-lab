from datetime import datetime, timedelta
from random import randint

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

def int_to_bits(n, bits):
    return [int(x) for x in list(f'{n:0{bits}b}')][:bits]

def random_bits(bits):
    return [int(x) for x in list(f'{randint(0, 2**bits):0{bits}b}')][:bits]