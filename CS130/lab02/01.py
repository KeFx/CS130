def print_title():
    print("Average Rainfall, temperature and sunshine data for selected locations throughout NZ")
    print("====================================================================================")

    
def read_file(filename):
    
    input_file  = open(filename, 'r')
    
    content_as_list_of_lines = input_file.read().split('\n')
    input_file.close()
    
    return content_as_list_of_lines


def get_numbers_list(data):
    
    return [float(number.strip()) for number in data.split(',')]


def create_dictionary(filename):
    
    content_as_list_of_lines = read_file(filename)
    dictionary = {}
    
    for line in content_as_list_of_lines:
        key, value = line.split(':')

        dictionary[key] = get_numbers_list(value)

    return dictionary


def create_regions_dictionary(regions_list):

    return {region:[] for region in regions}


def Average(numbers_list):
    
    return sum(numbers_list) / len(numbers_list)


def merge_data(regions_dict, data_dict):
    
    for key, value in data_dict.items():
        regions_dict[key].append(Average(value))


def round_and_stringfy_data(data_list):
    return [str(format(data, ".2f")) for data in data_list]


def print_table(regions_dict, column_names) :
    col_width = 16
    column_names.insert(0, "Name")
    
    for column_name in column_names:
        print(column_name.rjust(col_width) + '|', end = "")

    print()

    for row_name, data in sorted(regions_dict.items()):

        data = round_and_stringfy_data(data)
        
        row_as_list = [row_name] + data

        for row_item in row_as_list:
            print(row_item.rjust(col_width) + '|', end = "")

        print()
            

def main():
    
    print_title()
    
    regions_filename = str(input("Enter a filename for reading regions: "))
    regions_list = read_file(regions_filename)
    regions_dictionary = create_regions_dictionary(regions_list)

    prompts =  {
        'rainfall' : "Enter a filename for reading rainfall data: ",
        'min_temp' : "Enter a filename for reading minimum temperature data: ",
        'max_temp' : "Enter a filename for reading maximum temperature data: ",
        'sunshine' : "Enter a filename for reading sunshine data: "
    }
        
    rainfall_data_file = str(input(prompts['rainfall']))
    min_temp_data_file = str(input(prompts['min_temp']))
    max_temp_data_file = str(input(prompts['max_temp']))
    sunshine_data_file = str(input(prompts['sunshine']))
    
    rainfall_data_dict = create_dictionary(rainfall_data_file)
    min_temp_data_dict = create_dictionary(min_temp_data_file)
    max_temp_data_dict = create_dictionary(max_temp_data_file)
    sunshine_data_dict = create_dictionary(sunshine_data_file)
    
    merge_data(regions_dictionary, rainfall_data_dict)
    merge_data(regions_dictionary, min_temp_data_dict)
    merge_data(regions_dictionary, max_temp_data_dict)
    merge_data(regions_dictionary, sunshine_data_dict)

    column_names = ['Rainfall(mm)', 'Min.Temperature', 'Max.Temperature', 'Sunshine(hr)']
    
    print_table(regions_dictionary, column_names)

main()
