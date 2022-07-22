
def grouped_anagrams(strings):
    anagrams = {}
    for word in strings:
        a = tuple(sorted(word))
        if a in anagrams:
            anagrams[a].append(word) 
        else:
            anagrams[a] = [word]
    return list(anagrams.values())


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else: 
            frequency[num] = 1
    sorted_frequency = sorted(frequency.keys(), key = frequency.get, reverse = True)
    return sorted_frequency[:k]

# optional 
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

