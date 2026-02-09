grados = float(input("Ingresa la temperatura de la CDMX en °C: "))

if grados < 0 or grados > 32:
    print("Ingresa el valor de nuevo. Temperatura totalmente fuera de rango para dicha ubicación")
elif grados >= 0 and grados <= 17:
    print(f"{grados}°C en la CDMX es considerada baja temperatura")
elif grados > 17 and grados <= 22:
    print(f"{grados}°C en la CDMX es considerada temperatura templada")
elif grados > 22 and grados <= 32:
    print(f"{grados}°C en la CDMX es considerada alta temperatura")
