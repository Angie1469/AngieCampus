notas = []
suma=0
for i in range(1,6):
    
    nota = float(input(f"Ingrese la {i}  nota (0-10): "))
    notas.append(nota)
    suma+=nota

NotaBaja=min(notas)
NotaAlta=max(notas)

print("las notas son:",notas,"promedio:",round((suma/5),2),"nota mas baja:",NotaBaja,"nota mas alta:",NotaAlta)
    
