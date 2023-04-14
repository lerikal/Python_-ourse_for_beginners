import requests

data = open("C:\\Users\\valer\\Documents\\Python_projects\\Stepik_Python\\dataset_3378_3.txt", "r")
data_set = data.readlines()

url = ''
for line in data_set:
    url = line.replace('\n', '')

response = requests.get(url)

while response.status_code == 200:
    if not response.text.startswith('We'):
        url = 'https://stepic.org/media/attachments/course67/3.6.3/' + response.text
        response = requests.get(url)
    else:
        print(response.text)
        break
