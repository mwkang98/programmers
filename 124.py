def solution(n):
    answer = ""
    share=n
    remainder=0
    while(share!=0):
        share=share/3
        remainder=share%3
        if(remainder==0):
            answer='4'+answer
            share=share-1
        if(remainder==1):
            answer='1'+answer
        if(remainder==2):
            answer='0'+answer
    return answer

print("숫자입력:")
n=str(input())
a=solution(n)
print(a)
