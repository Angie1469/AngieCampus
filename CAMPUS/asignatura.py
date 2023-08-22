AsignaturasReprobadas = []
Asignaturas = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
notaMat = float(input("Ingrese la nota de matematicas: "))
notaFis = float(input("Ingrese la nota de Fisica: "))
notaQui = float(input("Ingrese la nota de quimica: "))
notaHist = float(input("Ingrese la nota de Historia: "))
notaLeng = float(input("Ingrese la nota de Lengua: "))

if notaMat <3.0:
    AsignaturasReprobadas.append("Matematicas")
if notaFis <3.0:
    AsignaturasReprobadas.append("Fisica")
if notaQui < 3.0:
    AsignaturasReprobadas.append("Quimica")
if notaHist < 3.0:
    AsignaturasReprobadas.append("Historia")
if notaLeng < 3.0:
    AsignaturasReprobadas.append("Lenguas")

print (AsignaturasReprobadas)

