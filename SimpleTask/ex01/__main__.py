import sys

def cust_len(ourline):
    length = 0;
    for one_letter in ourline:
        length += 1
    
    return length

def main(args):
    print(cust_len(args))
    print(len(args))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Enter value please. Only 2 arguments are available.")
