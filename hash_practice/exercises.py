
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    pass


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
    """
    print(k)
    frequency_map = {}

    for element in nums:
        if element in frequency_map:
            frequency_map[element] += 1
        else:
            frequency_map[element] = 1

    print(frequency_map)

    max_value = sorted(frequency_map.keys(),
                       key=frequency_map.get, reverse=True)
    print(max_value)
    return max_value[0:k]


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    pass
