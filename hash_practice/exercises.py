
from collections import defaultdict

def create_string_freq_map(strings):
    """
    Return a dictionary of dictionaries. 
    Keys are of each string in strings and values of a dictionary 
    that has keys of each letter in the string and values of how many 
    times that letter appears in the string.
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    grouped_string_dicts = {}

    for string in strings: 
        string_dict = defaultdict(int)

        for char in string:
            string_dict[char] += 1

        grouped_string_dicts[string] = string_dict

    return grouped_string_dicts

def grouped_anagrams(strings):
    """ 
    This method will return an array of arrays.
    Each subarray will have strings which are anagrams of each other
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    grouped_anagrams = []

    if not strings:
        return grouped_anagrams

    grouped_string_dicts = create_string_freq_map(strings)

    for string in strings:
        anagram_array = []
        anagram_array.append(string)

        for word, char_freq_dict in grouped_string_dicts.items():
            if grouped_string_dicts[string] == char_freq_dict and word != string:
                anagram_array.append(word)
                strings.remove(word)

        grouped_anagrams.append(anagram_array)

    return grouped_anagrams

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    pass


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

