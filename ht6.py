class Calc(object):
    last_result = None

    def add(self, a, b):
        self.last_result =  a + b

    def subtract(self, a, b):
        self.last_result = a - b

    def multiply(self, a, b):
        self.last_result = a * b

    def divide(self, a, b):
        try:
            self.last_result = a / b
        except ZeroDivisionError:
            self.last_result = 0
            print("Zerro division error!")


clc = Calc()
print(clc.last_result)
clc.add(3, 2)
print(clc.last_result)
