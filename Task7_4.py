def fact_gen(num):
    f = 1
    for i in range(num+1):
        yield f"{i}!={f}"
        f *= i + 1

for el in fact_gen(int(input("Введите число для расчета факториала: "))):
    print(el)