
# student : Dipede Carlotta
# student number :201537058


main_program = True
# creating the main menu for the user - function


def program():
    print('Hello user, please enter a value to choose an option')
    print('select 1 to find the sum of two numbers')
    print('2 to find the product')
    print('3 to raise a number to a power')
    print('4 to find the remainder,')
    print('q to exit the program')

    # designing the output of each choice in the main menu
    choice = input('human,please enter a value: ')

    """
    creating conditional path( with empty variables , yet )
    for the program to perform specific tasks by travelling through users imput
    """
    global main_program

    while main_program:
        if(choice == '1'):
            sum_numbers()
        elif(choice == '2'):
            product_of_numbers(*get_info())
        elif(choice == '3'):
            esponent_of_numbers(*get_info())
        elif(choice == '4'):
            remainder_of_numbers(*get_info())
        elif(choice == 'q'):
            print('program terminated, Bye')
            main_program = False
        else:
            print('you have entered an unvalid option')


# Defiing a function,
# to prompt the user and avoid repetition of codes


def get_info():
    while True:
        try:
            x = float(input('Human, enter the first value: '))
            y = float(input('Human, enter the second value: '))
            return x, y
        except ValueError:
            print('my processor cannot understand the input')


# Sum of numbers

def sum_numbers():
    while True:
        try:
            x, y = get_info()
            Sum = x + y
            print(Sum)
            break
        except ValueError:
            print('Unvalid Option, ejecting User from the system in 4 3 2 ..')

    program()


# Defining function - Product of Two Numbers
def product_of_numbers(x, y):

    # recursive function to calculate
    # multiplication of two numbers

    if (x < y):
        return product_of_numbers(x, y)
    if(x == 0):
        return 0
    return x + product_of_numbers(x, y-1)


program()

# recursive function
# multiplication of two numbers


def esponent_of_numbers(x, y):
    if y == 0:
        print(1)
    elif y % 2 == 0:
        print(esponent_of_numbers(x, y / 2)**2)
    else:
        print(x * esponent_of_numbers(x, y-1))


program()


# remainder of numbers- # parameters : x et y (integers)

def remainder_of_numbers(x, y):
    if x < y:
        print(x)
    print(remainder_of_numbers(x - y, y))


program()
