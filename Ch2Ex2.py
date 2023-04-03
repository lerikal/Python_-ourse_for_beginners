a = int(input())
b = int(input())
i = 1

while i % a != 0 or i % b != 0:
    i += 1

print(i)