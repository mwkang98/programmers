from itertools import permutations
def sosu(num):
    for i in range(2,num):
        if(num%i==0):
            return 0
    return 1
def solution(nums):
    count=0
    temp=list(permutations(nums,3))
    for i in range(len(temp)):
        temp[i]=temp[i][0]+temp[i][1]+temp[i][2]
    temp=list(set(temp))
    print(temp)
    for i in range(len(temp)):
        if(sosu(temp[i])==1):
            count+=1
    answer=count
    return answer
print(solution([1,2,7,6,4]))
