def my_f3():
    zp={}
    try:
        with open("text_3.txt", "r", encoding="UTF-8") as file_op:
            for line in file_op:
                zp[line.split()[0]] = float(line.split()[1])
        print("Меньше 20000 получают: ")
        for name, oklad in zp.items():
            if oklad < 20000:
                print(name)
        print(f"Средняя зарплата сотрудников равна {sum(zp.values()) / len(zp)}")
    except IOError:
        print("Ошибка")

my_f3()

