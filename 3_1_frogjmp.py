'''
Count minimal number of jumps from position X to Y.
'''

import math

def solution(X, Y, D):
    distance = Y - X
    return math.ceil(distance / D)