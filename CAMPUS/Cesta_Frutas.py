# nombreDiccionario[llave] = valor
Lista = []
CestaCompra = {}

while True:
    Articulo = input("Ingrese el articulo: ")
    Precio = float(input("Ingrese el precio del articulo: "))
    Validacion = input("Desea agregar otro articulo:")
    CestaCompra[Articulo]= Precio
    if Validacion == "si":
        continue
    else:
        break


#Lista.append(CestaCompra)
    

  

print (CestaCompra)
