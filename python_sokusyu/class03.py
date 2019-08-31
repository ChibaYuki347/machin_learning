# class03.py
from python_sokusyu.inherit import Calc
from python_sokusyu.inherit import SuperCalc

sup = Calc()
sup.a = 1
sup.b = 2

print(sup.add())
print(sup.sub())
# print(sup.mul())
# print(sup.div())

sub = SuperCalc()

sub.a = 3
sub.b = 2

print(sub.add())
print(sub.sub())
print(sub.mul())
print(sub.div())

