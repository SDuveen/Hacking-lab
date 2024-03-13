from pylfsr import LFSR

lfsr1 = LFSR(initstate=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], fpoly=[10, 3])
lfsr2 = LFSR(initstate=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], fpoly=[10, 9, 8, 6, 3, 2])

table = {
    1: (2, 6),
    2: (3, 7),
    3: (4, 8),
    4: (5, 9),
    5: (1, 9),
    6: (2, 10),
    7: (1, 8),
    8: (2, 9),
    9: (3, 10),
    10: (2, 3),
    11: (3, 4),
    12: (5, 6),
    13: (6, 7),
    14: (7, 8),
    15: (8, 9),
    16: (9, 10),
    17: (1, 4),
    18: (2, 5),
    19: (3, 6),
    20: (4, 7),
    21: (5, 8),
    22: (6, 9),
    23: (1, 3),
    24: (4, 6),
    25: (5, 7),
    26: (6, 8),
    27: (7, 9),
    28: (8, 10),
    29: (1, 6),
    30: (2, 7),
    31: (3, 8),
    32: (4, 9)
}

def gold_code(prn_code):
    gold_code = []
    for _ in range(1023):
        g1 = lfsr1.next()
        lfsr2.next()
        states = table[prn_code]
        g2 = lfsr2.state[states[0]-1] ^ lfsr2.state[states[1]-1]
        gold_code.append(g1 ^ g2)

    return ''.join(map(str, gold_code)), int(''.join(map(str, gold_code)), 2)

def binary_correlation(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Binary strings must be of equal length.")

    n = len(str1)
    
    list1 = [int(bit) for bit in str1]
    list2 = [int(bit) for bit in str2]

    mean1 = sum(list1) / n
    mean2 = sum(list2) / n

    numerator = sum((x - mean1) * (y - mean2) for x, y in zip(list1, list2))
    denominator1 = sum((x - mean1)**2 for x in list1)
    denominator2 = sum((y - mean2)**2 for y in list2)

    correlation = numerator / ((denominator1 * denominator2)**0.5)

    return correlation  

if __name__ == "__main__":
    prn_code = 1
    code, formatted_code = gold_code(prn_code)

    print("Gold code for PRN code {} is: ".format(prn_code), code)
    print("Gold code number for PRN code {} is: ".format(prn_code), formatted_code)