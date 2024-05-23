# inheritance challenge
class Person:
    # Instance variables
    has_identity = True

    if has_identity:
        print("Hi, I'm a person.")

    def speaks(self):
        print("I'm off to do whatever!\n")


person = Person()
person.speaks()


class Customer(Person):

    has_identity = False

    def speaks(self):
        print("I'm a customer, I'm spending money!\n")


customer = Customer()
customer.speaks()


class Developer(Person):

    has_identity = True

    def speaks(self):
        print("I'm a developer, I'm off to code!\n")


developer = Developer()
developer.speaks()
