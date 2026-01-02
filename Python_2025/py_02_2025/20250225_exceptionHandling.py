class CustomError(Exception):
    """Custom exception class."""
    def __init__(self, message):
        super().__init__(message)


def divide_numbers(a, b):
    """Function that divides two numbers."""
    try:
        # Try to divide numbers and may raise ZeroDivisionError
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: Cannot divide by zero! ({e})")
        return None
    except TypeError as e:
        print(f"Error: Invalid input type! ({e})")
        return None
    else:
        print(f"The result of {a} divided by {b} is {result}")
        return result
    finally:
        print("Finished attempting to divide the numbers.")


def read_file(filename):
    """Function to read the content of a file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"Error: File not found! ({e})")
        return None
    except IOError as e:
        print(f"Error: Problem reading the file! ({e})")
        return None
    else:
        print(f"File content:\n{content}")
        return content
    finally:
        print("Finished attempting to read the file.")


def main():
    # Test the divide_numbers function with various inputs
    divide_numbers(10, 2)    # Valid division
    divide_numbers(10, 0)    # Division by zero
    divide_numbers(10, 'a')  # Invalid type (string instead of a number)

    # Test the read_file function with various file names
    read_file("example.txt")  # Try to read a non-existent file
    read_file("sample.txt")   # If you have a real file to test, use it here


    # Raising and catching a custom exception
    try:
        raise CustomError("Something went wrong in the custom logic!")
    except CustomError as e:
        print(f"Caught custom exception: {e}")


if __name__ == "__main__":
    main()

