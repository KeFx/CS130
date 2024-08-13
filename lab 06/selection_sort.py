def get_position_of_largest(data, index):
    largest_index = 0
    for index, number in enumerate(data[0:index+1]):
        if number > data[largest_index]:
            largest_index = index
    return largest_index

def selection_single_pass(data, index):
    largest_index  = get_position_of_largest(data, index)
    data[largest_index], data[index] = data[index], data[largest_index]

def my_selection_sort(data):	
    for index in range(len(data) - 1, 0, -1 ):
        selection_single_pass(data, index)
