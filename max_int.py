n = 101  
su = 0  
for i in range(1, n):  
    for j in range(1, int(i)):  
        if (i % j == 0):  
            su = su + j  
    if (su > i):  
        print( i)  
    su = 0
    sd