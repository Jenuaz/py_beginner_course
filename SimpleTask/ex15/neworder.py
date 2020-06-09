def special_order():
    first_input = input("Enter the first input, which are digits: ")
    second_input = input("Enter the second input, which are letters: ")
    sep_f = first_input.split(' ')
    sep_s = second_input.split(' ')
    new_list = list()
    if len(sep_f) == len(sep_s):
        i = 0
        while i < len(sep_f):
            new_list.append(sep_f[i])
            new_list.append(sep_s[i])
            i += 1
    else:
        print("Different lens.")
    print(*new_list, sep=' ')

special_order()

