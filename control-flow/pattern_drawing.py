# Prompt user for pattern size
pattern_size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw the pattern
while row < pattern_size:
    # Print asterisks for each row
    for _ in range(pattern_size):
        print("*", end="")
    
    # Move to the next row
    print()
    row += 1

