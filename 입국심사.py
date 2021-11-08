def solution(n, times):
    times=sorted(times)
    array={}
    for i in range(len(times)):
        array[times[i]]=0
    for i in range(n):
        for j in range(len(times)):
            k=array[times[j]]+times[j]
            if(j==0):
                temp=k
                q=times[j]
            else:
                if(k<temp):
                    temp=k
                    q=times[j]
        array[q]+=q
    print(array)
    return max(array.values())
print(solution(10,[1,2,3]))      
