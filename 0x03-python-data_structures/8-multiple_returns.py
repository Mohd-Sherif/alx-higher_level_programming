#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentance) > 0:
        return tuple(len(sentance), sentance[0])
    else:
        return tuple(len(sentance), None)
