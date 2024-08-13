def bubble_single_pass(data, index):
    for current_index in range(0, index):
        if data[current_index] > data[current_index + 1]:
            data[current_index], data[current_index + 1] = data[current_index + 1], data[current_index]

    largest = data[0]
    largest_index = 0
    for current_index in range(1, index + 1):
        if data[current_index] > largest:
            largest_index = current_index
        else:
            data[current_index], data[largest_index] = data[largest_index], data[current_index]
