import json
from os import system


with open("./biblioteca.json", "r") as archivo:
    diccionario = json.load(archivo)

#Funcion para menu
def menu_principal ():
    print("-------------- Menu --------------")
    print("\n1.Mostrar en pantalla todos los libros\n2.Crear Nuevo libro con la posibilidad de múltiples autores por Libro\n3.Mostrar los datos de un libro consultado por título\n4.Actualizar los datos de un libro consultado por título\n5.Eliminar un Libro de la biblioteca\n0.SALIR\n")
    
def mostrar_libros (diccionario):
    print("TITULO \t\t\t AUTOR\n\n")
    for i in diccionario["bookstore"]["book"]:
        print(i["title"]["__text"],"\t",i["author"])

def mostrar_libro_consultado (diccionario):
    titulo = input("Ingrese el nombre del libro que desea buscar: \n")
    for i in diccionario["bookstore"]["book"]:
        if i["title"]["__text"] == titulo:
            print("TITULO \t\t\t AÑO \t\t\t CATEGORIA \t\t\t AUTOR\n\n")
            for i in diccionario["bookstore"]["book"]["title"][titulo]:
                print(i["title"]["__text"],"\t", i["year"],"\t",i["_category"],"\t",i["author"])
    


def crear_libro (diccionario):
    
    lista = []
    titulo = input("Ingrese el título del nuevo libro:\n")
    contadorautor = int(input("Cuantos autores tiene el libro"))
    for i in range(contadorautor) :
        autor = input("Ingrese un autor del nuevo libro:\n")
        lista.append(autor)
    año = input("Ingrese el año del nuevo libro:\n")
    categoria = input("Ingrese la categoria del nuevo libro:\n")
    diccionario["bookstore"]["book"].append({"title":{"__text": titulo}, "author" : lista, "year" : año, "_category" : categoria})
    with open("./biblioteca.json", "w") as archivo:
        json.dump(diccionario, archivo)
    print("Libro creado con éxito")

def mostrar_libro (diccionario):
    titulo = input("Ingrese el nombre del libro que desea buscar: \n")
    for i in diccionario["bookstore"]["book"]:
        if i["title"]["__text"] == titulo:
            print(i["title"]["__text"])
            

def actualizar_libro (diccionario):
    mostrar_libro(diccionario)
    titulo = input("Ingrese el nombre del libro que desea buscar: \n")
    for i in diccionario["bookstore"]["book"]:
        if i["title"]["__text"] == titulo:
            cambio = int(input("Que desea editar del libro: \n1.Titulo\n2.Autor\n3.Año\n4.Categoria\n0.Ninguna\n"))
            if cambio == 1:
                titulo = input("Ingrese el nuevo título del libro:\n")
                diccionario["bookstore"]["book"][i]["title"] = {"__text": titulo}
            elif cambio == 2:
                autor = input("Ingrese el nuevo autor del libro:\n")
                diccionario["bookstore"]["book"][i]["title"] = {"author": autor}
            elif cambio == 3:
                año = input("Ingrese el nuevo año del libro:\n")
                diccionario["bookstore"]["book"][i]["title"] = {"year": año}
            elif cambio == 4:
                categoria = input("Ingrese la nueva categoria del libro:\n")
                diccionario["bookstore"]["book"][i]["title"] = {"category": categoria}
            elif cambio == 0:
                print("No se edito ningun elemento")
            
            
            
            
def eliminar_libro(diccionario):
    mostrar_libros(diccionario)
    titulo = input("Ingrese el nombre del libro que desea eliminar: \n")
    for i in diccionario["bookstore"]["book"]:
        if i["title"]["__text"] == titulo:
            diccionario["bookstore"]["book"].remove(i)
    with open("./biblioteca.json", "w") as archivo:
        json.dump(diccionario, archivo)



flag  = True

while  flag:
    menu_principal()
    opcion = int(input("\n"))
    if opcion == 1:
        mostrar_libros(diccionario)
    elif opcion == 2:
        crear_libro(diccionario)
    elif opcion == 3:
        mostrar_libro_consultado(diccionario)
    elif opcion == 4:
        actualizar_libro(diccionario)
    elif opcion == 5:
        eliminar_libro(diccionario)
    elif opcion == 0:
        flag = False
    else:
        print("Opcion no valida")
    
print("Fin del proceso")