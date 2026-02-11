opcion = "1"

while opcion != "salir":
    print("\nMenú:")
    print("1 - Saludar")
    print("2 - Mostrar número secreto")
    print("\nEscribe 'Salir' para terminar")
    
    opcion = input("\nElige una opción: ")
    
    if opcion == "1":
        print("\nHola, humano.")
    elif opcion == "2":
        print("\nEl número secreto es 42.")
        while opcion == "2":
            print("\nMenú:")
            print("1 - Saludar")
            print("2 - Mostrar número secreto")
            print("\nEscribe 'Salir' para terminar")
            
            opcion = input("\nElige una opción: ")
            
            if opcion == "1":
                print("\nHola, humano.")
                opcion = "2"
            elif opcion == "2":
                print("\nYa no es posible consultar el número secreto.")
            elif opcion == "salir":
                print("\nCerrando programa")
                opcion = "salir"
            else:
                print("\nOpción inválida")
    elif opcion == "salir":
            print("\nCerrando programa...")
    else:
        print("\nOpción inválida.")
