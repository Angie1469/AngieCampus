#datos de entrada: N usuarios, pedimos : codigo, nombre estado (V=vigente o S=suspendido
#estrato: (1,2,3,4,5 o 6) , consumo del mes (cm3)
#proceso: Valor a pagar = tarifa + valor consumo
#output: nombre de usuario, el valor de la tarifa basica, el valor del consumo y el valor a pagar por concepto de agua


empl = int(input("Ingrese la cantidad de empleados:"))
tarBas=0
vlrtotal = 0
for i in range (1,empl+1):
    print("\nInformacion del usuario #", i)
    est = input("Ingrese el estado del usuario (V=vigente o S=suspendido)")
    if est == "V" or est == "v":
        cod = input("Ingrese el codigo del empleado:")
        nom = input("Ingrese el nombre del empleado:")
        est = int(input("Ingrese el estrato (1,2,3,4, o 5)?"))
        cons = int( input("Ingrese el consumo del mes (cm3):"))
    elif est == 1:
        tarBas = 10000
    elif est == 2:
        tarBas = 20000
    elif est == 3:
        tarBas = 30000
    elif est == 4:
        tarBas = 45000
    elif est == 5:
        tarBas = 60000
    elif est == 6:
        tarBas = 70000

    valorCons = cons * 200
    vlrpagar = tarBas + valorCons
    vlrtotal += vlrpagar

    print("\n\t", "-" * 30)
    print("\tNombre de usuario:", nom)
    print(f"valor tarifa basica: ${tarBas:,.0f}")
    print(f"valor de consumo del mes:${valorCons:,.0f}")
    print(f"valor a pagar servicio de agua: ${vlrpagar:,.0f}")

print("\n", "=." * 20)
print(f"El valor total de los servicio de todos los usarios es ${vlrtotal:,.0f}")
    


    