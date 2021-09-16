#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
i = 0
while (i < len(roman_string)):
    if roman_string[i] == 'M':
        result += 1000
        i += 1
        continue
    elif roman_string[i] == 'C':
        if roman_string[i + 1] == 'M':
            result += 900
            i += 2
            continue
        elif roman_string[i + 1] == 'D':
            result += 400
            i += 2
            continue
        result += 100
        i += 1
        continue
    elif roman_string[i] == 'D':
        result += 500
        i += 1
        continue
    elif roman_string[i] == 'X':
        if roman_string[i + 1] == 'C':
            result += 90
            i += 2
            continue
        elif roman_string[i + 1] == 'L':
            result += 40
            i += 2
            continue
        result += 10
        i += 1
        continue
    elif roman_string[i] == 'L':
        result += 50
        i += 1
        continue
    elif roman_string[i] == 'I':
        if roman_string[i + 1] == 'X':
            result += 9
            i += 2
            continue
        elif roman_string[i + 1] == 'V':
            result += 4
            i += 2
            continue
        result += 1
        i +=1
        continue
    elif roman_string[i] == 'V':
        result += 5
        i += 1
        continue
    return result
