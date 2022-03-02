import string


def poem_specifices():
    vowels = 'aeuio'
    consonants = string.ascii_lowercase
    white_spaces = string.whitespace
    poem_list = []

    how_many_lines = int(input('How many lines will there be? '))
    for line in range(how_many_lines):
        poem_list.append(input('input your line here: '))

    my_dict = {}
    for num, line in enumerate(poem_list):
        my_dict[str('line' + str(num + 1) + ' vowels:')] = 0
        my_dict[str('line' + str(num + 1) + ' consonants:')] = 0
        for char in line.lower():
            if char in white_spaces:
                continue
            elif char in vowels:
                my_dict[str('line' + str(num + 1) + ' vowels:')] += 1
            elif char in consonants:
                my_dict[str('line' + str(num + 1) + ' consonants:')] += 1
        number_of_vowels = sum([v for k, v in my_dict.items() if 'vowels' in k])
        number_of_consonants = sum([v for k, v in my_dict.items() if 'consonants' in k])
    return how_many_lines, number_of_vowels, number_of_consonants, my_dict


x = poem_specifices()
print('output the number of lines:', x[0])
print('Number of vowels:', x[1])
print('Number of consonants:', x[2])
for k, v in x[3].items():
    print(k, v)
