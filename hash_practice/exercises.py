
from http.client import CONTINUE


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    strings_dict = {}
    anagrams_list = []

    for string in strings:
        string_list = list(string)
        string_list.sort()
        alphabetized_string = "".join(string_list)

        if alphabetized_string not in strings_dict.keys():
            strings_dict[alphabetized_string] = []
            strings_dict[alphabetized_string].append(string)
        else: 
            strings_dict[alphabetized_string].append(string)
    
    for value in strings_dict.values():
        anagrams_list.append(value)

    return anagrams_list




def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    
    nums_tally = {}
    most_common_nums = []

    for num in nums:
        if num not in nums_tally.keys():
            nums_tally[num] = 1
        else: 
            nums_tally[num] += 1
    
    sorted_tally_keys = sorted(nums_tally, key=nums_tally.get, reverse=True)

    most_common_nums = sorted_tally_keys[0:k]

    return most_common_nums


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

