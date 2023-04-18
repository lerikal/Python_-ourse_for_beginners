data = open(f'C:\\Users\\uzivatel\\PycharmProjects\pythonProject\\Engeto\\dataset_3380_5.txt', 'r')
data = data.readlines()

# create dictionaries
pupils = {}
height = {}
for i in range(1, 12):
    pupils[i] = 0
    height[i] = 0

# full data from dataset to dictionaries
for line in data:
    line = line.replace('\n', '').split()
    pupils[line[0]] += 1
    height[line[0]] += int(line[-1])

# print results for every year
for year in range(1, 12):
    if pupils.get(year) == 0:
        print(year, '-')
    else:
        result = float(height.get(str(year)) / pupils.get(str(year)))
        print(year, result)
