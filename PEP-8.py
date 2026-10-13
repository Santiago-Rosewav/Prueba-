
def parar():
    input("Presione <ENTER> para continuar")


def capturar_temperatura():
    try:
        temperatura = float(input("Por favor digite la temperatura: "))
        return temperatura
    except ValueError:
        print("Error: debe ingresar un número válido.")
        return None


def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_a_kelvin(celsius):
    return celsius + 273.15


def kelvin_a_fahrenheit(kelvin):    
    return (kelvin - 273.15) * 9 / 5 + 32


def kelvin_a_celsius(kelvin):
    return kelvin - 273.15


def fahrenheit_a_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    continuar = True
    temperatura = None

    while continuar:
        opcion = input(
            "\nSeleccione una opción:\n"
            "1 --> Capturar temperatura\n"
            "2 --> Celsius a Fahrenheit\n"
            "3 --> Celsius a Kelvin\n"
            "4 --> Kelvin a Fahrenheit\n"
            "5 --> Kelvin a Celsius\n"
            "6 --> Fahrenheit a Kelvin\n"
            "7 --> Fahrenheit a Celsius\n"
            "0 --> Salir\n"
            "Opción: "
        )

        if opcion == "1":
            temperatura = capturar_temperatura()

            if temperatura is not None:
                parar()

        elif opcion in ("2", "3", "4", "5", "6", "7"):
            if temperatura is None:
                print("Primero debe capturar una temperatura.")
                parar()
                continue

            if opcion == "2":
                resultado = celsius_a_fahrenheit(temperatura)
                print(f"{temperatura} °C = {resultado} °F")

            elif opcion == "3":
                resultado = celsius_a_kelvin(temperatura)
                print(f"{temperatura} °C = {resultado} K")

            elif opcion == "4":
                resultado = kelvin_a_fahrenheit(temperatura)
                print(f"{temperatura} K = {resultado} °F")

            elif opcion == "5":
                resultado = kelvin_a_celsius(temperatura)
                print(f"{temperatura} K = {resultado} °C")

            elif opcion == "6":
                resultado = fahrenheit_a_kelvin(temperatura)
                print(f"{temperatura} °F = {resultado} K")

            elif opcion == "7":
                resultado = fahrenheit_a_celsius(temperatura)
                print(f"{temperatura} °F = {resultado} °C")

            parar()

        elif opcion == "0":
            print("Hasta luego.")
            continuar = False

        else:
            print("Seleccione una opción válida.")
            parar()


if __name__ == "__main__":
    main()

#Hola esta es mi primera modificación y cambios que hago en Git y subire a GitHub se les quiere mucho
#Los quiero mucho