import collections
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(N log N)
        Space Complexity: O(N)
    """
    if strings == []:
        return []

    hash = collections.defaultdict(list)
    for char in strings:
        hash[tuple(sorted(char))].append(char)   
    
    expected = []
    for each in hash.values():
        expected.append(each)
    return expected



def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(N)
        Space Complexity: O(N)
    """
    hash = collections.defaultdict(int)
    for num in nums:
        hash[num] += 1
    return sorted(hash, key=hash.get, reverse=True)[:k]



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

