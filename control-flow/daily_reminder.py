# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        priority_message = f"'{task}' is a high priority task"
        if time_bound.lower() == "yes":
            reminder = f"{priority_message} that requires immediate attention today!"
        else:
            reminder = f"{priority_message}. Try to complete it as soon as possible."
    case "medium":
        priority_message = f"'{task}' is a medium priority task"
        if time_bound.lower() == "yes":
            reminder = f"{priority_message} that requires attention today."
        else:
            reminder = f"{priority_message}. You can complete it at your convenience."
    case "low":
        priority_message = f"'{task}' is a low priority task"
        if time_bound.lower() == "yes":
            reminder = f"{priority_message} that needs to be done today."
        else:
            reminder = f"{priority_message}. Consider completing it when you have free time."
    case _:
        reminder = "Unknown priority. Please try again."

# Provide a customized reminder
print("Reminder:", reminder)

