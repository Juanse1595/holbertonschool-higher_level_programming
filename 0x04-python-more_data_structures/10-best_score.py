#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    max_value = a_dictionary[list(a_dictionary.keys())[0]]
    for key in a_dictionary:
        if a_dictionary[key] > max_value:
            answer = key
            max_value = a_dictionary[key]
    return answer
