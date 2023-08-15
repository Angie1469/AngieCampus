import json

ventas = {"vendedores":[]}

with open("vendedores.txt","r") as file_csv:
    lineas = file_csv.readlines()
#print(lineas)

for i in lineas[1:]:
    res=i.replace("\n","").split(",")
    ventas["vendedores"].append({"apellido":res[0],"id":res[1],"ventas":res[2:]})
print(ventas)

with open("ventas.json","w") as newfile:
    json.dump(ventas, newfile,indent=4)