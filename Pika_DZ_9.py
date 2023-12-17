import json
import csv
# # Ex_1
# c = b'r\xc3\xa9sum\xc3\xa9'
# s = c.decode()
# print(s)
# d = s.encode("Latin1")
# print(d)
# h = d.decode("Latin1")
# print(h)
# # Ex_2
# a = "Name"
# b = "Surname"
# c = "Age"
# d = "Status"
# f = open('my_homework', 'w+')
# f.write(f'{a}\n{b}\n')
# f.close()
# f = open('my_homework', 'a')
# f.write(f'{b}\n{c}\n')
# f.close()
# Ex_3
new_dic = {
    123456: ("Arthur", 22),
    654321: ("Dima", 24),
    234561: ("Vasya", 23),
    345612: ("Nastya", 20),
    456123: ("Valya", 31),
}
with open("new_dic.json", "w") as file:
    json.dump(new_dic, file)
# Ex_4
with open("new_dic.json", "r") as file:
    new_dic_1 = json.load(file)
    number_dic = ["id", "name", "age", "phone_number"]
with open("new_sl1.csv", "w") as csv1:
    writedic = csv.DictWriter(csv1, fieldnames = number_dic)
    writedic.writeheader()
    for key, values in new_dic_1.items():
        writedic.writerow({"id": key, "name": values[0], "age": values[1], "phone_number": ""})