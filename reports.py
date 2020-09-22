def all_games_data(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    result = []
    for i in lines:
        result.append(i.split('\t'))
    for i in result:
        i[1] = float(i[1])
        i[2] = int(i[2])
    return result


def alfa_sort(to_sort):
    x = len(to_sort)
    for i in range(x):
        for j in range(0,x-i-1):
            if to_sort[j] > to_sort[j+1]:
                to_sort[j] ,to_sort[j+1]  = to_sort[j +1],to_sort[j]
    return to_sort




def count_games(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    i = 0
    for _ in lines:
        i += 1
    return i


print(count_games('game_stat.txt'))


def decide(file_name, year):
    lines = all_games_data(file_name)
    for i in lines:
        if i[2] == year:
            return True
    return False


print(decide('game_stat.txt', 2000))


def get_latest(file_name):
    lines = all_games_data(file_name)
    latest = [0, 0, 0]
    for i in lines:
        if i[2] > latest[2]:
            latest = i
    return latest[0]


print(get_latest('game_stat.txt'))


def count_by_genre(file_name, genre):
    lines = all_games_data(file_name)
    gen = 0
    for i in lines:
        if i[3] == genre:
            gen += 1
    return gen


print(count_by_genre('game_stat.txt', ''))


def get_line_number_by_title(file_name, title):
    lines = all_games_data(file_name)
    line_num = 1
    for i in lines:
        if title == i[0]:
            break
        line_num += 1
    return line_num


print(get_line_number_by_title('game_stat.txt', 'Populous'))


def sort_abc(file_name):
    lines = all_games_data(file_name)
    titels = [i[0] for i in lines]
    return alfa_sort(titels)



print(sort_abc("game_stat.txt"))

def get_genres(file_name):
    lines = all_games_data(file_name)
    genre = []
    for i in lines:
        if not i[3] in genre:
            genre.append(i[3])
    return alfa_sort(genre)



# TODO sortowanie wlasnej roboty

print(get_genres('game_stat.txt'))


def when_was_top_sold_fps(file_name):
    lines = all_games_data(file_name)
    top_sold = [0, 0, 0]
    for i in lines:
        if (i[3] == 'First-person shooter') and (i[1] > top_sold[2]):  # zdanie logiczne
            top_sold = i
    if top_sold[2] == 0:
        raise ValueError
    return top_sold[2]


print(when_was_top_sold_fps('game_stat.txt'))
