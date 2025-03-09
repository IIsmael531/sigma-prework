import ast  # Import ast to safely convert the string into a list

input_str = input("Input your array here: ")

try:
    # Convert string to list
    input_array = ast.literal_eval(input_str)

    # Checks for a list of numbers
    if isinstance(input_array, list) and all(isinstance(num, int) for num in input_array):
        input_array.sort()  # Sort the list in ascending order
        maxmin = [input_array[0], input_array[-1]]  # Get min and max values

        print(maxmin)

    else:
        print("Please enter a valid list of numbers.")

except (ValueError, SyntaxError):
    print(
        "Invalid input format. Please enter a list like [2, 3, 7, 8, -2, -3].")
