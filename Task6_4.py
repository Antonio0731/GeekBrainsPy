from itertools import count, cycle
from random import randint

i = int(input("Введите число от 1 до 10: "))
for j in count(i):
    if j > 13:
        break
    else:
        print(j)

my_l = list(input("Введите 3 любых символа через пробел: ").split())
f = 0
for el in cycle(my_l):
    if f > 13:
        break
    else:
        print(el)
        f += 1