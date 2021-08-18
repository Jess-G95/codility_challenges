'''
Find the missing element in a given permutation.
'''

def solution(A):
    # write your code in Python 3.6
    sorted_set = sorted(A)
    base = 1

    for num in sorted_set:
        if num == base:
            base += 1
        else:
            break

    return base

A = [1,2,4,5,8,9]

print(solution(A))