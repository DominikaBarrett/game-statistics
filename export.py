# Export functions

def all_games_data(file_name):
    file = open(file_name,'r')
    lines = file.readlines()
    result = []
    for i in lines:
        result.append(i.split('\t'))
    return result

all_games_data('game_stat.txt')
