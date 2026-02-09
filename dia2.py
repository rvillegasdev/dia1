hora = int(input("¿Qué hora es? (0-23): "))

if hora < 0 or hora > 23:
    print("Hora inválida")
elif hora < 12:
    print("Es mañana")
elif hora < 18:
    print("Es tarde")
else:
    print("Es noche")
