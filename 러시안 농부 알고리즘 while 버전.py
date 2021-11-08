def russian_mult(m,n):
    if n > 0:
        a = 0
        while n > 1:
            if n % 2 == 1:
                a = a + m
            m = m +m
            n = n // 2
        return a+m
    else:
        return 0
        