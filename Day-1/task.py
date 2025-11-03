import os
import time
# from Logger.log import logger

def addition(number_1: int, number_2: int) -> int:
    """
    Adds two integers.

    Parameters:
    number_1 (int): The first integer.
    number_2 (int): The second integer.

    Returns:
    int: The sum of number_1 and number_2.
    """
    return number_1 + number_2


def subtraction(number_1: int, number_2: int) -> int:
    """
    Subtracts the second integer from the first.

    Parameters:
    number_1 (int): The number to subtract from.
    number_2 (int): The number to subtract.

    Returns:
    int: The result of number_1 minus number_2.
    """
    return number_1 - number_2


def multiplication(number_1: int, number_2: int) -> int:
    """
    Multiplies two integers.

    Parameters:
    number_1 (int): The first integer.
    number_2 (int): The second integer.

    Returns:
    int: The product of number_1 and number_2.
    """
    return number_1 * number_2


def division(number_1: int, number_2: int) -> float:
    """
    Divides the first integer by the second.

    Parameters:
    number_1 (int): The numerator.
    number_2 (int): The denominator (must not be zero).

    Returns:
    float: The result of number_1 divided by number_2.

    Raises:
    ZeroDivisionError: If number_2 is zero.
    """
    if number_2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return number_1 / number_2


def get_valid_choice() -> int | None:
    """
    Prompts the user to enter a valid operation choice (1 to 5).

    Returns:
    int: A valid choice entered by the user.
    """
    while True:
        print("\nChoose Operation")
        print("1 -> Addition")
        print("2 -> Subtraction")
        print("3 -> Multiplication")
        print("4 -> Division")
        print("5 -> Exit")
        choice_input = input("Enter Your Choice => ").strip() ##string.. => "1"

        if not choice_input.isdigit():
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        choice = int(choice_input)
        if choice in range(1, 6):
            return choice
        else:
            print("Invalid choice! Please select a number from 1 to 5.")


def get_integer_input(prompt: str) -> int:
    """
    Prompts the user to enter an integer.

    Parameters:
    prompt (str): The message shown to the user.

    Returns:
    int: The validated integer input.
    """
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Input cannot be empty. Please enter a number.")
            continue
        try:
            return int(value)
        except ValueError:
            print("Invalid input! Please enter an integer.")



def perform_operation(choice: int, number_1: int, number_2: int) -> None:
    """
    Performs and displays the result of the selected arithmetic operation using match-case.

    Parameters:
    choice (int): The operation choice selected by the user.
    number_1 (int): The first number.
    number_2 (int): The second number.
    """
    try:
        match choice:
            case 1:
                result = addition(number_1, number_2)
                print(f"Result (Addition): {result}")
            case 2:
                result = subtraction(number_1, number_2)
                print(f"Result (Subtraction): {result}")
            case 3:
                result = multiplication(number_1, number_2)
                print(f"Result (Multiplication): {result}")
            case 4:
                result = division(number_1, number_2)
                print(f"Result (Division): {result}")
            case _:
                print("Invalid operation selected.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")


def clear_screen(delay_seconds: int = 3) -> None:
    """
    Waits for a few seconds, then clears the terminal screen.

    Parameters:
    delay_seconds (int): Number of seconds to wait before clearing the screen.
    """
    print(f"\nClearing screen in {delay_seconds} seconds...")
    time.sleep(delay_seconds)
    os.system('cls' if os.name == 'nt' else 'clear')


def main() -> None:
    """
    Main function to run the calculator application.
    """
    while True:
        print("Welcome to the Calculator Application!")
        choice = get_valid_choice()

        if choice == 5:
            print("Thanks for using the application. Goodbye!")
            break

        number_1 = get_integer_input("Enter first number => ")
        number_2 = get_integer_input("Enter second number => ")

        perform_operation(choice, number_1, number_2)

        clear_screen()


if __name__ == '__main__':
    main()
