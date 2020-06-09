import sys

def check_if_bite_is_entered(string_list):
    for every_string in string_list:
        for every_char in every_string:
            if every_char == '1' or every_char == '0':
                continue
            else:
                print("It's not a bite code")
                exit(0)

def main(args):
    new_list = list()
    list_of_digits = args[1].split(',')
    check_if_bite_is_entered(list_of_digits) 
    for one_digit in list_of_digits:
        decimal_value = int(one_digit, 2)
        if (decimal_value % 5 <= 0):
            new_list.append(one_digit)
    result = ','.join(new_list)
    if result:
        print(result)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print("Please follow the instrustions: ")
        print("python3 __main__.py '0001,0011,0111,1111,0010,0100,1000,1001,1010,1100,1101,1110,1111'")

