#
#
import forallpeople as si
si.environment(env_name='structural', top_level=False)
q = 3 * si.kN / si.m**2
print(q)
# print(q.to())
# print(q.to('MPa'))
print('mi')
q = 3 * si.N_m / si.m
print(q)
qq = 3 * si.N_m / si.m
print(qq)
print(qq / q)
