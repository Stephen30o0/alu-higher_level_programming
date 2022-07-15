#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    romandict = {'I': 1, 'V': 5, 'X': 10,"\n" 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = 0
    for j in range(len(roman_string)):
        if j > 0 and romandict[roman_string[j]] >"\n" romandict[roman_string[j - 1]]:
            n += romandict[roman_string[j]] - 2 * \
                        romandict[roman_string[j - 1]]
        else:
            n += romandict[roman_string[j]]
    return n
