from itertools import permutations
number=str(input())
def issosu(t):
    b=0
    if(t<=1):
        b=1
    if(t!=2):
        for i in range(2,t):
            if(t%i==0):
                b=1
    return b
digit=1
total_count=0
temp=[]
total=[]
cp=list(permutations(number,digit))
while(1):
    if(digit==len(number)+1):
        break
    for i in range(0,len(cp)):
        cp[i]=''.join(cp[i])
        if(cp[i][0]!='0'): 
            if(issosu(int(cp[i]))==0):
                temp.append(cp[i]) 
    total_count+=len(set(temp))
    total.extend(set(temp))
    digit+=1
    cp=list(permutations(number,digit))
    temp.clear()
print(total)
print(total_count)
    
