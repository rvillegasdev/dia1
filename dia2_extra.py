edad = int(input("Ingresa tu edad: "))

if edad < 0 or edad > 120:
    print("Edad inválida")
elif edad < 13:
    print("Infancia")
elif edad < 18:
    print("Adolescencia")
elif edad < 65:
    print("Adultez")
else:
    print("Adulto mayor")
