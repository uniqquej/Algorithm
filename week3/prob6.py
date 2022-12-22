# 6. 가운데 글자 가져오기

def solution(s):
    
    idx = len(s)//2
    
    if len(s) % 2 != 0:
        return s[idx]
    else:
        return s[idx -1]+s[idx]
    
print(solution("qwer"))