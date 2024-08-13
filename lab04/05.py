def get_connected_list(airports_dict, start_airport):
    try:
        trip = []
        trip.append(start_airport)
        while airports_dict[start_airport] != None:
            trip.append(airports_dict[start_airport])
            start_airport = airports_dict[start_airport]
        return (trip, 'Success!')

    except KeyError:
        return (trip, 'Missing end destination')

data_dict = {'a':'q', 'd':'a', 'e':'f', 'q':None, 'f':'o', 'g':'h', 'h':'m'}
print(get_connected_list(data_dict, 'd'))
result = get_connected_list(data_dict, 'f')
print(type(result), result)
result = get_connected_list(data_dict, 'o')
