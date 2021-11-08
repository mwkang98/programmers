name=str(input())
name_count=len(name)
totalcount=[]
total=0
for k in range (len(name)):
    if(ord(name[k])<=ord('M')):
       totalcount.append((ord(name[k])-ord('A'))+1)  
    else:
       totalcount.append((91-ord(name[k]))
