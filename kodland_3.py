def ask_of_coordinates():
    user_coordinates = []
    for i in range(4):
        x = int(input('give coordinate no.'+str(i+1) + ' (x1, y1, x2, y2): '))
        while 1 > x or x > 8:
            x = int(input('wrong coordinate, try once again with that: '))
        user_coordinates.append(x)
    return user_coordinates[:]



def possible_in_one_move(coordinates):
    x1, y1 = coordinates[:2]
    x2, y2 = coordinates[2:]
    if y2 - y1 == x2 - x1 or 1 == x2 or y1 == y2:  # skos 1, 1, 2, 2
        return 'YES'
    return 'NO'


list_of_coordinates = ask_of_coordinates()
print(possible_in_one_move(list_of_coordinates))
