from sys import argv
def salary():
    try:
        work, hour, prem = argv[1:]
        print(f"Зарплата сотрудника равна {float(work)*float(hour)+float(prem)}")
    except ValueError:
        print("Введите 3 числа!")

salary()