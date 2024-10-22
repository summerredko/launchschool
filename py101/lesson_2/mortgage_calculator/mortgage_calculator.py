# Prompts user for input with an f string
def prompt(message):
    print(f"==> {message}")

# Checks input for valid characters
def is_valid_input(input_str):
    valid_chars = set("0123456789.")
    if input_str == "0":
        return False
    if input_str == "":
        return False
    return all(char in valid_chars for char in input_str)

# Loop that returns invalid message if not is_valid_input or
# executes the clean_money_input function if valid.
def get_valid_input(prompt_message):
    while True:
        prompt(prompt_message)
        user_input = input().strip()
        if is_valid_input(user_input):
            return float(user_input)

        print("Invalid input. Please enter a valid number.")


# Adjusts percentage calculation if APR is input as a float
def adjust_percentage(value):
    return value / 100 if value > 1 else value

# Converts APR to monthly
def monthly_apr_conversion(n):
    return n / 12

# Converts loan duration in years to monthly
def monthly_duration_conversion(n):
    return n * 12


# START
prompt('Welcome to Mortgage Calculator!')

# Retrieves and validates data from user for
# Loan Amount, APR, and Loan Duration
while True:
    loan_amount = get_valid_input('Enter loan amount: ')
    annual_apr = get_valid_input('Enter Annual Percentage Rate (APR): ')
    adjusted_apr = adjust_percentage(annual_apr)
    loan_duration = get_valid_input('Enter loan duration in years: ')

    # Converts yearly to monthly for APR and Loan Duration
    monthly_apr = monthly_apr_conversion(adjusted_apr)
    monthly_loan_duration = monthly_duration_conversion(loan_duration)

    # Formula for monthly payment calculation
    monthly_payment = (
        loan_amount * (
            monthly_apr / (
                1 - (1 + monthly_apr) ** (-monthly_loan_duration)
            )
        )
    )

    # Rounds float to two decimal places and prints result
    monthly_payment = round(monthly_payment, 2)
    print(f'Monthly mortgage payment: ${monthly_payment}')

    prompt("Would you like to execute another calculation? (y/n)")
    answer = input().lower()
    if answer and answer[0].lower() != 'y':
        break

while answer not in ["y", "n"]:
    prompt('Invalid input. Please enter "y" or "n"')
    answer = input()
