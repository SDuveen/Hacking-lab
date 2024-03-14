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