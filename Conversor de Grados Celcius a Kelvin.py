print("Benvingut al convertidor de graus Celsius a Kelvin o viceversa")

def convertidor_temperatura():
    print("Quina conversió de les següents opcions desitja fer?")
    print("1: Passar de Celsius a Kelvin")
    print("2: Passar de Kelvin a Celsius")

    opció = input("Introdueix una de les dues opcions (1 o 2): ")

    if opció == "1":
        celsius = float(input("Introdueix el nombre de graus Celsius que desitges convertir a graus Kelvin: "))
        kelvin = celsius + 273.15
        print(str(celsius) + " °C són " + str(kelvin) + " K")
    elif opció == "2":
        kelvin = float(input("Introdueix el nombre de graus Kelvin que desitges transformar a graus Celsius: "))
        celsius = kelvin - 273.15
        print(str(kelvin) + " K són " + str(celsius) + " °C")
    else:
        print("Opció no vàlida. Torna-ho a intentar")

convertidor_temperatura()
