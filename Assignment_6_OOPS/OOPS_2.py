
class Dog:
    def __init__(self):
        self.information={}

    def description(self):
        self.name = input("enter a name : ")
        self.age = input("enter a age :")
        print(self.get_info())

    def get_info(self):
        self.coat_colour = input("enter a colour of dog : ")
        # print(self.get_info())

class JackRussellTerrie(Dog):
    @staticmethod
    def breed():
        print("i m JackRussellTerrie breed ")


class Bulldog(Dog):
    @staticmethod
    def breed():
        print("i m Bulldog breed")

D1=JackRussellTerrie()
D1.breed()
D1.description()

D2=Bulldog()
D2.breed()
D2.description()