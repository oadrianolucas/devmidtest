class PrimeNumbers:
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def main():
        try:
            num_primes = int(input("Enter the number to check if it's prime and print the first 10 prime numbers: "))

            if PrimeNumbers.is_prime(num_primes):
                print("The number is prime.")
                
                primes_found = 0
                current_number = 2

                print("First 10 prime numbers:")

                while primes_found < 10:
                    if PrimeNumbers.is_prime(current_number):
                        print(current_number, end=" ")
                        primes_found += 1
                    current_number += 1

                print()
            else:
                print("The number is not prime.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
