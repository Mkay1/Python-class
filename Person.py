class Person:
    specie = "Human"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self, food):
        return "{} is eating {}".format(self.name, food)

p1 = Person("Nnamdi", 7, "Male")
p2 = Person("Ekene", 3, "Male")

print(p2.eat("Yam and sauce"))