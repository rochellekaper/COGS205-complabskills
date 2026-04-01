import math

def square_root_manual(number):
    '''this function takes in a number & returns the square root of manually'''

    return (number)**0.5


def validate_manual_square_root(number):
    '''this function takes in a number to compare whether the manual square root function is equal to the python sqrt function, and returns TRUE 
    if yes, FALSE is not'''
    square_root_to_test = square_root_manual(number)

    if square_root_to_test == math.sqrt(number):
        return "TRUE"
    else:
        return "FALSE"
    

if __name__ == "__main__":
    numb = input("enter a number you want the square root of: ")
    print(validate_manual_square_root(float(numb)))
