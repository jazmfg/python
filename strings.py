# Escribe un programa que pregunte el nombre del usuario y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido (end="" argumento de la función print() que controla como termina la salida)

nombre = input("Ingresa tu nombre: ")
entero = int(input("Ingresa un número entero: "))

print((nombre + "\n") * (entero), end="")

# Escribe un programa que pregunte el nombre completo del usuario y lo muestre por pantalla una con todas las letras en minúsculas, otra con todas las letras en mayúsculas y otra con la primera letra del nombre y de los apellidos en mayúscula

nombre = input("Ingresa tu nombre completo: ")

print(nombre.upper())
print(nombre.lower())
print(nombre.title())

# Escribe un programa que pregunte el nombre del usuario y después muestre por pantalla "<NAME> tiene <n> letras" donde <NAME> es el nombre de usuario en mayúsculas y <n> es el número de letras que tiene el nombre

nombre = input("Ingresa tu nombre: ")
n = len(nombre.replace(" ", ""))

print(f"{nombre.upper()} tiene {n} letras")

# Los teléfonos de una empresa tienen el siguiente formato: prefijo-número-extension. El prefijo es el código del país y la extensión tiene 2 dígitos (ejemplo: +52-7773189654-90). Escribe un programa que pregunte por un número de télefono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión

num = input("Ingresa un número de teléfono con el siguiente formato, prefijo-número-extensión ejemplo: +52-7772842849-41: ")
numero = num.split("-")

print(f"Número sin prefijo y extensión: {numero[1]}")

# Escribe un programa que pida al usuario una frase y muestre por pantalla la frase invertida

frase = input("Ingresa una frase: ")
print(f"Frase invertida: {frase[::-1]}")

# Escribe un programa que pida al usuario una frase y una vocal, después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula

frase = input("Ingresa una frase: ")
vocal = input("Ingresa una vocal: ")

print(frase.replace(vocal, vocal.upper()))

# Escribe un programa que pregunte el email del usuario y muestre otro email con el mismo nombre pero con dominio 'ceu.es' 

email = input("Ingresa tu email: ")
correo = email.split("@")

print(f"Tu correo es: {correo[0]}@ceu.es")

# Escribe un programa que pregunte al usuario su fecha de nacimiento en formato dd/mm/yyyy, adaptar el programa para que funcione cuando el día o mes se introduce con un solo carácter (Método zfill(n) si el string es más corto que 'n' agrega ceros al principio hasta que su logitud sea de n caracteres)

fecha = input("Ingresa tu fecha de nacimiento en formato: dd/mm/aaaa: ")
dia, mes, año = fecha.split("/")

dia = dia.zfill(2)
mes = mes.zfill(2)

print(f"Día: {dia}\nMes: {mes}\nAño: {año}")

# Pide al usuario que ingrese varias palabras separadas por espacios y muestra la palabra más larga

palabras = input("Ingresa varias palabras separadas por espacios: ").split()

palabra_maxima = max(palabras, key=len)
print(f"La palabra más larga es {palabra_maxima}")

# Pide al usuario su nombre y edad, y calcula en qué año cumplirá 100 años (Puedes usar un año fijo, por ejemplo 2025)

import datetime

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

año_actual = datetime.datetime.now().year

años_faltantes = 100 - edad
año_100 = año_actual + años_faltantes

print(f"En el año {año_100}, cumplirás 100 años")

# Calcula el factorial de un número ingresado por el usuario

import math

n = int(input("Ingresa un número: "))
print(f"El factorial de {n} es: {math.factorial(n)}")