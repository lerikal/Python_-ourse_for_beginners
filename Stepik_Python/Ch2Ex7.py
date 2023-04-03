str_input = str(input())
new_str = ''
count = 1

for char in str_input:
    if len(new_str) == 0:
        new_str += char
    elif char == new_str[-1]:
        count += 1
    else:
        new_str = new_str + str(count) + char 
        count = 1

new_str += str(count)
print(new_str)
