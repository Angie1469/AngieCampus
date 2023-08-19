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

def leerJson():
    with open("PaísCiudad.json","r") as file:
        Data = json.load(file)
    return Data

def escribirJson(data):
    with open("PaísCiudad","w") as file:
        json.dump(data,file,ensure_ascii=False,indent=4)

def ListaCiudades():
    for n in Data['Departamentos']:
        print (n['id']," -- ", n['nomDepartamento']," -- ",n['talla']," -- ",n['precio']," -- ",n['servicios'])
        print(Data)

    

def AgregarNuevaCiudad():
    pass

def EliminarCiudad():
    pass

def CrearDepartamento():
    pass

def EliminarDepartamento():
    pass

def ListaDepartamentos():
    for n in Data['Departamentos']:
        print(n['idDep']," -- ", n['nomDepartamento'])
    input()




def menu():
    seguir = True
    while seguir:
        print("Selecciona la opción que desee\n")
        print(" "*6 + "1) Lista de ciudades\n")
        print(" "*6 + "2) Agregar una ciudad\n")
        print(" "*6 + "3) Eliminar una ciudad\n")
        print(" "*6 + "4) Crear un departamento\n")  #****
        print(" "*6 + "5) Eliminar un deparmento\n")  #****
        print(" "*6 + "6) Lista de departamentos\n") 
        print(" "*6 + "7) Salir del programa\n") 


        print()

        opcion = int(input('opcion -> '))

        if(opcion == 7):
            seguir = False
            return print('\nFin del programa\n')

        if(opcion < 1 or opcion > 7):
            return print('\nEl número debe ser entre 0 y 7\n')
        
       
        switch = { 1: ListaCiudades, 2: AgregarNuevaCiudad, 3: EliminarCiudad, 
                  4: CrearDepartamento, 5: EliminarDepartamento, 6:ListaDepartamentos}
        switch[opcion]()


Data = {}
Data = leerJson()
menu()