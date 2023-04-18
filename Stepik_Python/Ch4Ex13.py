n_moves = int(input())
x, y = 0, 0

for i in range(n_moves):
    move = [i for i in input().split()]
    if move[0] == 'север':
        y += int(move[-1])
    elif move[0] == 'юг':
        y -= int(move[-1])
    elif move[0] == 'запад':
        x -= int(move[-1])
    elif move[0] == 'восток':
        x += int(move[-1])

print(x, y)
