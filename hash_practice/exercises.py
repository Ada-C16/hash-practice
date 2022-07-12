
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n^2)
        Space Complexity: )(n)
    """
    anagrams_map = {}
    for word in strings:
        alpha_word = "".join(sorted(word))
        if anagrams_map.get(alpha_word):
            anagrams_map[alpha_word].append(word)
        else:
            anagrams_map[alpha_word]= [word]
    
    anagram_groups = []
    for key, value in anagrams_map.items():
        anagram_groups.append(value)
        

    return anagram_groups

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

