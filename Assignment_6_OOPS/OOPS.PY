class Dog:
    def __init__(self):
        self.information={}

    def description(self):
        self.name = self.my_name
        self.age = self.my_age
        print(self.get_info())

    def get_info(self):
        self.coat_colour = self.my_coat_colour

class JackRussellTerrie(Dog):
    def breed(self):
        print("i m JackRussellTerrie breed ")
        self.my_name = print("i m TOM")
        self.my_age = print("i m 8 years old")
        self.my_coat_colour =print("my coat colour is black with white")


class Bulldog(Dog):
    def breed(self):
        print("i m Bulldog breed")
        self.my_name = print("i m JACK")
        self.my_age = print("i m 10 years old")
        self.my_coat_colour =print("my coat colour is brown")

D1=JackRussellTerrie()
D1.breed()
D1.description()

D2=Bulldog()
D2.breed()
D2.description()