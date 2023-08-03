from classes.SimpleCalculator import SimpleCalculator
from classes.PrimeNumbers import PrimeNumbers
from classes.Factorial import Factorial
from classes.Palindrome import Palindrome
from classes.Table import Table
from classes.VowelCounter import VowelCounter
from classes.GradeAverage import GradeAverage
from classes.InterestCalculation import InterestCalculation

class Menu:
    def __init__(self, options):
        self.options = options
    def display(self):
        print("=== MENU ===")
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")
    def get_choice(self):
        while True:
            try:
                choice = int(input("Choose an option: "))
                if 1 <= choice <= len(self.options):
                    return choice
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    def option1(self):
        SimpleCalculator.main()
    def option2(self):
        PrimeNumbers.main()
    def option3(self):
        Factorial.main()
    def option4(self):
        Palindrome.main()
    def option5(self):
        Table.main()
    def option6(self):
        VowelCounter.main()
    def option7(self):
        GradeAverage.main()
    def option8(self):
        InterestCalculation.main()
    def exit_menu(self):
        print("Exiting the menu...")

    def map_functions_to_classes():
        return [SimpleCalculator, PrimeNumbers, Factorial,
                Palindrome, Table, VowelCounter,
                GradeAverage, InterestCalculation]
    
    def run(self):
            functions = Menu.map_functions_to_classes()

            while True:
                self.display()
                choice = self.get_choice()
                if 1 <= choice <= len(functions):
                    selected_class = functions[choice - 1]
                    selected_class.main()
                    if self.ask_return_to_menu():
                        continue
                    else:
                        break
                elif choice == len(functions) + 1:
                    self.exit_menu()
                    break
                else:
                    print("Invalid option. Please try again.")

    def ask_return_to_menu(self):
        answer = input("Return to menu? (y/n): ").lower()
        return answer == "y"