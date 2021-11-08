def solution(N, number):

    total_array=[[] for t in range(9)]

    if(N==number):
        return 1

    else:
        for i in range(1,9):
            total_array[i].append(int(str(N)*i)) 
            for j in range(1,i):
                for k in range(len(total_array[j])):      
                    for q in range(len(total_array[i-j])):
                        total_array[i].append(total_array[j][k]+total_array[i-j][q])
                        total_array[i].append(total_array[j][k]-total_array[i-j][q])
                        total_array[i].append(total_array[j][k]*total_array[i-j][q])
                        if total_array[i-j][q]!=0:
                            total_array[i].append(total_array[j][k]//total_array[i-j][q])
            print(total_array)
            if(number in total_array[i]):
                return i
        
        return -1
print(solution(2,11))