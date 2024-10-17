def calcular_bonificacion(cargo_empleado, nivel_desempenio):
    bonificacion = 0.0
    if cargo_empleado == "directivo":
        if nivel_desempenio == "alto":
            bonificacion = 0.20
        elif nivel_desempenio == "medio":
            bonificacion = 0.10

    elif cargo_empleado == "operativo":

        if nivel_desempenio == "alto":
            bonificacion = 0.15
        elif nivel_desempenio == "medio":
            bonificacion = 0.05
    else:
        print("Cargo desconocido")

    return bonificacion


def calcular_total(salario_base_mensual, bonificacion):
    monto_bonificacion = int(salario_base_mensual * bonificacion)
    total_a_recibir = int(salario_base_mensual + monto_bonificacion)
    return [monto_bonificacion, total_a_recibir]


def resumen_pago(cargo_empleado, nivel_desempenio, salario_base_mensual):
    bonificacion = calcular_bonificacion(cargo_empleado, nivel_desempenio)
    calculo_total = calcular_total(salario_base_mensual, bonificacion)
    return (f"-----Resumen del Pago-----\n"
            f"Cargo: {cargo_empleado.capitalize()}\n"
            f"Nivel de Desempeño: {nivel_desempenio.capitalize()}\n"
            f"Salario Base: ${salario_base_mensual}\n"
            f"Bonificación: ${calculo_total[0]}\n"
            f"Total a Recibir: ${calculo_total[1]}\n"
            f"____________________________")


def app():
    salario_base_mensual = int(input("Salario base mensual $: "))
    cargo_empleado = input("Cargo empleado: ").lower()
    nivel_desempenio = input("Nivel de desempeño: ").lower()
    print(resumen_pago(cargo_empleado, nivel_desempenio, salario_base_mensual))


app()
