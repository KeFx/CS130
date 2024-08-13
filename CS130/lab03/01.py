def get_total(number_str):
    total = 0
    for position, digit in enumerate(number_str):
        total += int(digit) * (position+1)
    return total

total = get_total('000000000')
checksum = total % 11

print(checksum)
