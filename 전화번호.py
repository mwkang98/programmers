def numcheck(a,b):
    if(len(a)>len(b)):
        numcheck(b,a)
        return
    for i in range(0,len(a)):
        if(a[i]!=b[i]):
            return 
    return 1
pb=["12","923","54577","42"]
t=len(pb)
a=0
for i in range(0,t):
    for j in range(0,t):
        if(pb[i]==pb[j]):
            continue
        if(numcheck(pb[i],pb[j])==1):
            a=1
if(a==1):
    print("False")
else:
    print("True")
