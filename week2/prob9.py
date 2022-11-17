# 실패율
def solution(N, stages):
    fail = []
    for i in range(1, N + 1):
        count_no_clear = 0
        count_clear = 0
        for j in stages:
            if i == j:
                count_no_clear += 1
            if i <= j:
                count_clear += 1
            
        if count_clear == 0:
            fail.append(0)
        else:
            fail.append(count_no_clear / count_clear)

        answer = {}        
        for i in range(len(fail)):
            answer[i + 1] = fail[i]

    answer = sorted(answer.keys(), key=lambda key:answer[key], reverse=True)

    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
