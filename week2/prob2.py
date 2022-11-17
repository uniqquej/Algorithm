# 문자열을 정수로 바꾸기

def solution(s):
    answer = 0
    n = 0
    for i in s[:0:-1]:
        answer += int(i)*10**n
        n += 1
    
    if s[0] == '-':
        return -answer
    
    elif s[0] == '+':
        return answer
    
    else:
        answer += int(s[0]) * 10**n
        return answer

print(solution('-408'))        
        