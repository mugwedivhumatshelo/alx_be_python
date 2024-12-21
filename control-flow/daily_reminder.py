# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        priority_message = "'{}' is a high priority task".format(task)
    case "medium":
        priority_message = "'{}' is a medium priority task".format(task)
    case "low":
        priority_message = "'{}' is a low priority task".format(task)
    case _:
        priority_message = "Unknown priority"

if time_bound.lower() == "yes":
    reminder = "{} that requires immediate attention today!".format(priority_message)
else:
    reminder = "{} Consider completing it when you have free time.".format(priority_message)

# Provide a customized reminder
print("Reminder:", reminder)

