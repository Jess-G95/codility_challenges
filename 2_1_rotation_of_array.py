'''
Rotate an array to the right by a given number of steps.
'''

def solution(A, K):
    if len(A) == 0:
        return A
    else:
        for i in range(K):
            last_num = A.pop()
            A.insert(0, last_num)
        return A

mylist = [1,2,3,4]

print(solution(mylist,1))