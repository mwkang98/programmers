def solution(people, limit):
    print(people)
    count=0
    i=0
    go=0
    while(1):
        go=0
        if(len(people)==1):
                count+=1
                people.pop(0)
                print(people)
                print(count)
                break
        for j in range(1,len(people)):
            if(people[0]+people[j]<=limit):
                    people.pop(j)
                    people.pop(0)
                    print(people)
                    count+=1
                    print(count)
                    go=1
                    break
        if(go==0):
            people.pop(0) 
            count+=1
            print(count)
            print(people)
    answer=count
    return answer
solution([70,50,80,50],100)
