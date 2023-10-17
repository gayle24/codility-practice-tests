import random

def solution(A, F, M):
    N=len(A)
    a_sum = 0
    for i in A:
        a_sum += i
    tot_rolls = N + F
    total = M*tot_rolls
    f_sum = total - a_sum
    possible_values = [3, 2, 4, 3]
    print(sum(possible_values))
    return possible_values



val1 = [3, 2, 4, 3]
val2 = 2
val3 = 4
print(solution(val1, val2, val3))