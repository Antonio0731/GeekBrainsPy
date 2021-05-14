from functools import reduce

def my_f(el1, el2):
    return el1 * el2

my_l = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(my_f, my_l))