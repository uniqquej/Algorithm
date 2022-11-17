# 예산

def solution(d, budget):
    d.sort()
    count = 0
    for i in d:
        budget -= i
        if budget < 0 :
            return count
       
        count += 1
        return count    
    
print(solution([2,2,3,3], 10))