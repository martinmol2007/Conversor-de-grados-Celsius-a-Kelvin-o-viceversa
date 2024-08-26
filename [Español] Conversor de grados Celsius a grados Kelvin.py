print("Bienvenido al conversor de grados Celsius a Kelvin o viceversa")

def convertidor_temperatura():
    print("¿Qué conversión de las siguientes opciones desea hacer?")
    print("1: Pasar de Celsius a Kelvin")
    print("2: Pasar de Kelvin a Celsius")

    opcion = input("Ingrese una de las dos opciones (1 o 2): ")

    if opcion == "1":
        celsius = float(input("Introduce el número de grados Celsius que deseas convertir a grados Kelvin: "))
        kelvin = celsius + 273.15
        print(str(celsius) + " °C son " + str(kelvin) + " K")
    elif opcion == "2":
        kelvin = float(input("Introduce el número de grados Kelvin que deseas transformar a grados Celsius: "))
        celsius = kelvin - 273.15
        print(str(kelvin) + " K son " + str(celsius) + " °C")
    else:
        print("Opción no válida. Vuelve a intentarlo")

convertidor_temperatura()
