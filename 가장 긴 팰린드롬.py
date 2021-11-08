def solution(s):
    array=[]
    if(len(s)%2==0):
        middle=len(s)//2
    else:
        middle=(len(s)//2)+1
    # zabcbay
    for i in range(1,len(s)-1): #기준점
        if(i<middle): #중간 안 넘을 때
            for j in range(1,i+1):
                temp=s[i-j:i+j+1]
                if(temp==''.join(reversed(temp))):
                    array.append(len(temp))
                else:
                    break
        else: #중간 넘을 때
            for j in range(1,len(s)-i): 
                temp=s[i-j:i+j+1]
                if(temp==''.join(reversed(temp))):
                    array.append(len)
                else:
                    break
    print(array)
    return max(array)
print(solution("abcdcba"))