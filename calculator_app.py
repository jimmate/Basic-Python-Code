import os

def save_to_file(filename, text):
    # Saves text to a file
    try:
        with open(filename, "a") as file:
            file.write(text)
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_from_file(filename):
    # Reads text from a file
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found, please enter a valid filename")
    except Exception as e:
        print(f"Error reading from file: {e}")
    return None

def is_valid_float(value):
    # Checks if a value is a valid float
    try:
        float(value)
        return True
    except ValueError:
        return False


def calculator():
    # Perform simple calculations based on user input
    while True:
        filename = input("Please enter a filename to save calculations (without file extension): ")
        if not filename:
            print("Invalid filename. Please try again.")
            continue
        filename += ".txt" # Appends .txt extension to the filename

        if os.path.exists(filename):
            print("File name already exists. Please choose a different filename.")
            continue
        break

    while True:
        try:
            num1 = input("Please enter the first number: ")
            if not is_valid_float(num1):
                print("Invalid input. Please enter a valid number.")
                continue
            num1 = float(num1)

            operator = input("Please input an operator (+, -, *, /): ")
            if operator not in ['+', '-', '*', '/']:
                print("Invalid operator. Please try again.")
                continue

            num2 = input("Please enter the second number: ")
            if not is_valid_float(num2):
                print("Invalid input. Please enter a valid number.")
                continue
            num2 = float(num2)
            
        except ValueError:
            print("Invalid input. Please enter numeric values for numbers.")
            continue

        try:
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2
            save_to_file(filename, f"{num1} {operator} {num2} = {result}\n")
        except ZeroDivisionError:
            print("Error: cannot divide by zero.")
            continue
        except Exception as e:
            print(f"Error writing to file: {e}")
            continue

        print("Result: ", result)

        while True:
            choice = input("Would you like to perform another calculation? (y/n): ").lower()
            if choice not in ["y", "n"]:
                print("Invalid choice. Please enter either y or n.")
                continue
            break

        if choice == "n":
            break
    print("Calculations saved to:", filename)

    # Provide option to read from file
    while True:
        choice = input("Would you like to read from a file? (y/n): ").lower()
        if choice not in ["y", "n"]:
            print("Invalid choice. Please enter either y or n.")
            continue
        if choice == "y":
            while True:
                read_filename = input("Please enter the name of the text file you want to read (without file extension): ")
                read_filename += ".txt"
                read_text = read_from_file(read_filename)
                if read_text:
                    print("Contents of the file:")
                    print(read_text)
                else:
                    print("File not found. Please enter a valid filename.")
                    continue

                choice = input("Would you like to read another file? (y/n): ").lower()
                if choice not in ["y", "n"]:
                    print("Invalid choice. Please enter either y or n.")
                    continue
                if choice == "n":
                    break
        break

calculator()
