class SimpleCalculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def main(self): 
        print("Simple Calculator")
        print("Operations: 1. Add  2. Subtract  3. Multiply  4. Divide")

        try:
            choice = int(input("Choose an operation (1/2/3/4): "))

            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please choose a valid operation.")
            else:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == 1:
                    print("Result:", self.add(num1, num2))
                elif choice == 2:
                    print("Result:", self.subtract(num1, num2))
                elif choice == 3:
                    print("Result:", self.multiply(num1, num2))
                elif choice == 4:
                    try:
                        print("Result:", self.divide(num1, num2))
                    except ValueError as e:
                        print("Error:", e)
        except ValueError:
            print("Invalid input. Please enter valid numbers.")