def quicksort(xs):
    if len(xs) > 1:
        pivot=xs[0]
        left,right=partition(pivot,xs[1: ])
        return quicksort(left) + [pivot] + quicksort(right)

def partition(pivot,xs):
    if xs!=[]:
        left,right=partition(pivot,xs[1: ])
        if xs[0]<=pivot:    
            left.append(xs[0])
        else:
            right.append(xs[0]) 
        return left,right
    else:
        return [],[]
print(quicksort([3,7,8,5,2,1,9,6,4]))
