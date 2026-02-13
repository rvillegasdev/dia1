def pedir_opcion():
    while True:
        print("\n--- MENÚ ---")
        print("1 - Contar hacia arriba")
        print("2 - Contar hacia abajo")
        print("3 - Suma del 1 hasta N")
        print("4 - Salir")

        opcion = input("Elige una opción: ")
        
        if opcion in ["1", "2", "3", "4"]:
            return opcion
        else:
            print("Opción inválida. Intenta de nuevo.")

def pedir_limite():
    while True:
        try:
            limite = int(input("Ingresa un número positivo: "))
            if limite < 0:
                print("Sólo números positivos.")
            else:
                return limite
        
        except ValueError:
            print("Eso no es un número válido.")

def contar_arriba(limite):
    for numero in range(1, limite + 1):
        print(numero)

def contar_abajo(limite):
    for numero in range(limite, 0, -1):
        print(numero)

def sumar_hasta(limite):
    total = 0
    for numero in range(1, limite + 1):
        total += numero
    print("La suma total es: ", total)

while True:
    opcion = pedir_opcion()
    
    if opcion == "4":
        print("Programa finalizado.")
        break
    limite = pedir_limite()
    
    if opcion == "1":
        contar_arriba(limite)
    
    elif opcion == "2":
        contar_abajo(limite)
    
    elif opcion == "3":
        sumar_hasta(limite)
