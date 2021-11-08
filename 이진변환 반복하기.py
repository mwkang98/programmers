def sosu(n):
    temp=[]
    while(1):
        temp.append(n%2)
        n=int(n/2)
        if(n<1):
            break
    temp.reverse()
    result=""
    for i in range(len(temp)):
        result=result+str(temp[i])
    return result
def change(n):
    count=0
    for i in range(len(n)):
        if(n[i]=='0'):
            count+=1
    a=len(n)-count
    result=sosu(a)
    return result,count
def solution(s):
    count=0
    t=0
    a=s
    while(1):
        t+=1
        a,b=change(a)
        count+=b
        if(a=="1"):
            break
    answer=[]
    answer.append(t)
    answer.append(count)
    return answer
print(solution("110010101001"))
