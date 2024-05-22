# Working with constructors

class Developer:

    # Instance variables
    name: str
    salary: str
    language: str


def __init__(self, name, salary, language):
    # setting up initial values for the challenge
    self.name = name
    self.salary = salary
    self.language = language


# calling the constructor to create and initialize objects

object1 = Developer("Dan Pickles", "salary: $100,000", "language: Python")

object2 = Developer("Randolph Scott", "salary: $90,000", "language: SQL")

object3 = Developer("Howard Johnson", "salary: $70,000", "language: Java")


print(object1.name + " " + object1.language)
print(object2.name + " " + object2.language)
print(object3.name + " " + object3.language)
