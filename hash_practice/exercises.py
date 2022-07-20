def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: While there appears only a single for-loop, 
        .join() adds O(N) & sorted() adds O(nlogn) during their ideal case
        Space Complexity: We're adding a new data structure, the anagrams_hash,
        meaning we're adding linear O(N) space based on the size of this new hash table
        We're also adding an auxiliary sorted_anagram string
    """
    anagrams_hash = {}
    for anagram in strings:
        sorted_anagram = "".join(sorted(anagram))
        if sorted_anagram in anagrams_hash:
            anagrams_hash[sorted_anagram].append(anagram)
        else:
            anagrams_hash[sorted_anagram] = [anagram]

    return list(anagrams_hash.values())

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

print(grouped_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))