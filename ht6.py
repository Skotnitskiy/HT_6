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
print(clc.last_result)
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
        print("Age = {}, Name = {}".format(self.age, self.name))


p = Person(24, "Sergey")
p.show_all_information()
