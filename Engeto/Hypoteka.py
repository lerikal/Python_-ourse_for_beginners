def main():
    pujcka, urok, roky = data_input()

    r, n, mesicni_platba, celkova_suma, celkovy_urok, cislo_splatky, mesicni_urok, principal = vypocty(pujcka, urok, roky)
    sloupc_1, sloupc_2, sloupc_3, sloupc_4 = sirka_radku(pujcka, roky, celkovy_urok, mesicni_platba)

    muj_prvni_radek = prvni_radek(pujcka, roky, sloupc_1, sloupc_2, sloupc_3, sloupc_4, celkovy_urok, mesicni_platba)
    delka = len(muj_prvni_radek)
    print(muj_prvni_radek)
    print(print_line(delka))
    print(druhy_radek(sloupc_1, sloupc_2, sloupc_3, sloupc_4))
    print(print_line(delka))
    interest_vysledky, principal_vysledky, left_to_pay_vysledky = vypocety_v_tabulce(celkova_suma, mesicni_platba, r)

    a = 0
    while a < n:
        print(treti_radek(a, cislo_splatky, interest_vysledky, principal_vysledky, left_to_pay_vysledky, sloupc_1, sloupc_2, sloupc_3, sloupc_4))
        a += 1

# Vypocetni logiky

def data_input():
    pujcka = 2000000 #int(input('How much do you want to borrow?: '))  # loan
    urok = 2.09  #float(input('At what rate?: '))
    roky = 30  #int(input('How many years?: '))  # Years
    return pujcka, urok, roky

def vypocty(pujcka, urok, roky):
    r = urok / 100 / 12 # mon rate
    n = roky * 12
    mesicni_platba = round(pujcka * (r * (1 + r) ** n) / ((1 + r) ** n - 1))  # Monthly Payment
    celkova_suma = mesicni_platba * n  # Left to Pay - prvni radek
    celkovy_urok = celkova_suma - pujcka
    cislo_splatky = list(range(1, n + 1))
    mesicni_urok = celkova_suma * r  # interest v radku (1)
    principal = mesicni_platba - mesicni_urok  # Principal
    return r, n, mesicni_platba, celkova_suma, celkovy_urok, cislo_splatky, mesicni_urok, principal

def sirka_radku(pujcka, roky, celkovy_urok, mesicni_platba):
    sloupc_1 = len('Loan: ') + len(str(pujcka)) + 2
    sloupc_2 = len('Years: ') + len(str(roky)) + 2
    sloupc_3 = len('Interest: ') + len(str(int(celkovy_urok))) + 2
    sloupc_4 = len('Monthly Payment: ') + len(str(int(mesicni_platba))) + 2
    return sloupc_1, sloupc_2, sloupc_3, sloupc_4

def vypocety_v_tabulce(celkova_suma, mesicni_platba, r):
    left_to_pay_vysledky = []
    interest_vysledky = []
    principal_vysledky = []

    left_to_pay = celkova_suma

    i = 0
    while i < celkova_suma:
        left_to_pay_vysledky.append(int(left_to_pay))
        interest_vysledky.append(int(left_to_pay * r))
        principal_vysledky.append(int(mesicni_platba - (left_to_pay * r)))
        left_to_pay -= mesicni_platba
        i += mesicni_platba

    return left_to_pay_vysledky, interest_vysledky, principal_vysledky

# Formatovani tabulky
def prvni_radek(pujcka, roky, sloupc_1, sloupc_2, sloupc_3, sloupc_4, celkovy_urok, mesicni_platba):
    return '|{0:^{4}}|{1:^{5}}|{2:^{6}}|{3:^{7}}|'.format('Loan: ' + str(pujcka), 'Years: ' + str(roky),
                                                         'Interest: ' + str(int(celkovy_urok)),
                                                         'Monthly Payment: ' + str(int(mesicni_platba)), sloupc_1, sloupc_2,
                                                         sloupc_3, sloupc_4)

def print_line(delka):
    return '=' * delka

def druhy_radek(sloupc_1, sloupc_2, sloupc_3, sloupc_4):
    return '|{0:^{4}}|{1:^{5}}|{2:^{6}}|{3:^{7}}|'.format('Payment', 'Interest', 'Principal', 'Left to Pay', sloupc_1,
                                                         sloupc_2, sloupc_3, sloupc_4)

def treti_radek(a, cislo_splatky, interest_vysledky, principal_vysledky, left_to_pay_vysledky, sloupc_1, sloupc_2, sloupc_3, sloupc_4):
    return '|{0:^{4}}|{1:^{5},}|{2:^{6},}|{3:^{7},}|'.format(cislo_splatky[a], principal_vysledky[a], left_to_pay_vysledky[a], interest_vysledky[a],
                                                                   sloupc_1, sloupc_2, sloupc_3, sloupc_4)

main()
