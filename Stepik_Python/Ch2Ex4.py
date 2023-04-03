a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a <= 10 and b <= 10 and c <= 10 and d <= 10 and a <= b and c <= d:
    for row in range(a - 1,b + 1):
        for cell in range(c - 1, d + 1):
            if row == a - 1:
                if cell != d:
                    print('\t', cell + 1, end='')                    
            else:
                if cell == c - 1:
                    print(row, end='')
                else:
                    print('\t', row * cell, end='')
        print()


def main():
    a, b, c, d = inputs()
    print(first_line(c, d))
    for i in range(a, (b + 1)):
        print(str(i) + '\t' + str(print_tab(i, c, d)))

def inputs():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    return a, b, c, d

def first_line(c, d):
    header = '\t'
    for name in range(c, (d + 1)):
        header += str(name) + '\t'
    return header

def print_tab(i, c, d):
    row = ''
    for cis in range(c, (d + 1)):
        cell = i * cis
        row += str(cell) + '\t'
    return row

main()