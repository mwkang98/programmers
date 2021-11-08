import heapq
import re
def solution(operations):
    a=[]
    for i in operations:
        if(i[0])=='I':#첫 글자가 I면 원소 집어넣음
            number=re.sub('[A-Z]','',i)#정규식 통해 불필요한 글자 제거
            heapq.heappush(a,int(number))#INT로 바꿔주고 배열에 넣어줌
        else:#첫 글자가 D (제거) 일 경우
            if(not a):#배열이 비어있으면 무시
                continue 
            
            if('-' in i):#최솟값 제거 일 경우
                a.sort()
                a.pop(0)
            else: #최댓값 제거 일 경우
                a.sort()
                a.pop()
    if not a: #배열에 아무것도 없으면 
        return [0,0]
    else:
        return [max(a),min(a)]
print(solution(["I 16","D 1"]))