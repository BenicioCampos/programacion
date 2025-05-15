print("bienvenido al calculador de gastos de viajes")

total_gastado=int(input("ingrese el total gastado en su viaje:"))
numero_dias=int(input("ingrese los dias que estuvo de viaje:"))
presupuesto=int(input("ingrese su presupuesto de viaje"))

def calcular_gasto_promedio(total_gastado, numero_dias):
    gasto_promedio = total_gastado/numero_dias
    return gasto_promedio

gasto_promedio_gg=calcular_gasto_promedio(total_gastado, numero_dias)
print("su gasto promedio por dia es:")
print(gasto_promedio_gg)

def calcular_balance(presupuesto, gasto_promedio):
    presupuesto_dias = presupuesto/numero_dias
    restante = presupuesto_dias-gasto_promedio
    return restante
print("su balance es:")
print(calcular_balance(presupuesto, gasto_promedio_gg))