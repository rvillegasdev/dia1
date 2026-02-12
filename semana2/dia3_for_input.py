while True:
    try:
        limite = int(input("¿Hasta qué número quieres contar? (sólo números del 0 en adelante): "))

        if limite < 0:
            print("Ingresa unicamente cero o números enteros positivos")
        else:
            break
            
    except ValueError:
        print("Eso no es un número válido. Intenta de nuevo.")

for numero in range(1, limite + 1):
        print("Número:", numero)

print("Conteo terminado")
