class Calc(object):
    """ Last_result it is variable where will be saved result of calculation, by default is None. """
    last_result = None

    """ These are methods that take 2 arguments a and b and execute corresponding operations with these arguments, 
    then set the last_result variable to the last_result of the execution of the operation.
    
    """
    def add(self, a, b):
        self.last_result = a + b

    def subtract(self, a, b):
        self.last_result = a - b

    def multiply(self, a, b):
        self.last_result = a * b

    def divide(self, a, b):
        try:
            """ Trying divide a on b. """
            self.last_result = a / b
        except ZeroDivisionError:
            """ If get division by zero then set to last_result 0 and print message about error. """
            self.last_result = 0
            print("Zero division error!")


clc = Calc()
clc.add(3, 2)
print(clc.last_result)


class Person(object):
    def __init__(self, *args):
        self.age = args[0]
        self.name = args[1]

    def show_age(self):
        return self.age

    def print_name(self):
        print("Name is", self.name)

    def show_all_information(self):
        for key, value in self.__dict__.items():
            print(key, "=", value)


person1 = Person(24, "Sergey")
person2 = Person(26, "Qwerty")
person1.profession = "Student"
person2.profession = "Worker"
person1.show_all_information()


class Figure(object):
    def __init__(self, color="white"):
        self.color = color

    def set_color(self, color):
        self.color = color


class Oval(Figure):
    def __init__(self, color, diameter):
        self.color = color
        self.diameter = diameter


class Square(Figure):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y


oval = Oval(10, "Red")
print(oval.color, oval.diameter)

sqr = Square(10, 20, "Black")
print(sqr.color, sqr.x, sqr.y)
