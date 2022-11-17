#k번째 수

def solution(array, commands):
    answer = []
    for i in commands:
        new = sorted(array[i[0]-1:i[1]])
        answer.append(new[i[2]-1])
    return answer
        

commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
array = [1, 5, 2, 6, 3, 7, 4] 
print(solution(array, commands))
        