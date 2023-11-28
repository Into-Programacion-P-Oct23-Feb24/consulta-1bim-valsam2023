limite = int(input("Ingrese un límite de veces para la suma de números pares: "))

suma_pares = 0
numero = 2

while numero <= limite:
    suma_pares = suma_pares + numero
    numero = numero + 2

print("La suma de los números pares hasta", limite, "es:", suma_pares)