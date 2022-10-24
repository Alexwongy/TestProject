def fibIter(n):
    a = 1
    b = 1
    c = 1
    while n > 2:
        c = a + b
        a = b
        b = c
        n -= 1
    return c

fibIter(12)
