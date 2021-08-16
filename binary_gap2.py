def solution(N):
    binary_num = str(bin(N)[2:])
    binary_gap = binary_num.split('1')
    max_gap = 0

    if binary_num.count('1') == 1 or binary_num.count('0') == 0:
        return max_gap
    else:
        for i in range(len(binary_gap)):
            if len(binary_gap[i]) > max_gap:
                max_gap = len(binary_gap[i])
                return max_gap