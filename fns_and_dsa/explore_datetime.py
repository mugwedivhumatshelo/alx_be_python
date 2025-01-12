from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time."""
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """Calculates a future date based on user input."""
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    """Runs the datetime exploration script."""
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()