print("Hello, World")

def prime(n):
    p = True
    for i in range(2,n):
        if (n%i == 0):
            p = False
    return p

for j in range(2,250):
    if prime(j):
        print (j)