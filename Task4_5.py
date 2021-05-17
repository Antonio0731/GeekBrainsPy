my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_new.txt","w",encoding="UTF-8") as file_new:
    with open("text_4.txt", "r", encoding="UTF-8") as file_old:
        file_new.writelines(line.replace(line.split()[0], my_dict.get(line.split()[0])) for line in file_old)