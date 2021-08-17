import math

def solution(X, Y, D):
    distance = Y - X
    return math.ceil(distance / D)