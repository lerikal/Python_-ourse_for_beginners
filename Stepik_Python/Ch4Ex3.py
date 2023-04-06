list_num = []
dic = {}

n = int(input())

for h in range(n):
    x = int(input())
    list_num.append(x)
    if str(x) not in dic.keys():
        dic[str(x)] = f(int(x)) 

for num in list_num:
    print(dic.get(str(num)))
