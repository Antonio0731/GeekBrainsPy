with open("text_7.txt","r",encoding="UTF-8") as file_op:
    my_f = file_op.readlines()
    for i, word in enumerate(my_f,1):
        total = len(word.split())
        print(f"Строка {i} содержит {total} слов")