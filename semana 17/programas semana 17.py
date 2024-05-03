# def tipo_triangulo(a, b, c):
#     if a == b == c:
#         return "Equilátero"
#     elif a == b or a == c or b == c:
#         return "Isósceles"
#     else:
#         return "Escaleno"

# print("ingresar los ladoz del triangulo:")
# lado1 = float(input("Lado 1: "))
# lado2 = float(input("Lado 2: "))
# lado3 = float(input("Lado 3: "))

# if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
#     tipo = tipo_triangulo(lado1, lado2, lado3)
#     print("El triángulo es", tipo)
# else:
#     print("variable no valida")

# import math

# def obtener_perimetro(radio):
#     return 2 * math.pi * radio

# def obtener_area(radio):
#     return math.pi * radio ** 2

# def obtener_volumen(radio):
#     return (4/3) * math.pi * radio ** 3

# radio = float(input("Ingrese el radio: "))

# perimetro = obtener_perimetro(radio)
# area = obtener_area(radio)
# volumen = obtener_volumen(radio)

# print("perímetro del circulo:", perimetro)
# print("area del círculo:", area)
# print("volumen de la esfera:", volumen)

def imprimir_nombre_mes(numero):
    meses = ["Ene", "Febre", "Mar", "Abri", "May", "Jun",
             "Jul", "Ago", "Sep", "Oct", "Novi", "Dic"]
    
    if 1 <= numero <= 12:
        print("El mes correspondiente al número", numero, "es", meses[numero - 1])
    else:
        print("Error: El número ingresado no válido (1 al 12).")

numero_mes = int(input("Ingrese un número del 1 al 12: "))
imprimir_nombre_mes(numero_mes)