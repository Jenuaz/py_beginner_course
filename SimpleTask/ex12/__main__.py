import sys

def check_input_int(args):
    for x in args:
        if x.isdigit():
            continue
        else:
            print("Please enter the digit.")
            exit(0)

def inputinonerow(args):
    if len(args) == 3:
        args.sort()
        print(args[1])
    else:
        print("Enter three digits! Separated by ' '")


def main():
    i = 0
    tmp = list()
    while i < 3:
        tmp.append(input("Enter " + str(i + 1) +" digit: "))
        i += 1
    check_input_int(tmp)
    tmp.sort()


if len(sys.argv) == 2:
    print("Option")
    if sys.argv[1] == '-separate':
        main()
if len(sys.argv) == 1:
    list_of_input = input("Please ented 3 digits in the same row sep. by ' ': ")
    material_to_check = list_of_input.split(' ')
    check_input_int(material_to_check)
    inputinonerow(material_to_check)
else:
    print("Follow the rules of running the program: ")
    print("python3 __main__.py or you can use flag and run as: python3 __main__.py -separate")
