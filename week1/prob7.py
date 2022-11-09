# 비밀지도 - 2018 KAKAO BLIND RECRUITMENT
def solution(n, arr1, arr2):
    
    answer = []

    for i in range(n):
        a1 = str(format(arr1[i],'b')).zfill(n)
        b1 = str(format(arr2[i],'b')).zfill(n)
        row = ""
        
        for j in range(n):
            if (a1[j] == "0") & (b1[j] == "0"):
                row += "0"
            else:
                row += "1"

        result = row.replace("0"," ")
        result = result.replace("1","#")

        answer.append(result)
        
    return answer