
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n*m log m) ..? 
        Space Complexity: O(n) since a hash table was created
    """
    group_anagrams = {}
    for word in strings: #O(n) where n is the length of input
        sorted_ver = "".join(sorted(word)) #O(m log m) where m is the length of each word
        if sorted_ver not in group_anagrams:
            group_anagrams[sorted_ver] = [word]
        else:
            group_anagrams[sorted_ver].append(word)

    output = []
    for word_list in group_anagrams.values(): #O(n)
        output.append(word_list)
    return output
        

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

