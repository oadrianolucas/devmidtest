from menu import Menu

if __name__ == "__main__":
    options = ["Simple Calculator", "Prime Numbers", "Factorial",
               "Palindrome", "Table", "Vowel Counter", "Grade Average",
               "Interest Calculation", "Exit"]
    menu = Menu(options)
    menu.run() 