def show_menu():
    return (
        "\n=== CALCULATOR ===\n"
        "1. Addition (+)\n"
        "2. Subtraction (-)\n"
        "3. Multiplication (*)\n"
        "4. Division (/)\n"
        "5. Exit"
    )

def calculate_logic(option, num1=None, num2=None):
    """
    Main calculator logic function.
    option: "1"-"4" (operation)
    num1, num2: numbers to calculate
    Returns result or error message
    """
    try:
        num1 = float(num1)
        num2 = float(num2)
    except (TypeError, ValueError):
        return "❌ Invalid numbers"

    if option == "1":
        return num1 + num2
    elif option == "2":
        return num1 - num2
    elif option == "3":
        return num1 * num2
    elif option == "4":
        if num2 == 0:
            return "❌ Error: division by zero."
        return num1 / num2
    else:
        return "❌ Invalid option"


def main():
    print("Welcome to the Python Calculator (local test)!")
    while True:
        print(show_menu())
        option = input("Choose an option (1-5): ")
        if option == "5":
            print("Thank you for using the calculator 👋")
            break
        if option not in ["1", "2", "3", "4"]:
            print("❌ Invalid option.")
            continue
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        result = calculate_logic(option, num1, num2)
        print(f"Result: {result}")


if __name__ == "__main__":
    import sys
    if sys.stdin.isatty():
        main()