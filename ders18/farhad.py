with open('data.txt', 'r', encoding='utf-8') as my_file:
    header_str = my_file.readline()
    data_list = my_file.readlines()

my_dict = {}

for data_line in data_list:
    data_attributes = data_line.split(", ")
    my_dict[data_attributes[0]] = {header_str.split(", ")[1] : data_attributes[1], header_str.split(", ")[2][:-1]: data_attributes[2][:-1]}

max_age = 0
max_name = ""
city = ""
for key, value in my_dict.items():
    if int(value['yaş']) > max_age:
        max_age = int(value['yaş'])
        max_name = key
        city = value['şəhər']
print(max_age, max_name, city)

max_age_list = []
for key, value in my_dict.items():
    max_age_list.append(int(value['yaş']))
print(max(max_age_list))

print(my_dict)