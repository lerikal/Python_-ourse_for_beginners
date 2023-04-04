import random

def main():
    random_num = num_generator()
    print("Hi there!\nI've generated a random 4 digit number for you.\nLet's play a bulls and cows game.\nEnter a number")
    tips = 1
    while tips < 4:
        user_num = num_input()
        if random_num == user_num:
            break
        N_bulls, N_cows = bulls_cows(random_num, user_num)
        print(str(N_bulls) + ' bull' + plural(N_bulls) + str(N_cows) + ' cow' + plural(N_cows))
        tips += 1
    print(score(random_num, user_num, tips))

def num_generator():
    random_num = set()
    while len(random_num) < 4:
        random_num.add(random.randrange(1, 10))
    return list(random_num)

def num_input():
    while True:
        user_input = input()
        if len(set(user_input)) == 4 and user_input.isnumeric():
            return list(map(int, user_input))
        else:
            print('Try one more time')

def bulls_cows(random_num, user_num):
    N_bulls, N_cows = 0, 0
    i = 0
    for num in user_num:
        if num == random_num[i]:
            N_bulls += 1
        elif num in random_num:
            N_cows += 1
        i += 1
    return N_bulls, N_cows

def plural(cislo):
    if cislo != 1:
        return 's '
    else:
        return ' '

def score(random_num, user_num, tips):
    if random_num == user_num:
        return "Correct, you've guessed the right number in {} guesses!".format(tips)
    else:
        return "That's not so good"

main()