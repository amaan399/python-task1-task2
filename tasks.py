#TASK 1
original_list = [1, 2, 3, 4, 5]


copied_list = original_list.copy()

multiplied_list = [x * y for x, y in zip(original_list, copied_list)]


print("Original List:", original_list)
print("Copied List:", copied_list)
print("Multiplied List:", multiplied_list)

#TASK 2
original_tuple = (10, 20, 30)


user_input = input("Enter numbers to add to the tuple: ")


user_input_tuple = tuple(int(x) for x in user_input.split())


new_tuple = original_tuple + user_input_tuple


print("Original Tuple:", original_tuple)
print("New Tuple:", new_tuple)