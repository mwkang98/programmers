answer=0
def dfs(number):
    if(number==0):
        global answer
        answer+=1
        return 
    elif(number<0):
        return
    dfs(number-1)
    dfs(number-2)
    
def solution(n):
    dfs(n)
    return answer%1234567
print(solution(4))