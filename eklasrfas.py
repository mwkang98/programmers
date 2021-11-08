import sys
sys.setrecursionlimit(10**6)
print("배열 입력")
array = list(map(int, input().split()))
array=sorted(array)
temparray=list(array)
key=array[len(array)-1]
def add(arr,key,k):
	while(1):
		arr[k]=arr[k]+temparray[k]
		if(arr[k]>key):
			key=key+temparray[len(array)-1]
			add(arr,key,0)
		if(arr[k]==key):
			k=k+1
			if(k==len(array)-1):
				break
	return key
k=0
answer=add(array,key,k)
print("답은:",answer,"입니다")


