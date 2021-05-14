my_l = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_l = [i for i in my_l if my_l.count(i) == 1]

print(new_l)