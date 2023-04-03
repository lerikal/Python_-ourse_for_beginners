lst = [int(i) for i in input().split()]
x = int(input())

if x not in lst:
    print('Отсутствует')
else:
    for i, num in enumerate(lst):
        if num == x:
            print(i, end=' ')
    print()


# put your python code here
lst = [int(i) for i in input().split()]
x = int(input())
indx = 0

if x not in lst:
    print('Отсутствует')
else:
    for num in lst:
        if num == x:
            print(indx, end=' ')
        indx += 1