nem=int(input("Ingrese el número de empleados: "))
vh=20000

t_s_bruto=t_eps=t_pension=t_s_neto=s_n_max=0
pp_s_n_max=pp_s_n_min=""
s_n_min = float("inf")


for i in range(nem):
    pp=input(f"Ingrese el nombre del empleado {i+1}: ")
    h_t= float(input(f"Ingrese las horas trabajadas por {pp}: "))

    s_bruto=vh*h_t
    d_eps=s_bruto*0.04
    d_pension=s_bruto*0.04
    s_neto=s_bruto-d_eps-d_pension

    t_s_bruto+=s_bruto
    t_eps+=d_eps
    t_pension+=d_pension
    t_s_neto+=s_neto

    if s_neto>s_n_max:
        s_n_max=s_neto
        pp_s_n_max=pp

    if s_neto<s_n_min:
        s_n_min=s_neto
        pp_s_n_min=pp

    print(f"Empleado: {pp}")
    print(f"Salario bruto: ${s_bruto:.2f}")
    print(f"Descuento EPS: ${d_eps:.2f}")
    print(f"Descuento Pensión: ${d_pension:.2f}")
    print(f"Salario neto: ${s_neto:.2f}")
    print()

prome_s_bruto=t_s_bruto/nem
prome_s_neto=t_s_neto/nem

print("Estadísticas:")
print(f"Total salario bruto: ${t_s_bruto:.2f}")
print(f"Total EPS: ${t_eps:.2f}")
print(f"Total Pensión: ${t_pension:.2f}")
print(f"Total salario neto: ${t_s_neto:.2f}")
print(f"Empleado con mayor salario neto: {pp_s_n_max} - ${s_n_max:.2f}")
print(f"Empleado con menor salario neto: {pp_s_n_min} - ${s_n_min:.2f}")
print(f"Promedio de salarios brutos: ${prome_s_bruto:.2f}")
print(f"Promedio de salarios netos: ${prome_s_neto:.2f}")