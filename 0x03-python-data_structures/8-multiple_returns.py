#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = ()
    new_tuple += len(sentence), 
    if sentence == "":
        new_tuple += None,
        return new_tuple
    new_tuple += sentence[0],
    return new_tuple
