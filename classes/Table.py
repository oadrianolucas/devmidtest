class Table:
    def display_table(number):
        print(f"Multiplication table of {number}:")
        for i in range(1, 11):
            result = number * i
            print(f"{number} x {i} = {result}")

    def main():
        try:
            number = int(input("Enter a number to display its multiplication table: "))
            Table.display_table(number)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")