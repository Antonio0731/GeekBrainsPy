from random import randint

with open("text_5task.txt","w",encoding="UTF-8") as task_5:
    my_list = [randint(0,1000) for i in range(randint(5,20))]
    task_5.write(' '.join(map(str,my_list)))
print(f"Сумма чисел равна {sum(my_list)}")