

import forallpeople as si
si.environment(env_name='structural', top_level=False)

# si.mm = 0.001 * si.m

a = 1 * si.m
# a.to()
# a.to('mm')

b = 1 * si.km
b.to()
print(b)
#
# print(a)


# si.environment('default', [top_level=False])

