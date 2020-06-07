import sys    

def change_char(s, p, r):
        return s[:p]+r+s[p+1:]

def switch_demo(argument, integer):
    switcher = {
        1: "----",
        2: "|  /",
        3: "|  \\",
        4: "----",
    }
    solution = switcher.get(argument, "Invalid value")
    if argument == 2:
       solution = change_char(solution, 1, str(integer + 1))
    return solution

def print_flags(n): 
    for x in range(0, 4):
        for i in range(0, n):
            print('{:{n}s}'.format(switch_demo(x+1, i), n = 1), end = ' ')
        print()

def main(args):
    if args.isdigit() == True:
        digit = int(args);
        if (digit > 0 and digit < 10):
            print_flags(int(args[0]))
        else:
            print("Enter digit in range: 1-9.")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Waiting for argument.")
