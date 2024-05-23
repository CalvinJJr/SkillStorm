# inheritance challenge
class Person:
    # Instance variables
    def __init__(self, greeting):
        self.greeting = str("Hello!")

    def speaks(self):
        print("I'm off to do whatever!\n")


Ann = Person("Ann")
print(Ann.greeting + " " + "I'm Ann!")
Ann.speaks()


class Customer(Person):

    def speaks(self):
        print("I'm a customer, I'm spending money!\n")

# Andy's rude, he doesn't inherit the greeting.


Andy = Customer("Andy")
Andy.speaks()


class Developer(Person):

    def speaks(self):
        print("I'm a developer, I'm off to code!\n")


Jake = Developer("Jake")
print(Jake.greeting + " " + "I'm Jake")
Jake.speaks()
