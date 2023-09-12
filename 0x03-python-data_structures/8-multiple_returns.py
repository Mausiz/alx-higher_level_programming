#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    """ returns a tuple with len of str & first xcter."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
