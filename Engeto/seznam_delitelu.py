start_point = int(input('START POINT: '))
end_point = int(input('END POINT: '))

def main(start_point, end_point):
    seq = list(range(start_point, end_point + 1))
    divisor = list(range(2, 10))
    n_divided = []
    for div in divisor:
        n_divided.append(num_dev_str(seq, div))

    # tisk tabulky
    sirka_sloupce_1 = len('Divisor') + 2
    if len('Numbers Divided') + 2 < len(n_divided[0]) + 2:
        sirka_sloupce_2 = len(n_divided[0]) + 2
    else:
        sirka_sloupce_2 = len('Numbers Divided') + 2
    print('|{0:^9}|{1:^{2}}|'.format('Divisor', 'Numbers Divided', sirka_sloupce_2))
    print('=' * (sirka_sloupce_1 + sirka_sloupce_2 + 3))
    i = 0
    while i < len(divisor):
        print('|{0:^9}|{1:^{2}}|'.format(divisor[i], n_divided[i], sirka_sloupce_2))
        i += 1

def num_dev_str(seq, div):
    list_num_dev = ''
    for num in seq:
        if num % div == 0:
            list_num_dev = list_num_dev + str(num) + ', '
    list_num_dev = list_num_dev[:-2]
    return list_num_dev

main(start_point, end_point)