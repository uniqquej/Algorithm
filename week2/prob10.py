# 소수 만들기

from itertools import combinations

def solution(nums):
    
    comb = list(combinations(nums,3))
    prime_cnt = 0
    for i in comb:
        sum_num = sum(i)
        count = 0
        for n in range(2, (sum_num//2)+1):
            if sum_num % n == 0:
                count += 1
                
        if count == 0:
            prime_cnt += 1
    
    return prime_cnt
                       
    
print(solution([1,2,7,6,4]))
        