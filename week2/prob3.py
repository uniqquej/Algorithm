# 정수 내림차순으로 배치하기

def solution(n):
    answer = ''.join(sorted(str(n), reverse=True))
    return int(answer)

print(solution(1680246))
