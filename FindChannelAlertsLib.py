# Possibly add a check here for whitespace characters that aren't spaces.  Think
# about how robust I want this to be and whether I want to check for this
# elsewhere instead.
def read_text_file(file_name, delimeter):
    file = open(file_name, "r")
    data = []
    for line in file:
        temp_list = []
        list_index = -1
        for letter in line:
            list_index += 1
            if letter == delimeter:
                temp_list.append(list_index)
        if temp_list:
            if temp_list[-1] != list_index:
                if line[temp_list[-1]+1] != ' ':
                    if line.find('\n') == -1:
                        list_index += 1
                    temp_list.append(list_index)
        # for single word lines
        elif list_index > -1 and line[0] != '\n':
            if line[-1] == '\n':
                temp_list.append(list_index)
            else:
                temp_list.append(list_index + 1)
        current_index = -1
        row_data = []
        for number in temp_list:
            if number != current_index + 1:
                row_data.append(line[current_index+1:number])
            current_index = number
        if row_data:
            data.append(row_data)
    file.close()
    return data

# Helper function to search a list of lists and create a two new lists
# from a filter condition
def filter_list_of_lists(list_of_list, index, filter_condition):
    list_1 = [x for x in list_of_list if x[index] == filter_condition]
    list_2 = [x for x in list_of_list if x[index] != filter_condition]
    return list_1, list_2

# Helper function to print filtered data to file
def print_filtered_data_to_file(filtered_data, output_file_name):
    output_string = ''
    # first add alerts
    for alert in filtered_data[0]:
        output_string += ' '.join(alert) + '\n'
    # then add rest
    for line in filtered_data[1]:
        output_string += ' '.join(line) + '\n'
    file = open(output_file_name, 'w')
    file.write(output_string)
    file.close()

# Helper function to find all indeces of a specific char in a string
def find_char_indeces(char, string):
    return [i for i, ltr in enumerate(string) if ltr == char]
