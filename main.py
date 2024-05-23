import re

def pedirValor(base):
    while True:
        try:
            if base == "binario":
                r = input('\n' + "Por favor escriba su valor " + base + ": ")
                if not all(char in '01' for char in r):
                    raise ValueError
            elif base == "hexadecimal":
                r = input('\n' + "Por favor escriba su valor " + base + ": ")
                if not re.match('[0-9A-Fa-f]+', r):
                    raise ValueError
            else:
                r = float(input('\n' + "Por favor escriba su valor " + base + ": "))
            return r
        except ValueError:
            print('Número ' + base + ' Inválido')

def main():
    while True:
        print("Bienvenido al conversor de bases.\n")
        print("Seleccione la opción a ejecutar.\n")

        print("1. Convertir desde decimal")
        print("2. Convertir desde binario")
        print("3. Convertir desde octal")
        print("4. Convertir desde hexadecimal")
        print("5. Salir")

        exOption = input('\n' + 'Digite el número de la opción: ')

        if exOption == "1":
            decimalToOthers()
        elif exOption == "2":
            binarioToOthers()
        elif exOption == "3":
            octalToOthers()
        elif exOption == "4":
            hexadecimalToOthers()
        elif exOption == "5":
            print("Gracias por usar el conversor de bases. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor seleccione una opción válida.")

def decimalToOthers():
    decimal = float(pedirValor("decimal"))
    binario = bin(int(decimal))
    print("Decimal: " + str(decimal) + " => Binario: " + binario)
    octal = oct(int(decimal))
    print("Decimal: " + str(decimal) + " => Octal: " + octal)
    hexadecimal = hex(int(decimal))
    print("Decimal: " + str(decimal) + " => Hexadecimal: " + hexadecimal)

def binarioToOthers():
    binario = pedirValor("binario")
    decimal = int(binario, 2)
    print("Binario: " + binario + " => Decimal: " + str(decimal))
    octal = oct(decimal)
    print("Binario: " + binario + " => Octal: " + octal)
    hexadecimal = hex(decimal)
    print("Binario: " + binario + " => Hexadecimal: " + hexadecimal)

def octalToOthers():
    octal = pedirValor("octal")
    decimal = int(octal, 8)
    print("Octal: " + octal + " => Decimal: " + str(decimal))
    binario = bin(decimal)
    print("Octal: " + octal + " => Binario: " + binario)
    hexadecimal = hex(decimal)
    print("Octal: " + octal + " => Hexadecimal: " + hexadecimal)

def hexadecimalToOthers():
    hexadecimal = pedirValor("hexadecimal")
    decimal = int(hexadecimal, 16)
    print("Hexadecimal: " + hexadecimal + " => Decimal: " + str(decimal))
    binario = bin(decimal)
    print("Hexadecimal: " + hexadecimal + " => Binario: " + binario)
    octal = oct(decimal)
    print("Hexadecimal: " + hexadecimal + " => Octal: " + octal)
    input('\n' + 'Presione cualquier tecla para continuar...')

if __name__ == "__main__":
    main()
