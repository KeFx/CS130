def print_table(days_per_month, column_width=15):
    print(f"{'Month':>{column_width}} Days")
    print("-" * (column_width + 5))
    for month, days in days_per_month.items():
        print(f"{month:>{column_width}} {days}")

days_per_month = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

print_table(days_per_month)
