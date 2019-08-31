# inherit.py

class Calc:
    def __init__(self):
        self.a = 0
        self.b = 0

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b


class SuperCalc(Calc):
    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a // self.b
