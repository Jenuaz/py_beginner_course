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

#print (sys.argv)
#var = input("Please enter something: ")
#print("You entered: " + var)import sys

#try:
#     parser = argparse.ArgumentParser()
#     parser.add_argument("square", help="display a square of a given number",
#                type=int)
#    args = parser.parse_args()
#
#    #print the square of user input from cmd line.
#    print args.square**2
#
#    #print all the sys argument passed from cmd line including the program name.
#    print sys.argv
#
#    #print the second argument passed from cmd line; Note it starts from #ZERO
#    print sys.argv[1]
#except:
#    e = sys.exc_info()[0]
#    print e
