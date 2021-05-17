import json
with open("text_7_new_json.json","w",encoding="UTF-8") as new_obj:
    with open("text_7.txt","r",encoding="UTF-8") as obj:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in obj}
        final = [profit, {"Средняя прибыль: " : round(sum([int(n) for n in profit.values() if int(n) > 0]) /
                                                    len([int(n) for n in profit.values() if int(n) > 0]))}]
    json.dump(final, new_obj, ensure_ascii=False)