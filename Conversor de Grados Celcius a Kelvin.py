print ("Bienvenido al conversor de grados Celcius a Kelvin o viceversa")

def convertidor_temperatura():
    print ("¿Que conversion de las siguientes opciones desea hacer?")
    print ("1: Pasar de Celcius a Kelvin")
    print ("2: Pasar de Kelvin a Celcius")

    opcion = input("Ingrese una de las dos opciones (1 o 2): ")   

    if opcion == "1":
      celcius = float(input("Introduce el numero de grados Celcius que deseas convertir a grados Kelvin: "))
      kelvin = celcius + 273.15
      print (str(celcius) + " °C son " + str(kelvin) + " K ")
    elif opcion == "2":
      kelvin = float(input(" Introduce el numero de grados Kelvin que deseas transformar a grados Celcius: "))
      celcius = kelvin - 273.15
      print (str(kelvin) + " K son " + str(celcius) + " °C ")
    else:
      print ("Opcion no valida. Vuelve a intentarlo")

convertidor_temperatura()
