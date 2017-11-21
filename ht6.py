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


"""Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів, 
які зберігатиме в відповідні змінні. 
Методи, які повинні бути в класі Person - show_age, print_name, show_all_information."""

class Person(object):
