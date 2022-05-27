
from audioop import reverse
from re import L
from tokenize import group


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    grouped_anagrams = {}

    for word in strings:
        unique_word = "".join(sorted(word))
        if unique_word in grouped_anagrams:
            grouped_anagrams[unique_word].append(word)
        else:
            grouped_anagrams[unique_word] = [word]
    
    output = []

    for values in grouped_anagrams.values():
        output.append(values)
    
    return output


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if len(nums) == 0:
        return []

    num_map = {}

    for i in nums:
        if i in num_map:
            num_map[i] += 1
        else:
            num_map[i] = 1
    
    if len(num_map) == k:
        return nums

    reverse_num_map = {}

    for key in num_map:
        value = num_map[key]
        if value in reverse_num_map:
            reverse_num_map[value - .5] = key
        else:
            reverse_num_map[value] = key
    
    most_frequent = []

    for i in range(k):
        max_freq_num = reverse_num_map[max(reverse_num_map)]
        most_frequent.append(max_freq_num)
        reverse_num_map.pop(max(reverse_num_map))
    
    return most_frequent

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