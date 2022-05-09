
from numpy import sort
from pyrsistent import v


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(m * n log n)
        Space Complexity: O(n)
    """
    # hash_map = {
    #   key = sorted leters, value = ["words that are anagrams of key"]
    # }
    hash_map = {}

    # Determine if string is anagaram of another string
    for string in strings: # O(n)
        # Anagrams are the same letters rearranged
        # sort string to see if it subscribes to an anagram in hash_map
        temp_lst = list(string) # O(n log n)
        temp_lst.sort()
        sorted_string = "".join(temp_lst) 
        
        # Ensure there is a key at sorted_string, if not -- create empty list
        hash_map[sorted_string] = hash_map.get(sorted_string, []) 
        # Append new string to list
        hash_map[sorted_string].append(string)

    result = []
    for v in hash_map.values():
        result.append(v)

    return result

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    if not nums:
        return []

    # create frequency map
    freq_map = {}

    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    sorted_by_freq = []
    for num, freq in freq_map.items():
        # Adds to list frequency first, then key
        sorted_by_freq.append((freq, num))
    # Sorts descending based on frequency value
    sorted_by_freq.sort(key=lambda i: i[0], reverse=True)

    # store sorted values in array
    result = []
    for i in range(k):
        result.append(sorted_by_freq[i][1])

    return result

def valid_nums_freq_map():
    freq_map = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }
    return freq_map

def valid_grid(table, grid):
    # freq_map for grid
    grid_count = valid_nums_freq_map()
    i, j = grid

    for row in range(i, i + 3):
        for col in range(j, j + 3):
            if table[row][col] != ".":
                 grid_count[int(table[row][col])] += 1
                 if grid_count[int(table[row][col])] > 1:
                     return False


def valid_sudoku(table):
    """ This method will return true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    for row in range(0, len(table)):
        # Renew freq_maps
        row_map = valid_nums_freq_map()
        col_map = valid_nums_freq_map()
        # Check current row
        for col in range(0, len(table)):
            if table[row][col] != ".":
                row_map[int(table[row][col])] += 1
                if row_map[int(table[row][col])] > 1:
                    return False
            # Check current column
            if table[col][row] != ".":
                col_map[ int(table[col][row])] += 1
                if col_map[ int(table[col][row])] > 1:
                    return False

        # Check grids
        grids = [
            [0, 0], [0, 3], [0, 6],
            [3, 0], [3, 3], [3, 6],
            [6, 0], [6, 3], [6, 6],
        ]
        for grid in grids:
            if valid_grid(table, grid) == False:
                return False

    return True

if __name__ == '__main__':
    pass