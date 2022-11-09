# 자연수 뒤집어 배열로 만들기

def solution(n):
    num = str(n)
    result = []
    for i in num[::-1]:
        result.append(int(i))
    return result