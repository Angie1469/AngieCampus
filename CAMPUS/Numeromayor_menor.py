numeros=[]
mayor=0
menor=0

for i in range(0,10):
     numero = float(input("Introduce el número #{}: ".format(i + 1)))
     numeros.append(numero)
     mayor = numeros[0]
     for numero in numeros:
        if numero > mayor:
            mayor = numero
            menor =numero
print("Mayor:", mayor)

numeros.append(numero)
menor = numeros[0]
for j in range(0,10):
    for numero in numeros:
        if numero < menor:
            menor = numero
print("Menor:", menor)

