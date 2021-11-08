def adder(t,n):
    k=0
    for i in range(t,n):
        if(k>n):
            return 0
        if(k==n):
            return 1 
        if(k<n):
            k=k+i
            
        
n=int(input())
count=0
t=1
temp=[]
k=0
for i in range(t,n):
    k=adder(i,n)
    if(k==1):
        count=count+1
        temp.append(i)
print(temp)
print(count+1)
