while True:
    velocidad_necesaria = 11.2
    velocidad_encontrada = 0
    datoUsuario = input("Ingrese una velocidad para el cohete: ")
    try:
        if datoUsuario == "salir":
            print("!Hasta luego¡")
            break
        elif datoUsuario == "":
            print("Por favor ingrese un valor para la velocidad")
        else:
            entrada = float(datoUsuario)
            if entrada < 0:
                print("Por favor ingrese un valor válido para la velocidad")

            elif entrada >= velocidad_necesaria:
                print("Felicidades, estamos en orbita")
            elif entrada < velocidad_necesaria:
                velocidad_encontrada = velocidad_necesaria - entrada
                print(f"Velocidad no suficiente, aún te faltan {velocidad_encontrada} km/s")
                
    except ValueError:
        print("Por favor ingrese un dato válido")