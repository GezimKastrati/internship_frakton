def even_first_odd_second(lst, const=0):
    if const == 0:
        const = int(len(lst)/2)

    if len(lst) <= const:
        return lst

    if lst[0] % 2 == 0:
        return [lst[0]] + even_first_odd_second(lst[1:], const)
    else:
        return even_first_odd_second(lst[1:] + [lst[0]], const)


input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("INPUT LIST:")
print(input_list)
print("OUTPUT LIST:")
print(even_first_odd_second(input_list))
