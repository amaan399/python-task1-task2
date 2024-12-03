original_tuple = (10, 20, 30)

user_input = input("Enter a number to add to each element of the tuple: ")

user_input_value = int(user_input)

new_tuple = tuple(x + user_input_value for x in original_tuple)

print("Original Tuple:", original_tuple)

print("New Tuple:", new_tuple)
