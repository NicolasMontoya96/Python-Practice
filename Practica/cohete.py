
def cohete(velocidad):
    velocidad_obligatoria = 11.2
    if not velocidad_actual:
        print("Por favor ingrese un valor para la velocidad del cohete")
        return cohete(velocidad)
    
    elif velocidad < 0 :
        print("Error, por favor ingrese una velocidad válida para el cohete ")

    elif velocidad >= velocidad_obligatoria:
        print("¡Felicidades, estamos en órbita!")
    else:
        velocidad < velocidad_obligatoria
        velocidad_necesaria = velocidad_obligatoria - velocidad
        print(f"Aún te falta {velocidad_necesaria} para alcanzar la velocidad necesaaria.")


velocidad_actual = float(input("Por favor ingrese la velocidad actual del cohete: "))
cohete(velocidad_actual)



