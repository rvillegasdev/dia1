limite = int(input("¿Hasta qué número quieres contar? (sólo números del 0 en adelante): "))

while limite < 0:
    print("Ingresa unicamente cero o números enteros positivos")
    limite = int(input("¿Hasta qué número quieres contar? (sólo números del 0 en adelante): "))

for numero in range(1, limite + 1):
        print("Número:", numero)

print("Conteo terminado")
