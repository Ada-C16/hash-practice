
from array import array
from distutils.log import error
import string


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    anagram_dict = {}
    for sorted_word in strings:
        a = tuple(sorted(sorted_word))
        if a in anagram_dict:
           anagram_dict[a].append(sorted_word) 
        else:
           anagram_dict[a] = [sorted_word]
    return list(anagram_dict.values()) 

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    if len(nums) == 0:
        return []

    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    columns = {
        0: set(), 
        1: set(), 
        2: set(),
        3: set(), 
        4: set(), 
        5: set(),
        6: set(), 
        7: set(),
        8: set(), 
}
    rows = {
        0: set(), 
        1: set(), 
        2: set(),
        3: set(), 
        4: set(), 
        5: set(),
        6: set(), 
        7: set(),
        8: set(), 
    }
    grids = {
        (0,0): set(),
        (0,3): set(),
        (0,6): set(),
        (3,0): set(),
        (3,3): set(),
        (3,6): set(),
        (6,0): set(),
        (6,3): set(),
        (6,6): set()
    }

    for row in range(len(table)):
        for col in range(len(table[0])):
            n = table[row][col]
            if n != ".":
                n = int(n)
                if n < 1 or n > 9:
                    return False
                if n in columns[col] or n in rows[row] or n in grids[(get_top_left(row), get_top_left(col))]:
                    return False
                else:
                    columns[col].add(n)
                    rows[row].add(n)
                    grids[(get_top_left(row), get_top_left(col))].add(n)

    return True

