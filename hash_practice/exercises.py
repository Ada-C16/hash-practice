
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    # start with empty dictionary
    anagram_dict = {}
    # iterate through each string
    for string in strings:
        # sort each string alphabetically
        word_sorted = "".join(sorted(string))
        # if the sorted string is not in the dictionary
        if word_sorted not in anagram_dict:
            # store word sorted as key and original string as value
            anagram_dict[word_sorted] = [string]
        else:
            # else, we have an anagram, so add the original string to the value list
            anagram_dict[word_sorted].append(string)
    # return the values of the dictionary as an array of arrays which is contained in values of the dictionary
    return list(anagram_dict.values())



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

