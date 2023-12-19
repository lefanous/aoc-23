import pprint
with open('_2_input.txt', 'r') as file:
    input = file.read().strip()
    
# input example
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue

# turn into dict, where key is game number and value is dict of colors and their counts
# {'1': [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]}

bag = {'blue': 14, 'green': 13, 'red': 12}

games = {}
for game in input.split('\n'):
    game_number, colors = game.split(': ')
    game_number = game_number.split(' ')[1]
    games[game_number] = {}
    
    color_sets = colors.split('; ')
    color_sets = [color.split(', ') for color in color_sets]
    
    draws = []
    for color_set in color_sets:
        color_dict = {}
        for color in color_set:
            color = color.split(' ')
            
            color_dict[color[1]] = int(color[0])
        draws.append(color_dict)
    
    games[game_number] = draws
    
# pprint.pprint(games)

possible_games = []

for game_number, draws in games.items():
    possible = True
    for draw in draws:
        for color, count in draw.items():
            if count > bag[color]:
                possible = False
                break
    
    if possible:
        possible_games.append(game_number)
            
sum_of_possible_games = sum([int(game) for game in possible_games])
print(sum_of_possible_games)
                
