n=int(input("Ingrese el valor de n:"))
for i in range (1,n):
    p=int(input("Ingrese el valor de P:"))
    q=int(input("Ingrese el valor de Q:"))
    Exp=((p**3) + (q**4) - 2*(p**2))

    if (Exp<680):
        print(Exp)
        print(p,q, end=",")
