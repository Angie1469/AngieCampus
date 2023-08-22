vlrhora=20_000
N=int(input("Ingrese la cantidad de empleados"))
for i in range (1,N+1):
    canthora=int(input("Ingrese la cantidad de horas trabajadas:"))
    sueldobruto=vlrhora*canthora
    descEPS=sueldobruto-(sueldobruto*0.04)
    descPension=sueldobruto-(sueldobruto*0.04)
    sueldoneto=sueldobruto-(sueldobruto*0.08)

    print("El sueldo bruto es:",sueldobruto)
    print("El sueldo neto es:",sueldoneto)
    print("Descuento de la EPS es:",descEPS)
    print("Descuento de la pension:",descPension)



