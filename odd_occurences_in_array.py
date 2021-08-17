A = [9,3,9,3,9,7,9]

def solution(A):
    for n in A:
        if A.count(n) == 1:
            return n

print(solution(A))