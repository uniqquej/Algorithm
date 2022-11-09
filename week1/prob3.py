#자릿수 더하기
def solution(n):
    num = str(n)
    sum = 0
    for i in num:
        sum += int(i)
    return sum


