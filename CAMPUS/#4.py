p=int(input("Ingrese el num: "))
nme=nmay=p
for i in range(1, 10):
    p=int(input("Ingrese el num: "))
    if p>nmay:
        nmay=p
    if p<nme:
        nme=p

print("El numero mayor es:", nmay)
print("El numero menor es:", nme)