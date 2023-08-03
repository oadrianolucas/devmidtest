class Factorial:
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        else:
            factorial = 1
            for i in range(2, num + 1):
                factorial *= i
            return factorial

    def main():
        try:
            number = int(input("Enter an integer to calculate its factorial: "))
            if number < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                result = Factorial.factorial(number)
                print(f"The factorial of {number} is: {result}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")