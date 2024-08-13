while True:
    number = int(input("Enter an integer between 1 and 9: "))
    if 1 <= number <= 9:
        break

result = "EVEN" if number % 2 == 0 else "ODD"

print(result)
