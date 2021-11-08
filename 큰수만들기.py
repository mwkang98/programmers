number=int(input())
anumber=str(number)
k=int(input())
cp=0
value=0
temp=[]
ttemp=[]
ans=[]
while(1):
    if(len(ans)==(len(anumber)-k)):
         break
    for i in range(cp,k+1):
        temp.append(anumber[i])
    ttemp=temp.copy()
    temp.sort(reverse=True)
    value=temp[0]
    ans.append(value)
    for i in range(len(ttemp)):
       if(ttemp[i]==value):
                break
       cp=cp+1
    cp=cp+1
    temp.clear()
    ttemp.clear()
    k=k+1
    if(cp==k):
        k=k+1
print(ans)
    
    
    
       
        
        
        
    
