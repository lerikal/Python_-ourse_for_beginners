print('-' * 40)
users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

print('Welcome to the app. Please log in:')
username = input('USERNAME: ')
password = input('PASSWORD: ')

while username:
    if users.get(username) == password:
        print('Login was successful')
        break
    else:
        print('Username or password is not correct')
        username = input('USERNAME: ')
        password = input('PASSWORD: ')

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

print('We have 3 texts to be analyzed.')
number = input('Enter a number btw. 1 and 3 to select: ')

while number.isalpha() == True or int(number) < 1 or int(number) >= 4:
    print('Number is not correct')
    number = input('Enter a number btw. 1 and 3 to select: ')

print('-' * 40)

# tvorba indexu po volbe izivatele
n_of_text = int(number) - 1
text_list = TEXTS[n_of_text].split()

# počet slov
pocet_slov = len(text_list)
print('There are', pocet_slov, 'words in the selected text.')

# počet slov začínajících velkým písmenem
# počet slov psaných velkými písmeny
# počet slov psaných malými písmeny
# počet čísel (ne cifer!)

pocet_slov_velke_pismo = 0
pocet_slov_caps = 0
pocet_slov_mala_pismena = 0
pocet_cisel = 0

for slovo in text_list:
    if slovo.istitle():
        pocet_slov_velke_pismo += 1
    elif slovo.isupper():
        pocet_slov_caps += 1
    elif slovo.islower():
        pocet_slov_mala_pismena += 1
    elif slovo.isnumeric():
        pocet_cisel += 1

print('There are', pocet_slov_velke_pismo, 'titlecase words.')
print('There are', pocet_slov_caps, 'uppercase words')
print('There are', pocet_slov_mala_pismena, 'lowercase words')
print('There are', pocet_cisel, 'numeric strings')

print('-' * 40)

# sloupcový graf

pocet_znaku = []  # list s poctem znaku jednotlivych slov

text_string = TEXTS[n_of_text].replace('.', '').replace(',', '').split()

for word in text_string:
    delka_slova = len(word)
    pocet_znaku.append(delka_slova)

pocet_znaku_set = set(pocet_znaku)  # unikantni prvky

for sloupec in pocet_znaku_set:
    n = pocet_znaku.count(sloupec)  # pocet vyskytu
    print(sloupec, n * '*', n)

print('-' * 40)

# součet všech čísel (ne cifer!) v textu

cisla_z_textu = []  # list cisel

for num in text_list:
    if num.isnumeric():
        cisla_z_textu.append(float(num))

print('If we summed all the numbers in this text we would get: ', sum(cisla_z_textu))

print('-' * 40)
