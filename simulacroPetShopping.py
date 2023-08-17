"""
Elabore un programa Python para gestionar el CRUD del archivo de datos PetShopping.json con las siguientes funcionalidades:

    
Mostrar en pantalla todas las mascotas a la venta visualizando: Tipo, Raza, Precio y Servicios

    
Crear Nueva mascota con la posibilidad de múltiples ítems de Servicio

    
Mostrar los datos de Mascotas por Tipo elegido visualizando: Raza, Precio y Servicios

    
Actualizar los datos de una mascota consultada por índice (Mostrar el listado total y elegir por     índice)

    
Eliminar una mascota de la tienda (Mostrar el listado total y elegir por índice)
"""


import json
import os



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
        
def listaIndice():
    cont = 1
    for n in Data['pets']:
        print (cont,n['tipo']," -- ", n['raza']," -- ",n['talla']," -- ",n['precio']," -- ",n['servicios']) 
        cont +=1


def MostrarTodasMascotas():
#1    os.system('clear')
    for n in Data['pets']:
        print (n['tipo']," -- ", n['raza']," -- ",n['talla']," -- ",n['precio']," -- ",n['servicios'])

    
def validarOtroCiclo(msg):
    while True:
        try:
            a=input(msg)
            if a.lower() == "si":
                return True
            if a.lower() == "no":
                return False
            print("input error")
        except ValueError:
            print("input error")
            continue
            
def leerJson():
    with open("PetShopping.json","r") as file:
        data = json.load(file)
    return data

def escribirJson(data):
    with open("PetShopping.json","w") as file:
        json.dump(data,file,indent=4)

def CrearNuevaMascota():
    os.system('clear')
    tienda = leerJson()
    print(tienda)
    while True:#ingreso de datos por mascota

        tipo  = validarString("Digite el tipo de mascota: ")
        raza = validarString("Ingrese la raza: ")
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
    

def MostrarMascotaPorTipo():
    tipo = validarString("Escoja el tipo de mascota:  ")
    for i in Data['pets']:
        if i['tipo'] == tipo:
            print(i)
     
    

def ActualizarDatosMascota():
    dato = validarString("Que dato desea actualizar? ")
    listaIndice()
    opcion = validarEntero("que mascota desea actualizar?")
    if dato == 'raza':
        newdato = validarString("ingrese la neva raza")
        Data['pets'][opcion-1]['raza'] = newdato
    elif dato == 'talla':
        newdato = validarString("ingrese la neva talla")
        Data['pets'][opcion-1]['talla'] = newdato
    elif dato == 'servicios':
        newdato = validarString("ingrese la neva servicios")
        Data['pets'][opcion-1]['servicios'] = newdato
    elif dato == 'precio':
        newdato = validarFloat("Ingrese el nuevo precio")
        Data['pets'][opcion-1]['precio'] = newdato
    else:
        print("Se cancela la operacion")


def EliminarMascota():
    eliminar = validarString("Que mascota desea eliminar?")

def menu():
    seguir = True
    while seguir:
        print("Selecciona la opción que desee")
        print(" "*6 + "1) Mostar en pantalla todas las mascotas")
        print(" "*6 + "2) Crear una nueva mascota")
        print(" "*6 + "3) Mostrar mascota por tipo")
        print(" "*6 + "4) Actualizar los datos de una mascota")  #****
        print(" "*6 + "5) Eliminar una mascota\n")  #****
        print(" "*6 + "6) Salir del programa") 
        print()

        opcion = int(input('opcion -> '))

        if(opcion == 6):
            seguir = False
            return print('\nFin del programa\n')

        if(opcion < 1 or opcion > 6):
            return print('\nEl número debe ser entre 0 y 6\n')
        
       
        switch = { 1: MostrarTodasMascotas, 2: CrearNuevaMascota, 3: MostrarMascotaPorTipo, 
                  4: ActualizarDatosMascota, 5: EliminarMascota,}
        switch[opcion]()


Data = {}
Data = leerJson()
menu()