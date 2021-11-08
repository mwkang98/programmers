name=str(input())
name_count=len(name)
totalcount=[]
total=0
def fcheck(name):
    count=0
    rcount=0
    for k in range(1,len(name)):
        count=count+1
        if(name[k]!='A'):
            rcount=rcount+count
            count=0
    return rcount
def bcheck(name):
    count=0
    rcount=0
    for k in range(len(name)-1,0):
        count=count+1
        if(name[k]!='A'):
            rcount=rcount+count
            count=0
        return rcount
def dbcheck(name):
    count=0
    rcount=0
    for k in range(1,len(name)/2):
        count=count+1
        if(name[k]!='A'):
            checkpoint=k
            rcount=rcount+count
            count=0
    for k in range(checkpoint,0):
        rcount=rcount+1
    for k in range(len(name)-1,len(name)/2):
        count=count+1
        if(name[k]!='A'):
            rcount=rcount+count
            count=0
    return rcount
for k in range (len(name)):
    if(ord(name[k])<=ord('M')):
       totalcount.append((ord(name[k])-ord('A')))  
    else:
       totalcount.append((91-ord(name[k])))

if 
