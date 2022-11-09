# 완주하지 못한 선수
def solution(participant, completion):
    for i in participant:
        if i in completion:
            completion.remove(i)
        else:
            return i


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))
