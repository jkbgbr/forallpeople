#
#
# import forallpeople as si
# si.environment(env_name='structural', top_level=False)
#
# # si.mm = 0.001 * si.m
#
# a = 1 * si.m
# # a.to()
# # a.to('mm')
# b = 1 * si.km
# c = (a+b)
# print(c)
# print(c.to())
# print(c.value)
# print(c.factor)
# print(c.dimensions)
#
# print(c.prefix('m'))
# # si.environment('default', [top_level=False])
#

import pathlib
import forallpeople as si
# si.environment(pathlib.Path('E:/modules/forsipeople/forsipeople/environments/default.json'))
si.environment('default')
# q = 3 * si.kN / si.m**2
# print(q)
# print(q.to())
# print(q.to('MPa'))
# q = 3 * si.kN_m2
# print(q)

import timeit

mysetup = """import forallpeople as si
si.environment('default')
import math
import random"""

mycode = """

x = random.randint(1, 100) * si.m
y = random.randint(1, 100) * si.m
z = 0

def f(x, y, z):
    _ret = (z + x - y) / (x + y - z) * math.log(x/y)

f(x, y, z)
"""

print(timeit.timeit(setup=mysetup,
                    stmt=mycode,
                    number=100000))