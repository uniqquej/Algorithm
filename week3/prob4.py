# 4. 콜라츠 추측

def solution(num):
    if num == 1:
        return 0
    
    count = 0
    while (num!=1):
        if num%2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
            
        if count == 500:
            return -1
        
        count += 1
    return count

print(solution(16))