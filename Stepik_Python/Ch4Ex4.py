data = open("C:\\Users\\user\\Documents\\Python_projects\\Stepik_Python\\dataset_3363_2.txt", "r")
data_set = data.readlines()

new_str = ''
for i in data_set:
    new_str = i.replace('\n', '')

result = ''
letter = ''

for i, char in enumerate(new_str):
    if char.isalpha() is True:
        letter = char
    elif i == len(new_str)-1:
        num = char
        result += letter * int(num)
        num = ''
    elif char.isdigit() is True and new_str[i+1].isdigit() is True:
        num = char + new_str[i+1]
        result += letter * int(num)
        num = ''
    elif char.isdigit() is True and new_str[i+1].isalpha() is True and new_str[i-1].isalpha() is True:
        num = char
        result += letter * int(num)
        num = ''

print(result)
data.close()

data = open("C:\\Users\\user\\Documents\\Python_projects\\Stepik_Python\\dataset_3363_2.txt", "w")
data.write(result)
data.close()
