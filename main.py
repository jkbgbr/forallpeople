

import forallpeople as si

si.environment('structural2', top_level=False)

si.mm = 0.001 * si.m

a = 1 * si.m
a.to()
a.to('mm')

print(a)


# si.environment('default', [top_level=False])

