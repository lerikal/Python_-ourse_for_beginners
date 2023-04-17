def main():
    n = int(input())
    data = game_results(n)
    lst_of_teams = list_of_teams(data)
    games_count = games_counter(data, lst_of_teams)
    results = win_counter(data, games_count)
    final_results = total_results(results)

    for key, value in final_results.items():
        print((key + ':'), *value, end='\n')

def game_results(n):
    data = []
    while n > 0:
        str_input = str(input())
        data.append(str_input.split(';'))
        n -= 1
    return data

def list_of_teams(data):
    lst_of_teams = set()
    for game in data:
        lst_of_teams.add(game[0])
        lst_of_teams.add(game[2])

    return lst_of_teams

def games_counter(data, lst_of_teams):
    lst_teams = []
    for game in data:
        for i in game:
            if i.isdigit() is not True:
                lst_teams.append(i)

    results_total = {}
    for team in lst_of_teams:
        results_total[team] = [lst_teams.count(team)]

    return results_total

def win_counter(data, games_count):
    wins_count = games_count
    for team in wins_count:
        wins_count.get(team).append(0)
        wins_count.get(team).append(0)
        wins_count.get(team).append(0)
        wins_count.get(team).append(0)

    for game in data:
        if int(game[1]) > int(game[3]):
            winner = game[0]
            loser = game[2]
            wins_count.get(winner)[1] += 1
            wins_count.get(loser)[3] += 1
        elif int(game[1]) < int(game[3]):
            winner = game[2]
            loser = game[0]
            wins_count.get(winner)[1] += 1
            wins_count.get(loser)[3] += 1
        elif int(game[1]) == int(game[3]):
            wins_count.get(game[0])[2] += 1
            wins_count.get(game[2])[2] += 1

    return wins_count

def total_results(results):
    tab = results
    for key in results.keys():
        tab.get(key)[-1] = (3 * int(tab.get(key)[1])) + int(tab.get(key)[2])

    return tab

main()
