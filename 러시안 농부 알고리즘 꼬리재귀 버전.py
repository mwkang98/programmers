def russian_mult(m,n):
    def loop(m,n,a):
        if n>1:
            if(n%2==1):
                return loop(m*2, n//2, m+a)
            else:
                return loop(m*2,n//2, a)
        else:
            return m+a             
    if n>0:
        return loop(m,n,0)
    else:
        return 0
print(russian_mult(57,86))