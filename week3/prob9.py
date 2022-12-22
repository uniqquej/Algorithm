# 9. 폰켓몬
def solution(nums):
    new_nums = set(nums)
    if len(nums) / 2 >= len(new_nums):
        answer = len(new_nums)

    else:
        answer = len(nums) / 2

    return answer
