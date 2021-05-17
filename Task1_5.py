with open("text_10.txt","w",encoding="UTF-8") as open_f:
    while True:
        string = input("Введите строку или пустую строку для завершения работы программы: ")
        if not string:
            break
        open_f.write(f"{string}\n")

