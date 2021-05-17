my_dict = {}
with  open("text_6.txt","r",encoding="UTF-8") as obj:
    for line in obj:
        subj, num = line.split(":")
        sumnum = sum(map(int,''.join([i for i in num if i == ' ' or '0' <= i <= '9']).split()))
        my_dict[subj] = sumnum
print(f"{my_dict}")