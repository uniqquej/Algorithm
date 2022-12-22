# 문자열 내 p와 y의 개수

def solution(s):
    new = s.lower()
    p_cnt = new.count('p')
    y_cnt = new.count('y')
    
    if (p_cnt == y_cnt):
        return True
    else:
        return False 
    
print(solution("Pyy"))