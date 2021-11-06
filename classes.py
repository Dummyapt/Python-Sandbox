# class
class Student:
    # class documentation
    """
    This class creates a student with an ID, first and last name
    """

    # private members
    __number: int
    __first_name: str
    __last_name: str

    # constructor
    def __init__(self, number, first_name, last_name):
        self.__number = number
        self.__first_name = first_name
        self.__last_name = last_name

    # private member function
    def __display_details(self):
        # accessing private data members
        print("Number: ", self.__number)
        print("First name: ", self.__first_name)
        print("Last name: ", self.__last_name)

    # public member function
    def access_private_function(self):
        # accessing private member function
        self.__display_details()
        return ""


# creating object of Student
a = Student(1, "Duha", "Cinar")

print(Student.__doc__)
print(a.access_private_function())


class Animal:
    color: str
    name: str

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def sound(self):
        print("What am I?")


class Cat(Animal):
    def sound(self):
        print("Meow!")


class Dog(Animal):
    def sound(self):
        print("Woof!")


my_cat = Cat("White", "D-Cat")
my_cat.sound()
