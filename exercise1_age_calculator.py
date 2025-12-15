# Import datetime module to work with dates
from datetime import datetime

try:
    # Ask user for birth date input
    birth_date_input = input("Enter your birth date (mm/dd/yyyy): ")

    # Convert input string to datetime object
    birth_date = datetime.strptime(birth_date_input, "%m/%d/%Y")

    # Get today's date
    today = datetime.today()

    # Calculate age
    age = today.year - birth_date.year

    # Adjust age if birthday has not occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    # Convert to European format
    european_format = birth_date.strftime("%d/%m/%Y")

    # Display results
    print(f"Your age is: {age} years")
    print(f"Birth date in European format: {european_format}")

except ValueError:
    # Handle invalid date or format
    print("Invalid date format! Please enter date in mm/dd/yyyy format.")
except Exception as e:
    # Handle any unexpected errors
    print("An unexpected error occurred:", e)
