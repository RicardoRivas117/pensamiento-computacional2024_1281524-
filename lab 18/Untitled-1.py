# ejercicio 1

# def obtener_menor_precio(lista_precios):
#     return min(lista_precios)

# def obtener_mayor_precio(lista_precios):
#     return max(lista_precios)

# precios = [50, 75, 46, 22, 80, 65, 8]

# menor_precio = obtener_menor_precio(precios)
# mayor_precio = obtener_mayor_precio(precios)

# print("El precio menor:", menor_precio)
# print("El precio mayor:", mayor_precio)



# # ejercicio 2

# abecedario = list("abcdefghijklmnopqrstuvwxyz")  

# abecedario_filtrado = []  


# for i in range(len(abecedario)):
#     if (i + 1) % 3 != 0:
#         abecedario_filtrado.append(abecedario[i]) 

# print("Abecedario nuevo:", abecedario_filtrado) 



# ejercicio 4

# import random

# vector = []

# for _ in range(100):
#     vector.append(random.randint(1, 1000))

# print("Números pares:")
# for num in vector:
#     if num % 2 == 0:
#         print(num, end=" ")

# print("Números impares:")
# for num in vector:
#     if num % 2 != 0:
#         print(num, end=" ")