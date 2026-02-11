monto = float(input("Ingresa el monto de tu compra: "))

if monto < 0:
    print("Monto inválido")
elif monto < 500:
    print("Nivel 1")
elif monto < 2000:
    print("Nivel 2")
else:
    print("Nivel 3")
