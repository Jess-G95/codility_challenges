'''
Find the value that occurs once in an odd number of elements. The other elements will appear in pairs. 
'''


A = [9,3,9,3,9,7,9]

def solution(A):
    for n in A:
        if A.count(n) == 1:
            return n

print(solution(A))