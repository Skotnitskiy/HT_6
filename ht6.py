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
        super(Oval, self).__init__(color)
        self.diameter = diameter


class Square(Figure):
    def __init__(self, color, x, y):
        super(Square, self).__init__(color)
        self.x = x
        self.y = y


oval = Oval(10, "Red")
print(oval.color, oval.diameter)

sqr = Square(10, 20, "Black")
print(sqr.color, sqr.x, sqr.y)


class Library(object):
    books = {"book1": "text1", "book2": "text2", "book3": "text3"}

    def get_book(self, name):
        bk = self.books.get(name)
        del self.books[name]
        return bk

    def give_back(self, bk):
        self.books.update(bk)
        print("The book {} returned".format(bk))


library = Library()
print(library.books)
book_name = "book1"
book_text = library.get_book(book_name)
book = {book_name: book_text}
print(library.books)
library.give_back(book)
print(library.books)


class A(object):
    value = "some value"


class B(object):
    def func(self, a_obj):
        a_obj.value = "Next value"
        return a_obj.value


a = A()
print(a.value)
b = B()
print(b.func(a))


class Counter(object):
    count = 0

    def __init__(self):
        self.__class__.count += 1


print(Counter().count)
print(Counter().count)
print(Counter().count)
print(Counter().count)
print(Counter().count)


class Thing(object):
    pass


thing = Thing()
print("Thing class ", type(Thing), "Thing object ", Thing())


class Thing2(object):
    pass


Thing2.letters = "abc"
print(Thing2.letters)


class Thing3(object):
    pass


thing3 = Thing3()
thing3.letters = "xyz"
print(thing3.letters)


class DefaultClass(object):
    def __init__(self, name, symbol_number):
        self.name = name
        self.symbol_name = symbol_number


default_class_obj = DefaultClass("Some name", 10)
print(default_class_obj.name, default_class_obj.symbol_name)


dict_of_class = {'name': 'Vasya', 'l_name': 'Pupkin', 'age': 20}


class DefaultClass1(object):
    def __init__(self, dict):
        object.__setattr__(self, "__dict__", dict)

    def print_info(self):
        for key, value in self.__dict__.items():
            print(key, "=", value)


user = DefaultClass1(dict_of_class)
user.print_info()


class X(object):
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2


class Y(X):
    def __init__(self, val1, val2):
        super(Y, self).__init__(val1, val2)


class Z(Y):
    def __init__(self, val1, val2, val3):
        super(Z, self).__init__(val1, val2)
        self.val3 = val3


z = Z(1, 5, 10)
print(z.val1, z.val2, z.val3)
