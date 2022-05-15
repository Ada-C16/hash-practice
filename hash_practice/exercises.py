from collections import defaultdict

def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
    """

    anagrams = []
    word_dict = get_anagrams(strings)
    for word in word_dict.values():
        anagrams.append(word)
    return anagrams


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


# helpers
def get_anagrams(source_list):
    word_dict = defaultdict(list)
    for word in source_list:
        key = "".join(sorted(word))
        word_dict[key].append(word)
    return word_dict