from collections import defaultdict

def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n^2) rip
        Space Complexity: O(n)
    """
    res = set()
    freq_maps = {}
    for word in strings:
        freq_map = {}
        for char in word:
            if freq_map.get(char):
                freq_map[char] += 1
            else:
                freq_map[char] = 1
        freq_maps[word] = freq_map
    for word in strings:
        sub_res = set()
        for key, map in freq_maps.items():
            if freq_maps[word] == map:
                sub_res.add(key)
        res.add(tuple(sub_res))
    actual_res = []
    for sub in list(res):
        actual_res.append(list(sub))
    return actual_res

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log(n))
        Space Complexity: O(n)
    """
    if not nums:
        return []
    freq_map = {}
    for num in nums:
        if freq_map.get(num):
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    nums = set(nums)
    nums = list(nums)
    nums.sort(reverse = True, key = lambda k: freq_map[k])
    return nums[:k]


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(1) because sudoku boards are a constant size
                            I guess it could be O(n) where n is the number of cells if you did like 
                            a super sudoku board but the 9x9 grid size is hard coded in here so you'd
                            have to change that to len(table) and len(table[0])
        Space Complexity: O(n)
    """

    #check rows
    for i in range(0, 9):
        row_freq = {}
        for j in range(0, 9):
            cell = table[i][j]
            if row_freq.get(cell) and cell != ".":
                return False
            elif cell != ".":
                row_freq[cell] = True

    #check columns
    for i in range(0, 9):
        col_freq = {}
        for j in range(0,9):
            cell = table[j][i]
            if col_freq.get(cell) and cell != ".":
                return False
            elif cell != ".":
                col_freq[cell] = True

    #check boxes
    i = 0
    j = 0
    while i < 9:
        while j < 9:
            grid_freq = {}
            for n in range(0, 3):
                for m in range(0, 3):
                    cell = table[i + n][j + m]
                    if grid_freq.get(cell) and cell != ".":
                        return False
                    elif cell != ".":
                        grid_freq[cell] = True
            j += 3
        i += 3
    
    return True

