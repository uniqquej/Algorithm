# 두 정수 사이의 합
def solution(a,b):
    num = []
    if a > b:
        a,b = b,a
        
    for i in range(a, b+1):
        num.append(i)
    answer = sum(num)
    return answer

print(solution(3,5))