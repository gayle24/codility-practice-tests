def solution(S):
    count = 0
    N = len(S)
    i = 0
    while i < N:   
         if S[i] == "X":
            count +=1
            i += 2
         else: i+=1
    return count
        

str = '.X.X.XX....X'
print(solution(str))
print(solution(".X..X"))        # Output: 2
print(solution("X.XXXXX.X."))   # Output: 3
print(solution("XX.XXX.."))     # Output: 2
print(solution("XXXX"))         # Output: 2
print(solution('.X...XX'))      # Output: 2