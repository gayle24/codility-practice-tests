import random

def solution(A, F, M):
    N=len(A)
    a_sum = 0
    for i in A:
        a_sum += i
    tot_rolls = N + F
    total = M*tot_rolls
    f_sum = total - a_sum
    possible_values = []

    if f_sum> 6 * F or f_sum < F:
        return [0]

    while sum(possible_values) != f_sum:
        possible_values = [random.randint(1, 6) for _ in range(F)]

    return possible_values
    
A = [1, 5, 6]
F = 4
M = 3
print(solution(A=A, F=F, M=M))
print(solution(A = [6, 1], F = 1, M = 1))
print(solution( A = [1, 2, 3, 4], F = 4, M = 6))
print(solution(A = [3, 2, 4, 3], F = 2, M = 4))