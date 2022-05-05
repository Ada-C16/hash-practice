
from webbrowser import get


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n log(n))
        Space Complexity: O(n)
    """
    sorted_strings = {}
    result = []

    if len(strings) == 0:
        return []

    for char in strings:
        sorted_string = "".join(sorted(char))
        if sorted_string in sorted_strings:
            sorted_strings[sorted_string].append(char)
        else:
            sorted_strings[sorted_string] = [char]

    for value in sorted_strings.values():
        result.append(value)

    return result


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
    """
    freq_map = {}
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    max_keys = sorted(freq_map.keys(), key=freq_map.get, reverse=True)
    return max_keys[0:k]


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
