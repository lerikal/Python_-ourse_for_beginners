num = int(input())
result = ''
i = 1
while i <= num:
    result += str(i)  * i
    i +=1
print(*result[:num])


a = int(input())
i = 1
lst = ''
while i <= a:
    lst += (str(i) + ' ') * i
    i += 1
print(*lst.split()[:a])