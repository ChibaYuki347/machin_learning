# module01.py

from python_sokusyu import modules1

a = input('a=')
b = input('b=')

a = int(a)
b = int(b)

ans1 = modules1.mul(a, b)
ans2 = modules1.div(a, b)

print('{0} * {1} = {2}'.format(a,b,ans1))
print('{0} / {1} = {2}'.format(a,b,ans2))

