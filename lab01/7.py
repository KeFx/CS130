def read_school_census_data(filename):
    f = open(filename, 'r')
    lines = f.read().split("\n")

    data = []
    for line in lines:
        splitted_line = line.split(',')
        
        splitted_line[1] = int(splitted_line[1])
        splitted_line[2] = int(splitted_line[2])
        splitted_line[3] = int(splitted_line[3])
    
        data.append(tuple(splitted_line))
    f.close()

    return data
