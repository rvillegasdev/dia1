puntos = int(input("Ingresa tu puntaje (0-100): "))

if puntos < 0 or puntos > 100:
    print("Puntaje inválido")
elif puntos < 60:
    print("Reprobado")
elif puntos < 80:
    print("Aprobado")
elif puntos < 90:
    print("Buen desempeño")
else:
    print("Excelente desempeño")
