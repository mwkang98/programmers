def solution(progresses, speeds):
    days=[]
    works=[]
    for i in range(0,len(progresses)):
        k=progresses[i]
        count=0
        while(1):
            if(k>=100):
                break
            k+=speeds[i]
            count+=1
        days.append(count)
    print(days)
    i=0
    while(1):
        j=1
        while(1):
            if(i+j==len(days)):
                    break
            if(days[i]>days[i+j]):
                j=j+1
            else:
                break
        works.append(j)
        i=i+j
        if(i==len(days)):
                break
    answer=works.copy()
    print(answer)
    return answer
solution([99,1,99,1],[1,1,1,1] )
