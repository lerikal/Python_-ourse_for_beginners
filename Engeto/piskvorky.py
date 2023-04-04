def main():
    line()
    print("Welcome to Tic Tac Toe\nGAME RULES:\nEach player can place one mark (or stone) per turn on the 3x3 grid\n"
          "The WINNER is who succeeds in placing three of their marks in a\n* horizontal,\n* vertical or\n"
          "* diagonal row\nLet's start the game")
    cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print(area(cells))
    winner = game(cells)
    final_print(cells, winner)

def line():
    print('=' * 45)

def area(cells):
    return '------\n{}|{}|{}\n------\n{}|{}|{}\n------\n{}|{}|{}\n------'.format(cells[0], cells[1], cells[2],
                                                                                  cells[3], cells[4], cells[5],
                                                                                  cells[6], cells[7], cells[8])

def users(player):
    if player == 'x':
        return 'o'
    elif player == 'o':
        return 'x'

def input_move_num(player, cells):
    while True:
        move_num = input('Player {} | Please enter your move number: '.format(player))
        if move_num.isnumeric() and int(move_num) in range(1, 10) and cells[int(move_num) - 1] == ' ':
            return int(move_num)
        else:
            print('Your move is not correct. Try one more time.')

def move(cells, player, move_num):
    cells.pop(move_num - 1)
    cells.insert(move_num - 1, player)
    return cells

def game(cells):
    player = 'x'
    cond = True
    while cond == True and cells.count(' ') != 0:
        player = users(player)
        line()
        move_num = input_move_num(player, cells)
        line()
        line()
        cells = move(cells, player, move_num)
        if cells.count(player) > 2:
            cond = condition(cells, player)
        print(area(cells))
    return player

def condition(cells, player):
    i = 0
    while True and i < len(cells) - 1:
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        if cells[wins[i][0]] == player and cells[wins[i][1]] == player and cells[wins[i][2]] == player:
            return False
        else:
            i += 1
    return True

def final_print(cells, player):
    if cells.count(' ') == 0:
        print('Game over')
    else:
        print('Congratulations, the player {} WON!'.format(player))

main()