import requests

# receiving url from text
data = open("C:\\Users\\user\\Documents\\Python_projects\\Stepik_Python\\dataset_3378_2.txt", "r")
data_set = data.readlines()

url = ''
for line in data_set:
    url = line.replace('\n', '')

# counting lines in received file
response = requests.get(url)
print(response.text.count('\n'))
