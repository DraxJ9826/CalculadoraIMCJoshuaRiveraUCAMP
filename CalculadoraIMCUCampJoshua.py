#UCamp Joshua Rivera Python
#Criterios de evaluación: https://apps.utel.edu.mx/recursos/files/r161r/w26559w/4M%20Bootcamp/Fundamentos%20de%20Python/M1ProyectoFundamentosdePython.pdf

import re
# ::::::::::::: Funciones :::::::::::::
def pedirNumero(mensaje, tipo=float, min_val=None, max_val=None):
    """Pide un número válido (int o float) y opcionalmente verifica rango."""
    while True:
        dato = input(mensaje).strip()
        if dato:
            try:
                numero = tipo(dato)
                if (min_val is not None and numero < min_val) or (max_val is not None and numero > max_val):
                    print(f"⚠️ El valor debe estar entre {min_val} y {max_val}.")
                else:
                    return numero
            except ValueError:
                print("⚠️ Debes introducir un número válido.")
        else:
            print("⚠️ Este campo no puede estar vacío.")

def pedirNombre(mensaje, max_length=100):
    """Pide un nombre o apellido válido (solo letras y espacios)."""
    patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$"
    while True:
        dato = input(mensaje).strip()
        if not dato:
            print("⚠️ Este campo no puede estar vacío.")
        elif len(dato) > max_length:
            print(f"⚠️ El texto no puede tener más de {max_length} caracteres.")
        elif not re.match(patron, dato):
            print("⚠️ Solo se permiten letras y espacios en este campo.")
        else:
            return dato

# ::::::::::::: Programa Principal :::::::::::::
print("Bienvenido a la Calculadora de IMC de Joshua Rivera")
# Pedir la cantidad de personas
cantidad = pedirNumero("¿Para cuántas personas deseas calcular el IMC? ", tipo=int, min_val=1)
# Array para guardar datos de cada persona
personasACalcular = []
# Bucle para pedir datos de cada persona
for i in range(cantidad):
    print(f"\nOk, vamos con la persona {i + 1}")
    nombre = pedirNombre("Nombre(s): ")
    apellidoPaterno = pedirNombre("Apellido Paterno: ")
    apellidoMaterno = pedirNombre("Apellido Materno: ")
    edad = pedirNumero("Edad: ", tipo=int, min_val=1)
    peso = pedirNumero("Peso (kg): ", min_val=1)
    estatura = pedirNumero("Estatura (m, ejemplo 1.75): ", min_val=0.5, max_val=2.5)
    imc = peso / (estatura ** 2)
    # Guardar datos en el array
    persona = {
        "nombre": nombre,
        "apellidoPaterno": apellidoPaterno,
        "apellidoMaterno": apellidoMaterno,
        "edad": edad,
        "peso": peso,
        "estatura": estatura,
        "imc": imc
    }
    personasACalcular.append(persona)

# ::::::::::::: Mostrar resultados :::::::::::::
print("\n=== Resultados del cálculo de IMC ===")
for persona in personasACalcular:
    nombreCompleto = f"{persona['nombre']} {persona['apellidoPaterno']} {persona['apellidoMaterno']}"
    edad = persona['edad']
    peso = persona['peso']
    estatura = persona['estatura']
    imc = persona['imc']

    # Clasificación del IMC
    if imc < 18.5:
        categoria = "Bajo peso"
    elif 18.5 <= imc < 25:
        categoria = "Peso normal"
    elif 25 <= imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"

    # Rango de peso recomendado
    imc_min = 18.5
    imc_max = 24.9
    peso_min = imc_min * (estatura ** 2)
    peso_max = imc_max * (estatura ** 2)

    print(f"\nNombre: {nombreCompleto}")
    print(f"Edad: {edad} años")
    print(f"Peso actual: {peso} kg")
    print(f"Estatura: {estatura} m")
    print(f"IMC: {imc:.2f} → {categoria}")
    print(f"Peso recomendado según IMC normal (18.5-24.9): {peso_min:.1f} kg - {peso_max:.1f} kg")

print("\n¡Gracias por usar la Calculadora de IMC! 👋")
