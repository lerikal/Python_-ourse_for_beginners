def to_roman(cislo):
    roman = ''
    arabic_1 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    arabic_10 = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    arabic_100 = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    arabic_1000 = ['', 'M', 'MM', 'MMM']
    if len(str(cislo)) == 1:
        roman += arabic_1[cislo]
    elif len(str(cislo)) == 2:
        roman += arabic_10[int(str(cislo)[0])] + arabic_1[int(str(cislo)[1])]
    elif len(str(cislo)) == 3:
        roman += arabic_100[int(str(cislo)[0])] + arabic_10[int(str(cislo)[1])] + arabic_1[int(str(cislo)[2])]
    elif len(str(cislo)) == 4 and cislo in range(1000, 4000):
        roman += arabic_1000[int(str(cislo)[0])] + arabic_100[int(str(cislo)[1])] + arabic_10[int(str(cislo)[2])] + \
                 arabic_1[int(str(cislo)[3])]
    return roman

print(to_roman(3999))

def to_arab(str):
    slovnik = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    res = []
    for i in str:
        res.append(slovnik[i])

    right_cis = []
    for cis in res:
        if len(res) < 2:
            right_cis.append(cis)
            break
        elif cis < res[res.index(cis)+1]:
            nove_cislo = res[res.index(cis)+1] - cis
            right_cis.append(nove_cislo)
            res.remove(res[res.index(cis)+1])
        else:
            right_cis.append(cis)
    return sum(right_cis)

print(to_arab('I'))
