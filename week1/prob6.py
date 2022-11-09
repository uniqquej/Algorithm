
def solution(n, lost, reserve):
    # 중복 숫자 모두 못지움
    # for i in lost:
    #     if i in reserve:
    #         reserve.remove(i)
    #         lost.remove(i)

    # case18,20 error
    # new_reserve = [i for i in reserve if i not in lost]
    # new_lost = [j for j in lost if j not in reserve]

    new_reserve = list(set(reserve)-set(lost))
    new_lost = list(set(lost)-set(reserve))

    total = n - len(new_lost)

    for i in new_lost:
        if (i - 1) in reserve:
            total += 1     
            reserve.remove(i - 1)
        elif (i + 1) in reserve:
            total += 1    
            reserve.remove(i + 1)  
    return total
