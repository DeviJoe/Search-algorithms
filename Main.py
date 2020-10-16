# В текстовом файле input.txt представлен массив из N
# целых чисел от 1 до N, расположенных в произвольном
# порядке без повторений. Реализуйте функцию поиска в этом
# массиве на основе алгоритма последовательного поиска.
# Головная программа должна вызывать функцию поиска для
# каждого элемента массива от 1 до N. В текстовый файл
# output.txt выведите среднее число сравнений, проведённых
# программой последовательного поиска.
# 2) Выполните то же для двоичного поиска в упорядоченном
# массиве.
# 3) Выполните то же для интерполяционного поиска в
# упорядоченном массиве.
# Сравните вычислительную сложность рассмотренных в задаче
# алгоритмов.
from FileUtils import read_array, write_data_in_file
from Finder import linear_search, binary_search, interpolation_search

array = read_array('input.txt')
array.sort()
linear_output = linear_search(array)
binary_output = binary_search(array)
interpolation_output = interpolation_search(array)
write_data_in_file('output.txt', linear_output, binary_output, interpolation_output)
