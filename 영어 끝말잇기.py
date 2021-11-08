def sameword(n,words):
       for i in range(len(words)):
            for j in range(len(words)):
                if(i==j):
                    continue
                if(words[i]==words[j]):
                    return j 
       return False 
def wrongword(n,words):
    for i in range(len(words)-1):
        if(words[i][len(words[i])-1]!=words[i+1][0]):
            return i+1
    return False

def solution(n, words):
    if(sameword(n,words)==False and wrongword(n,words)==False):
        answer=[0,0]
        return answer
    else:
        a=[]
        person=1
        t=1
        k=0
        while(1):
            a.append([person,t])
            k=k+1
            if(k==len(words)):
                break
            person=person+1
            if(person==n+1):
                person=1
                t=t+1
        print(a)
        if(sameword(n,words)!=False):
            return a[sameword(n,words)]
        if(wrongword(n,words)!=False):
            return a[wrongword(n,words)] 
        
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])) 
