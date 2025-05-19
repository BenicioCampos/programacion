ptint("bienvenido al programa de control de consumo de agua")
def calcular_objetivo_ml(peso_kg, nivel_actividad):
    base_ml = 35 * peso_kg
    if nivel_actividad == "bajo":
        ajuste = -0.1
    elif nivel_actividad == "alto":
        ajuste = 0.1
    else:
        ajuste = 0
    objetivo_ml = base_ml * (1 + ajuste)
    return objetivo_ml

def estado_hidratacion(consumo_ml, objetivo_ml):
    porcentaje = (consumo_ml / objetivo_ml) * 100
    if porcentaje >= 100:
        if porcentaje == 100:
            return "Has alcanzado tu objetivo"
        else:
            return f"Has excedido tu objetivo en {porcentaje - 100:.2f}%"
    else:
        return f"Te falta un {100 - porcentaje:.2f}% para llegar"

def main():
    peso_kg = float(input("Ingrese su peso en kg: "))
    nivel_actividad = input("Ingrese su nivel de actividad (bajo, medio o alto): ").lower()
    consumo_ml = float(input("Ingrese la cantidad de agua que ha consumido hoy en ml: "))

    objetivo_ml = calcular_objetivo_ml(peso_kg, nivel_actividad)
    mensaje_estado = estado_hidratacion(consumo_ml, objetivo_ml)

    print(f"Objetivo diario en ml: {objetivo_ml:.2f}")
    print(mensaje_estado)

if __name__ == "__main__":
    main()