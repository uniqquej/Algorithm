# 3. 제일 작은 수 제거하기

def solution(arr):
    arr.remove(min(arr))

    if len(arr)==1:
        return [-1]
    return arr

print(solution([4,3,2,1]))