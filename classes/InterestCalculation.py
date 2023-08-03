class InterestCalculation:
    def calculate_final_value(initial_capital, interest_rate, investment_time_months):
        interest_rate_decimal = interest_rate / 100
        investment_time_years = investment_time_months / 12

        final_value = initial_capital * (1 + (interest_rate_decimal * investment_time_years))
        return final_value

    def main():
        initial_capital = float(input("Enter the initial capital: "))
        interest_rate = float(input("Enter the interest rate (in percentage): "))
        investment_time_months = int(input("Enter the investment time (in months): "))

        final_value = InterestCalculation.calculate_final_value(initial_capital, interest_rate, 
        investment_time_months)
        print(f"The final value of the investment is: {final_value:.2f}")