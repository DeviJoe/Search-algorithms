# reading array from file
def read_array(file_name):
    with open(file_name) as f:
        array = [int(x) for x in next(f).split()]
    return array


# writing metadata in file
def write_data_in_file(file_name, linear_output, binary_output, interpolation_output):
    with open(file_name, 'w') as f:
        f.write('Average linear search comparisons: ' + str(linear_output) + '\n')
        f.write('Average binary search comparisons: ' + str(binary_output) + '\n')
        f.write('Average interpolation search comparisons: ' + str(interpolation_output) + '\n')
