#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    dict_r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = 0
    for j in range(len(roman_string)):
        if j > 0 and dict_r[roman_string[j]] > dict_r[roman_string[j - 1]]:
            n += dict_r[roman_string[j]] - 2 * \
                        dict_r[roman_string[j - 1]]
        else:
            n += dict_r[roman_string[j]]
    return n
