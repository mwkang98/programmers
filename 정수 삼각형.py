answer=[]

def add(length,idx,total,triangle):
    if(length==(len(triangle)-1)):
        global answer
        answer.append(total)
        return 
    else:
        left=triangle[length+1][idx]
        right=triangle[length+1][idx+1]
        add(length+1,idx,total+left,triangle) #left
        add(length+1,idx+1,total+right,triangle) #right
        
def solution(triangle):
    add(0,0,triangle[0][0],triangle)
    global answer
    return max(answer)
    
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
    