
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    anagrams_map = {}
    if not strings:
        return []
    
    for string in strings: 
        letters_in_string = ''.join(sorted(string))
        if letters_in_string in anagrams_map:
            anagrams_map[letters_in_string].append(string)
        else:
            anagrams_map[letters_in_string] = [string]
    
    anagrams = []
    for item in anagrams_map.values():
        anagrams.append(item)
    
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

