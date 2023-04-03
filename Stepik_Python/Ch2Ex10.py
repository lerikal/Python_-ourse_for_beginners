list_num = [int(i) for i in input().split()]
list_num.sort()
result = []

for num in list_num:
    if list_num.count(num) > 1 and num not in result:
        result.append(num)
        print(num, ' ', end='')


numbers = [int(i) for i in input().split()]
lst = []
for num in numbers:
    if numbers.count(num) > 1 or num not in lst:
        lst.append(num)
        print(num, end=' ')
       