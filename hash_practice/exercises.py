def sort_string(string):
    sorted_chars = sorted(string)
    sorted_string = "".join(sorted_chars)

    return sorted_string


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    arrays = {}
    for string in strings:
        sorted = sort_string(string)
        if sorted in arrays:
            arrays[sorted].append(string)
        else:
            arrays[sorted] = [string]

    groups = [group for group in arrays.values()]

    return groups


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(nlogn)
        Space Complexity: O(n)
    """
    if not nums:
        return []
    
    freq_map = {}
    for e in nums:
        if e in freq_map:
            freq_map[e] +=1
        else:
            freq_map[e] = 1

    sorted_nums = sorted(freq_map.items(), key=lambda map_key: map_key[1], reverse=True)

    common_nums = [e[0] for e in sorted_nums]

    return common_nums[:k]


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

