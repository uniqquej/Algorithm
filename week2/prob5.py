#음양 더하기

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
        
    return answer

print(solution([4,7,12],[True, False, True]))
        