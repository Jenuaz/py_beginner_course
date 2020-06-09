#To run function without main. Run python3
#>>import sort
#>>from sort import two_digit_string_comb
#>>two_digit_stirng_comb()


def check_if_digit(args):
    for x in args:
        if x.isdigit():
            continue
        else:
            print("Please enter the digit.")
            exit(0)


def two_digit_string_comb():
    first_row_digits = input("Enter digits 1 line: ")
    second_row_digits = input("Enter digits second line: ")
    splitted_result_one = first_row_digits.split(' ')
    splitted_result_two = second_row_digits.split(' ')
    combo = splitted_result_one + splitted_result_two
    check_if_digit(combo)
    intmaterial_list = list(map(int, combo))
    intmaterial_list.sort()
    print(intmaterial_list)
    return intmaterial_list
