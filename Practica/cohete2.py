
velocidad_correcta = 11.2
velocidad_final = 0
entrada = input("Por favor ingrese un valor para la velocidad del cohete: ")

if  entrada == "":
    print("Por favor ingrese una velocidad válida para el cohete")
else:
    datoUsuario = float(entrada)

    if datoUsuario < 0:
        print("Por favor ingrese una velocidad válida para el cohete")

    elif datoUsuario >= velocidad_correcta:
        print("Felicidades, estamos en orbita")
    elif datoUsuario < velocidad_correcta:
        velocidad_final = velocidad_correcta - datoUsuario
        print(f"Te falta {velocidad_final} para llegar a la velocidad necesaria")
    
    
