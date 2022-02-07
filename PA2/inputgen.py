import random

def String_to_BitList(data):
    """Turn the string data, into a list of bits (1, 0)'s"""
    l = len(data) * 8
    result = [0] * l
    pos = 0
    for ch in data:
        i = 7
        while i >= 0:
            if ch & (1 << i) != 0:
                result[pos] = 1
            else:
                result[pos] = 0
            pos += 1
            i -= 1
    return result


def BitList_to_String(data):
    """Turn the list of bits -> data, into a string"""
    result = []
    pos = 0
    c = 0
    while pos < len(data):
        c += data[pos] << (7 - (pos % 8))
        if (pos % 8) == 7:
            result.append(c)
            c = 0
        pos += 1
    
    return bytes(result)



plaintext = b"besthero" 

strbit = String_to_BitList(plaintext)

plaintexts_list = [plaintext] # 5 plaintext / keys with 1 hamming distance differnce wrt plaintext (str)

for i in range(5):
    temp = strbit
    temp[i] = 1 - temp[i] # changing 1 bit in the base PT
    plaintexts_list.append(BitList_to_String(temp))




strbit = String_to_BitList(plaintext)

plaintexts_HD_list = [plaintext,] # 6 plaintext with hamming distance differnce from 0 to 5 wrt plaintext (str, bit list)

for i in range(1,6):
    temp = strbit
    for j in range(i):
        temp[j] = 1 - temp[j]  # changing 1 bit in the base PT
    plaintexts_HD_list.append(BitList_to_String(temp))





