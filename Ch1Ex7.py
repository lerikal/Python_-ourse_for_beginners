ticket = str(input())
list_num = []

for i in ticket:
    list_num.append(int(i))

if sum(list_num[:3]) == sum(list_num[3:]):
    print('Счастливый')
else:
    print('Обычный')
