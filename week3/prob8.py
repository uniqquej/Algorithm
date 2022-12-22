# 8. H-index

# h번 이상 인용된 논문이 h편이상
# n-h편이 h번 이하로 인용 / n = len(citations)
# max(h) = H-index
citations = [6,8,0,2,4,7]

def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)

    print(citations)
    for i in range(n):
        if citations[i] <= i+1:
            return citations[i]
            
        
print(solution(citations))