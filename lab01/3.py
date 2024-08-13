user_input = input("Enter your full name: ")

first_name, last_name = user_input.split()

formatted_name = first_name[0] + '. ' + last_name

print("=" * len(formatted_name))
print(formatted_name)
print("=" * len(formatted_name))

