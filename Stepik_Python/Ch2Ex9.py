list_num = [int(i) for i in input().split()]
result = ''

for i, num in enumerate(list_num):
    if len(list_num) == 1:
        result += str(num)
    elif i == 0:
        result += str(list_num[1] + list_num[-1]) + ' '
    elif i == len(list_num)-1:
        result += str(list_num[-2] + list_num[0])
    else:
        result += str(list_num[i-1] + list_num[i+1]) + ' '

print(result)


# put your python code here
seq = input().split(' ')
res = ''
i = 0
while i in range(len(seq)):
    if len(seq) == 1:
        res += seq[0] + ' '
        break
    elif i == 0:
        res += str(int(seq[-1]) + int(seq[1])) + ' '
        i += 1
    elif i == len(seq)-1:
        res += str(int(seq[-2]) + int(seq[0]))
        i += 1
    else:
        res += str(int(seq[i-1]) + int(seq[i+1])) + ' '
        i += 1
print(res)
