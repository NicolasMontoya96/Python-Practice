my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))


my_other_dict = {"Nombre":"Nicolas", "Apellido":"Montoya","Edad":"29", 1:"Python"}

my_dict = {
    "Nombre":"Nicolas", 
    "Apellido":"Montoya",
    "Edad":"29", 
    1:"Python",
    "Lenguajes": {"Python","Swift","Kotlin"}
    }

print(my_other_dict)
print(my_dict)

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])


my_dict["Calle"] = "Calle Nicolas"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print(my_dict.items)
print(my_dict.keys)
print(my_dict.values)
print(my_dict.fromkeys)

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))