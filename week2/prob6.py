# 예산

def solution(d, budget):
    d.sorted()
    for i in range(len(d)):
        budget -= d[i]