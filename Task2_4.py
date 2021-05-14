from random import randint

my_l = [randint(0, 1001) for i in range(0, randint(5, 15))]
final = [my_l[j] for j in range(1, len(my_l)) if my_l[j] > my_l[j-1]]
print(my_l)
print(final)