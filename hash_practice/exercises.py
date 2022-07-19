
from typing import OrderedDict


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
    """
    anagrams = {}
    for string in strings:
        string_sorted = ''.join(sorted(string))
        if string_sorted in anagrams:
            anagrams[string_sorted].append(string)
        else:
            anagrams[string_sorted] = [string]
    return list(anagrams.values())


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
    """
    elements_count = {}
    for num in nums:
        if num in elements_count:
            elements_count[num] += 1
        else:
            elements_count[num] = 1
    result = []
    count = 0
    for key, _ in sorted(elements_count.items(), key= lambda x: x[1], reverse=True):
        if count < k:
            result.append(key)
            count += 1
        else:
            break
    return result



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

