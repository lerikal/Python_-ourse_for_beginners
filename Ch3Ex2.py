def modify_list(l):
    i = len(l)
    n_num = 0
    i_num = -1

    while n_num < i:
        if l[i_num] % 2 == 0:
            l.append(l[i_num]//2)
            i_num -= 1
        
        l.pop(i_num)
        n_num += 1

    l.reverse()

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]