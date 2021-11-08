def solution(s):
    answer = True
    return answer
def get(s):
       stack=0
       for i in range(len(s)):
          if(s[i]=='('):
               stack+=1
          if(s[i]==')'):
                stack-=1
          if(stack<0):
              return False
       if(stack!=0):
              return False
       else:
              return True
s=str(input())
print(get(s))
