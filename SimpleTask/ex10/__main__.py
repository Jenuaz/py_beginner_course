import sys

def review_inserted_data(digitslist):
    for digit in digitslist:
        if digit.isdigit() != True:
            print("We accept only digits in input")
            exit(0)

def create_list_with_result(listofdigits_one, listofdigits_two):
    noduplicateslistone = list(set(map(int, listofdigits_one)))
    noduplicateslisttwo = list(set(map(int, listofdigits_two)))
    resultlist = list(set(noduplicateslistone).intersection(set(noduplicateslisttwo)))
    resultlist.sort()
    print(resultlist)


def main(args):
    ourListRowOne = args[1].split(', ')
    ourListRowTwo = args[2].split(', ') 
    review_inserted_data(ourListRowOne)
    review_inserted_data(ourListRowTwo)
    create_list_with_result(ourListRowOne, ourListRowTwo)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv)
    else:
        print("Please follow the instrustions: ")
        print("To run program enter 2 arguments and run program like this: ")
        print("python3 __main__.py '3, 5, 2, 8, 1, 34, 13, 21, 1, 55, 100, 99, 88, 77, 66' '77, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13'")  
