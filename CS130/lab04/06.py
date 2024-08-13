def g():
    user_input = -1
    while user_input < 0 or user_input > 2:
        try:
            user_input = int(input("Enter selection: "))
        except ValueError:
            print("invalid")
    return user_input

g()
