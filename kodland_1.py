input_list = [4, 0, 5, 0, 3, 0, 0, 5]


def shrink(list_of_integer):
    non_zero_list = []
    zero_list = []
    [non_zero_list.append(num) if num > 0 else zero_list.append(num) for num in list_of_integer]
    return non_zero_list + zero_list


print(shrink(input_list))
