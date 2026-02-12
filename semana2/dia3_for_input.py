while True:
        entrada = input("¿Hasta qué número quieres contar? (0 o positvo, o 'salir'):  ")

        if entrada.lower() == "salir":
            print("Programa finalizado por el usuario.")
            break
        
        try:
            limite = int(entrada)
            
            if limite < 0:
                print("Solo se permiten números 0 o positivos.")
            else:
                for numero in range(1, limite + 1):
                    print("Número: ", numero)
                print("Conteo terminado.")
                break
        except ValueError:
            print("Eso no es un número válido. Intenta de nuevo.")

