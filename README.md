# Base Converter

Este programa es un conversor de bases numéricas. Permite al usuario convertir números entre diferentes bases: decimal, binario, octal y hexadecimal.

## Funcionamiento

El programa se ejecuta en un bucle infinito hasta que el usuario decida salir. En cada iteración, se presenta un menú con las siguientes opciones:

1. Convertir desde decimal
2. Convertir desde binario
3. Convertir desde octal
4. Convertir desde hexadecimal
5. Salir

El usuario debe ingresar el número de la opción que desea ejecutar.

### Convertir desde decimal

Si el usuario selecciona la opción 1, se le pedirá que ingrese un número decimal. Luego, el programa convertirá este número a binario, octal y hexadecimal y mostrará los resultados.

### Convertir desde binario

Si el usuario selecciona la opción 2, se le pedirá que ingrese un número binario. Luego, el programa convertirá este número a decimal, octal y hexadecimal y mostrará los resultados.

### Convertir desde octal

Si el usuario selecciona la opción 3, se le pedirá que ingrese un número octal. (Nota: esta función aún no está implementada completamente)

### Convertir desde hexadecimal

Si el usuario selecciona la opción 4, se le pedirá que ingrese un número hexadecimal. (Nota: esta función aún no está implementada completamente)

### Salir

Si el usuario selecciona la opción 5, el programa terminará.

## Validación de entrada

El programa valida la entrada del usuario para asegurarse de que es válida para la base seleccionada. Por ejemplo, si el usuario está ingresando un número binario, el programa verificará que todos los caracteres sean 0 o 1. Si el usuario ingresa un valor inválido, se le pedirá que ingrese un nuevo valor.