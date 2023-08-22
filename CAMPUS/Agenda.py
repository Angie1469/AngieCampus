
Agenda = []

def Añadir_modificar():
    encontrado=False # Bandera para validar si el usuario se encontro o no 
    nombre = input("Ingrese el nombre:") # Se pide por teclado el nombre del usuario
    for usuario in Agenda: # Recorre la lista en donde esta los usuarios(diccionnario)
        if usuario['nombres'] == nombre: # Valida que el nombre ingresado este en el diccionario usuario
            print(usuario["telefonos"]) # Imprime el numero correspondiente al usuario ingresado
            encontrado=True # Bandera cambia porque se encontro el usuario
            break # Rompe el ciclo para que mantenga el usuario que se encontro
    mod = input("desea modificar el telefono?")
    if encontrado and mod == "si":  # Si el usuario fue encontrado y se quiere modificar
        nuevoTelefono = input("Ingrese el nuevo telefono:") # Se pide el nuevo telefono
        usuario["telefonos"] = nuevoTelefono # Se guarda el nuevo telefono
    elif encontrado==False: # Si el usuario no fue encontrado
        print("Usuario no encontrado") 
        añadir = input("desea añadirlo? ")
        if añadir == "si":
            nuevoTelefono = input("Ingrese el telefono: ")
        Agenda.append({"nombres": nombre, "telefonos": nuevoTelefono})
    else: # Si el usuario fue encontrado y no desean modificarlo
        return # No se hace nada

    input("Enter any key to continue...") # Para dar una pausa al codigo 


def Buscar():
    letra = input("Ingrese una letra")
    for usuario in Agenda:
        if  usuario["nombres"].startswith(letra):
            print(usuario)
    input("Enter any key to continue...") # Para dar una pausa al codigo 

def Borrar():
    nombre = input("Ingrese el nombre:")
    for usuario in Agenda:
        if usuario['nombres'] == nombre:
            break
    op = input("Desea eliminar el usuario? ")
    if op == "si":
        Agenda.remove(usuario)
        print("El usuario ha sido eliminado")
    else:
        return
            
    input()

def Listar():
    for usuario in Agenda:
        print(f"Nombre: {usuario['nombres']}\nTelefono: {usuario['telefonos']}")

    input()
""" for i in range(5):
    print(i) """

def AgregarUsuario():
    while True:
        nombre = input("Ingrese el nombre:")  
        telefono = input("Ingrese el telefono:")
        Validacion = input("Desea agregar otro usuario:")
    

        Usuario = {
            "nombres": nombre,
            "telefonos": telefono,
        }
        Agenda.append(Usuario)
        if Validacion != "si":
            break

def menu():
    seguir = True
    while seguir:
        print("Selecciona la opción que desee")
        print(" "*6 + "1) Agregar un usuario:\n")
        print(" "*6 + "2) Añadir y modificar:\n")
        print(" "*6 + "3) Buscar por letra \n")
        print(" "*6 + "4) Borrar\n")
        print(" "*6 + "5) Listar \n")  
        print(" "*6 + "6) Salir del programa\n")
        print()

        opcion = int(input('opcion -> '))

        if(opcion == 6):
            seguir = False
            return print('\nFin del programa\n')

        if(opcion < 1 or opcion > 6):
            return print('\nEl número debe ser entre 0 y 6\n')
    
    
        switch = {1:AgregarUsuario, 2: Añadir_modificar, 3: Buscar, 4: Borrar, 5: Listar}
        switch[opcion]()

menu()
