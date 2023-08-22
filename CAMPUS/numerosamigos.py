n1=int(input("Ingresa el num1: "))
n2=int(input("Ingresa el num2: "))
sum=sum2=0
for i in range(1,n1):
    if n1%i==0:
        sum+=i
for i in range(1,n2):
    if n1%i==0:
        sum2+=i  

if sum==n2 or sum2==n1:
    print("El numero",n1,"y el numero",n2,"son amigos")
else:
    print("NO SON AMIGOS")