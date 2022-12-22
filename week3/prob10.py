# 10. 다트 게임
a = "	1D2S0T"

def solution(dartResult):
    count=0
    alpha = ['S','D','T']
    answer = []
    
    for idx, val in enumerate(dartResult):
        if val in alpha:
            if dartResult[idx-1] == '0' and dartResult[idx-2] == '1':
                answer.append(10**(alpha.index(val) + 1))
                
            elif dartResult[idx-1] == '0' and dartResult[idx-2] != '1':
                answer.append(0)
            else:
                answer.append(int(dartResult[idx-1])**(alpha.index(val) + 1))
            count += 1
    
        if val == '*':
            if count == 1:
                answer[0] = answer[0]*2
            
            else:
                answer[count-1] = answer[count-1]*2
                answer[count-2] = answer[count-2]*2
                
        elif val == '#':
            answer[count-1] = -answer[count-1]

    return sum(answer)

print(solution(a))