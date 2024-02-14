def Divby4and3(n):
    for i in range(12,n):
        if i % 12 == 0:
            yield i 



DivBy3and4 = (i for i in range(12,100) if i % 12==0)

