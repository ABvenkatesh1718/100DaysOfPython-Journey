def addition(number_1: int, number_2: int) -> int:
    """
    Calculate the sum of two integers.

    Parameters:
    number_1 (int): The first number to add.
    number_2 (int): The second number to add.

    Returns:
    int: The result of number_1 + number_2.
    """
    return number_1 + number_2

def multiplication(number_1: int, number_2: int) -> int:
    """
    Calculate the product of two integers.

    Parameters:
    number_1 (int): The first number to multiply.
    number_2 (int): The second number to multiply.

    Returns:
    int: The result of number_1 * number_2.
    """
    return number_1 * number_2

def division(number_1: int, number_2: int) -> float:
    """
    Divide the first integer by the second.

    Parameters:
    number_1 (int): The numerator.
    number_2 (int): The denominator (must not be zero).

    Returns:
    float: The result of number_1 / number_2.

    Raises:
    ZeroDivisionError: If number_2 is zero.
    """
    return number_1 / number_2

def substraction(number_1: int, number_2: int) -> int:
    """
    Subtract the second integer from the first.

    Parameters:
    number_1 (int): The number to subtract from.
    number_2 (int): The number to subtract.

    Returns:
    int: The result of number_1 - number_2.
    """
    return number_1 - number_2

if __name__ == '__main__':
    while True:
        print("Choose Operation")
        print("1 -> Addition")
        print("2 -> Subtraction")
        print("3 -> Multiplication")
        print("4 -> Division")
        print("5 -> Exit")

        choice=int(input("Enter Your Choice =>"))
        if choice not in [1,2,3,4,5]:
            print("Invalid Choice , pls Enter Choice Number Properly")
            continue
        try:
            number_1=int(input("Enter first Number =>"))
            number_2=int(input("Enter Second Number =>"))
        except ValueError as e:
            print("Invalid input! Please Enter Integers Only..")
            continue
        match choice:
            case 1:
                add=addition(number_1,number_2)
                print(f"Addition of Two Numbers:{add}")
            case 2:
                sub=substraction(number_1,number_2)
                print(f"Substraction of Two Numbers:{sub}")
            case 3:
                mul=multiplication(number_1,number_2)
                print(f"Multiplication of Two Numbers:{mul}")
            case 4:
                div=division(number_1,number_2)
                print(f"Division of Two Numbers:{div}")
            case 5:
                print("Thanks for using application , Bye..")
                break