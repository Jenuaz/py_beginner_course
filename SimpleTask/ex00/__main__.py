import sys

def magic_function(stringelement):
    first_letter = stringelement[0]
    stringelement = stringelement.replace(first_letter, '*')
    stringelement = first_letter + stringelement[1:]

    return stringelement

def main(args):
    i = 0;
    ourline = args[1].split()
    counts = len(ourline)
    for tmp in ourline:
        print(magic_function(tmp) + ' ')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print("Only 2 arguments allowed! \n First argument is a name of our program. \n Second argument is our string which we will handle.")
