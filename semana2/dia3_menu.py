opcion = ""
secreto_mostrado = False

while opcion != "salir":
    print("\nMenú:")
    print("1 - Saludar")
    print("2 - Mostrar número secreto")
    print("\nEscribe 'salir' para terminar")
    
    opcion = input("\nElige una opción: ")
    
    if opcion == "1":
        print("\nHola, humano.")
    elif opcion == "2":
            if not secreto_mostrado:
                    print("\nEl número secreto es 42.")
                    secreto_mostrado = True
            else:
                print("\nYa no es posible consultar el número secreto.")
    elif opcion == "salir":
            print("\nCerrando programa...")
    else:
        print("\nOpción inválida.")
