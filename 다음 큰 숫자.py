def sosu(num):
    a=[]
    while(1):
        a.append(num%2)
        num=int(num/2)
        if(num<1):
            break
    count=0
    print(a)
    for i in range(len(a)):
        if (a[i]==1):
            count+=1
    return count
sosu(78)
