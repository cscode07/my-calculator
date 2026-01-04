def show_menu():
    print("\n=== CALCULATOR ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("❌ Please enter a valid number.")


def calculate(option, num1, num2):
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