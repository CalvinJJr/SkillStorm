# inheritance challenge
class Person:
    # Instance variables
    has_title = True

    def speaks(self):
        print("Hi, I'm a person!")


person = Person()
person.speaks()


class Customer(Person):

    def speaks(self):
        print("I'm spending money!")


customer = Customer()
customer.speaks()


class Developer(Person):

    def speaks(self):
        print("I'm off to code!")


developer = Developer()
developer.speaks()


