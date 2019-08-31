# module02.py

from python_sokusyu.modules1 import mul
from python_sokusyu.modules1 import div
a = input('a=')
b = input('b=')

a = int(a)
b = int(b)

ans1 = mul(a,b)
ans2 = div(a,b)

print('{0} * {1} = {2}'.format(a,b,ans1))
print('{0} / {1} = {2}'.format(a,b,ans2))

