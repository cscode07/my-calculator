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