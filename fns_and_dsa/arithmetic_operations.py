def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
    Performs basic arithmetic operations.

    Args:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The arithmetic operation to perform. Can be 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
    float: The result of the arithmetic operation.
    """

    # Check if the operation is valid
    if operation not in ['add', 'subtract', 'multiply', 'divide']:
        raise ValueError("Invalid operation. Supported operations are 'add', 'subtract', 'multiply', and 'divide'.")

    # Perform the arithmetic operation
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        # Check for division by zero
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = num1 / num2

    return result
