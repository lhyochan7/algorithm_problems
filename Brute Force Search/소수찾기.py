from itertools import permutations
import math

# Check if prime number
def prime_num(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    x = set()
    
    # Use permutation to find all possible cases
    for i in range(1, len(numbers)+1):
        x |= set(map(int, map(''.join, permutations(numbers, i))))
    
    for num in x:
        # remove 0, 1 because they are not prime
        if num in (0, 1):
            continue
        
        if prime_num(num):
            answer += 1
    
    return answer