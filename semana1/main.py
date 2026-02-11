def es_usuario_valido(nombre):
    es_largo = len(nombre) > 4
    empieza_con_r = nombre[0] == "R"
    empieza_con_a = nombre[0] == "A"
    
    if es_largo and (empieza_con_r or empieza_con_a):
        return True
    else:
        return False

usuarios = ["Ana", "Luis", "María", "Roberto", "Sol", "Alejandro"]

for nombre in usuarios:
    if es_usuario_valido(nombre):
        print(nombre))
