# def tabla_de_multiplicar(numero):
#     print(f"Tabla de multiplicar del {numero}:")
#     for i in range(1, 10):
#         resultado = numero * i
#         print(f"{numero} x {i} = {resultado}")

# try:
#     numero = int(input("Ingrese un número"))
#     tabla_de_multiplicar(numero)
# except ValueError:
#     print("Error: Ingrese un número válido.")
# def es_primo(numero):
#     if numero <= 1:
#         return False
#     elif numero <= 3:
#         return True
#     elif numero % 2 == 0 or numero % 3 == 0:
#         return False
#     i = 5
#     while i * i <= numero:
#         if numero % i == 0 or numero % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# numero = input("Ingrese un número para determinar si es primo: ")

# if numero.isdigit():
#     numero = int(numero)
#     if es_primo(numero):
#         print(f"{numero} es un número primo.")
#     else:
#         print(f"{numero} no es un número primo.")
# else:
#     print("Error: Ingrese un número válido.")
# def suma_hasta(numero):
#     suma = 0
#     for i in range(1, numero + 1):
#         suma += i
#     return suma

# try:
#     numero = int(input("Ingrese un número: "))
#     if numero > 0:
#         resultado = suma_hasta(numero)
#         print(f"La suma desde 1 hasta {numero} es: {resultado}")
#     else:
#         print("Ingrese un número positivo.")
# except ValueError:
#     print("Error: Ingrese un número válido.")