#체육복 - 탐욕법(Greedy)

n = 5
lost = [2,4]
reserve = [1,3,5]

def solution(n, lost, reserve):
    total = n - len(lost)

    for i in lost:
        if (i+1) in reserve or (i-1) in reserve:
            total += 1
            
    return answer