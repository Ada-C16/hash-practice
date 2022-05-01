
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    # dict = {
    #   "key"-->sorted leters, value = ["words that are anagrams of key"]
    # }
    hash_map = {}
    # Determine if string is anagaram of another string
    for string in strings:
        # Anagrams are the same letters rearranged
        # sort string to see if it subscribes to an anagram in hash_map
        sorted_string = sorted(list(string))
        sorted_string = "".join(sorted_string)
        
        # Ensure there is a key at sorted_string, if not -- create empty list
        hash_map[sorted_string] = hash_map.get(sorted_string, [])
        # Append new string to list
        hash_map[sorted_string].append(string)

    result = []
    for v in hash_map.values():
        result.append(v)

    return result
    # return list of lists 
    # [ 
    #   [list of anagramed strings],
    #   [list of anagramed strings],
    # ]

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


# if __name__ == '__main__':
#     words = ["eat", "tea", "tan", "ate", "nat", "bat"]

#     print(grouped_anagrams(words))
