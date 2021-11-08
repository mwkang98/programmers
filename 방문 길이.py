def solution(dirs):
    temp=[]
    now=(0,0)
    for i in range(len(dirs)):
        if(dirs[i]=='U'):
            if(now[1]<5):
                now=(now[0],now[1]+1)
                temp.append(now)
        elif(dirs[i]=='D'):
            if(now[1]>-5):
                now=(now[0],now[1]-1)
                temp.append(now)
        elif(dirs[i]=='L'):
            if(now[0]>-5):
                now=(now[0]-1,now[1])
                temp.append(now)
        elif(dirs[i]=='R'):
            if(now[0]<5):
                now=(now[0]+1,now[1])
                temp.append(now)
    print(set(temp))
    
solution("ULURRDLLU")
