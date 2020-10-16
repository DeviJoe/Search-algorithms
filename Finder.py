

# Linear search
# Return average number of linear search comparisons
def linear_search(array):
    # счетчик операций
    count_of_operations = 0
    for i in range(len(array)):
        # локальный счетчик
        counter = 0
        for j in range(len(array)):
            counter += 1
            if array[j] == array[i]:
                count_of_operations += counter
                break
    return int(count_of_operations / len(array))


# Binary search
# Return average number of binary search comparisons
def binary_search(array):
    # счетчик операций
    count_of_operations = 0
    for i in range(len(array)):
        # локальный счетчик
        counter = 0
        # нижняя граница
        lower_bound = 0
        # верхняя граница
        upper_bound = len(array) - 1
        while lower_bound <= upper_bound:
            counter += 1
            middle = (lower_bound + upper_bound) // 2
            if array[i] == array[middle]:
                count_of_operations += counter
            elif array[i] < array[middle]:
                upper_bound = middle - 1
            else:
                lower_bound = middle + 1
    return count_of_operations / len(array)


# Interpolation search
# Return average number of interpolation search comparisons
def interpolation_search(array):
    # счетчик операций
    count_of_operations = 0
    # нижняя граница
    lower_bound = 0
    # верхняя граница
    higher_bound = (len(array) - 1)
    for i in range(len(array)):
        counter = 0
        while lower_bound <= higher_bound and array[lower_bound] <= array[i] <= array[higher_bound]:
            counter += 1
            index = lower_bound + int(((float(higher_bound - lower_bound) / (
                    array[higher_bound] - array[lower_bound])) * (array[i] - array[lower_bound])))
            if array[index] == array[i]:
                count_of_operations += counter
            elif array[index] < array[i]:
                lower_bound = index + 1
            else:
                higher_bound = index - 1
    return count_of_operations
