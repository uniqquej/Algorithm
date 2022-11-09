# 숫자 문자열과 영단어

def solution(s):
    num_list = ['zero','one','two','three','four','five','six','seven','eight','nine']
   
    for i in range(len(num_list)):
        if num_list[i] in s:
            s = s.replace(num_list[i],str(i))
    return int(s)



