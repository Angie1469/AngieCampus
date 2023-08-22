def ValidarFruta():
    try:
        nombre =input("Ingrese el nombre de la fruta: ")
        if nombre in frutas:
            return nombre
        else:
            print("La fruta no esta disponible")
            return ValidarFruta()
    except:
        return ValidarFruta()
    
frutas ={
    "Platano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70,
}

fruta = ValidarFruta()
kilos = float(input("Ingrese la cantidad de kilos que desea:"))
precio = frutas[fruta]*kilos

print(precio)

