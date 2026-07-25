i = 1

def NumerosPerfectos(i):
    while i < 500:
        n = 1
        Division = 0
        while n < i:
            if i % n == 0:
                Division = n + Division
            n += 1
        if Division == i:
            print(i)
        i += 1

NumerosPerfectos(i)