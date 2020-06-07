import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        operw = sys.argv[1].split()
        if len(operw) == 2:
            print(operw[1], end = ' ')
            print(operw[0])
        else:
            print("More or less then 2 words entered.")
    else:
        print("Required an argument")
