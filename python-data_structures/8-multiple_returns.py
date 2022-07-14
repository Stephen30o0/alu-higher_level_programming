#!/usr/bin/python3
def multiple_returns(sentence):
    det = ()
    if len(sentence) == 0:
        det = 0, "None"
    else:
        det = len(sentence), sentence[0]
    return det
