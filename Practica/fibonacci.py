def fibonacci():
    a = 0
    b = 1
    c = 0
    
    for i in range(0,51):
        print(a)            # A vale Cero porque así la incializamos
        c = a + b           # C es igual a 0 + 1, es valor de las variables que se inicializaron
        a = b               # A vale
        b = c               # B vale 1, que es igula a A + b


fibonacci()