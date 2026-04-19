
def printnumbers(param1, param2):
    for number in range(1,101):
        if number % 3 == 0:
            print(param1)
        elif number % 5 == 0:
            print(param2)
        elif number % 3 == 0 and number % 5 == 0:
            print(f"{param1} + {param2}")

printnumbers("Cadena 1", "Cadena 2")