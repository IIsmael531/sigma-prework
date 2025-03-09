from datetime import datetime

# Checks if the input follows the format
input_date = datetime.strptime(
    input("Enter a date (DD/MM/YYYY): "), "%d/%m/%Y").date()

# Today's date
todays_date = datetime.today().date()

# Calculate the difference in years
years_difference = todays_date.year - input_date.year - \
    ((todays_date.month, todays_date.day) < (input_date.month, input_date.day))

print(f"The difference is {years_difference} years.")
