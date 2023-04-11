data = open("C:\\Users\\user\\Documents\\Python_projects\\Stepik_Python\\dataset_3363_4.txt", "r")
data_set = data.readlines()

list_for_result = []

# for avarage grades
math_grades = 0
physics_grades = 0
rus_grades = 0
n_student = 0

new_str = ''
lst_from_line = []

for line in data_set:
    new_str = line.replace('\n', '')
    lst_from_line = new_str.split(';')

    avg_per_student = 0
    avg_per_student = (int(lst_from_line[1]) + int(lst_from_line[2]) + int(lst_from_line[3])) / 3

    math_grades += int(lst_from_line[1])
    physics_grades += int(lst_from_line[2])
    rus_grades += int(lst_from_line[3])
    n_student += 1
    
    list_for_result.append(avg_per_student)

data = open("C:\\Users\\user\\Documents\\Python_projects\\Stepik_Python\\dataset_3363_4.txt", "w")
students = 0
for avg in list_for_result:
    data.write(str(avg))
    data.write('\n')
    students += 1
    if students == len(list_for_result):
        data.write(str(math_grades/n_student))
        data.write(' ')
        data.write(str(physics_grades/n_student))
        data.write(' ')
        data.write(str(rus_grades/n_student))
        data.write(' ')

data.close()
