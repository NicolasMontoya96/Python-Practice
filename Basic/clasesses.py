class MyEmptyPerson:
    pass

print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.fullname = f"{name} {surname} {alias}"

    def walk(self):
        print(f"{self.fullname} está caminando")

my_person = Person("Nicolas", "Montoya")
print(my_person.fullname)
my_person.walk()

my_other_person = Person("Nicolas", "Montoya", "Mouredev")
print(my_other_person.fullname)
my_other_person.walk()
