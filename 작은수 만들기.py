def solution(A,B):
    count=0
    answer=0
    for i in range(len(A)):
        count=min(A)*max(B)+count
        q=A.pop(A.index(min(A)))
        w=B.pop(B.index(max(B)))
        print(A,q)
        print(B,w)
        print(count)
    answer=count
    return answer
print(solution([1,4,2],[5,4,4]))
