#a, b = (int(i) for i in input().split())

a = int(input())
b = int(input())
sum = 0
count = 0

for num in range(a, b+1):
    if num % 3 == 0:
        sum += num
        count += 1

print(sum/count)