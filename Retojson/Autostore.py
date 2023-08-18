import json
import os

def leerJson():
    with open("AutoShopping.json","r") as file:
        Data = json.load(file)
    return Data

def escribirJson(data):
    with open("AutoShopping.json","w") as file:
        json.dump(data,file,ensure_ascii=False,indent=4)



def validarFloat(numero):
    while True:
        try:
            n = float(input(numero))
            return n
        except ValueError:
            print("Error. Número real inválido. intente de nuevo.")
            input("Presione cualquier tecla para continuar...")
        except Exception as e:
            print("Ha sucedido un Error: ", e)
        
   

def validarString(nombre):
    while True:
        try:
            n = input(nombre)
            if n == None or n.strip() == "":
                print("Nombre inválido.")
                continue
            return n
        except Exception as e:
            print("Ha sucedido un Error: ", e)
            
   

def validarEntero(mensaje):
    while True:
        try:
            n = int(input(mensaje))
            r = 5 /n
            return n
        except ValueError:
            print("Error. Número entero inválido. intente de nuevo.")
            input("Presione cualquier tecla para continuar...")
        except ZeroDivisionError:
            print("Error. No se puede dividir por cero.")
            input("Presione cualquier tecla para continuar...")

def MostrarAutos():
    for n in Data['autostore']['autos']:
        print (n['marca']," -- ", n['linea']," -- ",n['modelo']," -- ",n['precio']," -- ",n['equipamiento'])

def RegistarNuevoAuto():
    consecionario = leerJson()
    print(consecionario)
    while True:#ingreso de datos por auto

        Marca  = validarString("Ingrese la marca del auto": ")
        Linea = validarString("Ingrese la referencia del auto: ")
        talla = validarString("Ingrese la talla:")
        precio = validarFloat("Ingrese el precio:")
        listaServicios = []
        while True: #ciclo para ingresar varios servicios
            servicio=validarString("Ingrese el servicio: ")
            if servicio in listaServicios: #hago la validacion de si el servicio ya esta en la listaServicios
                #si el servicio esta en la lista se ejecuta continue y se repite el ciclo 
                print("El servicio que ingreso ya se encuentra en lista")
                input()
                continue
            #si el servicio no esta en la lista , se agrega a la listaServicios
            listaServicios.append(servicio)
            if validarOtroCiclo("Desea agregar otro servicio? (si\no)"):
                continue
            break


        tienda["pets"].append({ #agrego el primer diccionario a la lista pets que esta a su vez en el diccionario maestro tienda
            "tipo": tipo,
            "raza": raza,
            "talla": talla,
            "precio": precio,
            "servicios":listaServicios, #listaServicios es una lista donde se agregan los servicios que el usuario desea
        })
        print(tienda)
        if validarOtroCiclo("Desea agregar otra mascota? (si/no)"):
            continue
        break

def MostrarAutoMarca():
    pass

def ActualizarDatosAuto():
    pass

def EliminarAuto():
    pass

def menu():
    seguir = True
    while seguir:
        print("Selecciona la opción que desee")
        print(" "*6 + "1) MostrarAutos")
        print(" "*6 + "2) RegistarNuevoAuto")
        print(" "*6 + "3) MostrarAutoMarca")
        print(" "*6 + "4) ActualizarDatosAuto")  #****
        print(" "*6 + "5) EliminarAuto\n")  #****
        print(" "*6 + "6) Salir del programa") 
        print()

        opcion = int(input('opcion -> '))

        if(opcion == 6):
            seguir = False
            return print('\nFin del programa\n')

        if(opcion < 1 or opcion > 6):
            return print('\nEl número debe ser entre 0 y 6\n')
        
       
        switch = { 1: MostrarAutos, 2: RegistarNuevoAuto, 3: MostrarAutoMarca, 
                  4: ActualizarDatosAuto, 5: EliminarAuto,}
        switch[opcion]()


Data = {}
Data = leerJson()
menu()