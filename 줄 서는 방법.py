from math import factorial
def solution(n,k):
    answer=[]
    number=[i for i in range(1,n+1)]
    while n!=0:
        answer.append(number.pop((k-1)//factorial(n-1)))
        n,k=n-1,k%factorial(n-1)
    return answer
print(solution(3,5))