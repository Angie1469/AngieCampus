Reprobadas = []
Asignaturas = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
for i in Asignaturas:
    notas = float(input(f"Ingrese la nota de {i}"))

    if notas < 3.0:
        Reprobadas.append(i)

print(Reprobadas)
