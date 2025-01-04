class Parrot:
    # class attribute
    species = "bird"
    # instance attribute
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# instantiate the Parrot class
blu = Parrot("Blu", 10, "male")
# access the class attributes
print("Blu is a {}".format(blu.species))
# access the instance attributes
print("{} is {} years old and is a {}".format( blu.name, blu.age, blu.gender))
