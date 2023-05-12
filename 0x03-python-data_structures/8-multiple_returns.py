#!/usr/bin/python3
def multiple_returns(sentence):
    sent_lenss = len(sentence)

    if (sent_lenss == 0):
        new_tuple = (sent_lenss, None)
    else:
        new_tuple = (sent_lenss, sentence[0])

    return (new_tuple)
