#약수의 개수와 덧셈 - 월간 코드 챌린지 시즌2

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        cnt = 0
        
        for j in range(1, i//2 +1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 :
            answer += i
        else:
            answer -= i
            
    return answer