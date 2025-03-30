"""
data.txt faylını oxuyun və məlumatları dict-də saxlayın və dict-i print edin.
Ad key, qalan melumatlar ise key: value sheklinde hemin key-in altinda olmalidir

Print edilən dict belə görünməlidir:
{
    'Farhad': {
        'yaş': 25,
        'şəhər': 'Bakı'
    },
    'Aygün': {
        'yaş': 30,
        'şəhər': 'Gəncə'
    },
    'Murad': {
        'yaş': 22,
        'şəhər': 'Sumqayıt'
    },
    'Zəhra': {
        'yaş': 28,
        'şəhər': 'Naxçıvan'
    }
}
"""
with open('data.txt', 'r') as my_file:
    header_str = my_file.readline()
    data_list = my_file.readlines()

my_dict = {}

for data_line in data_list:
    data_attributes = data_line.split(", ")
    my_dict[data_attributes[0]] = {header_str.split(", ")[1] : data_attributes[1], header_str.split(", ")[2][:-1]: data_attributes[2][:-1]}

print(my_dict)
