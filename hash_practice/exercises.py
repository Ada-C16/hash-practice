from collections import defaultdict

def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n * m)?
        Space Complexity: O(n) A LOT
    """
    def create_freq_tuple(string):
        arr = [0] * 26
        for char in string:
            i = ord(char) - ord("a")
            arr[i] += 1
        return tuple(arr)

    map = defaultdict(list)
    for string in strings:
        freq = create_freq_tuple(string)
        map[freq].append(string)

    return [value for value in map.values()]


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n * k)?
        Space Complexity: O(n)
    """
    map = defaultdict(int)
    for num in nums:
        map[num] += 1

    map2 = defaultdict(list)
    for num, freq in map.items():
        map2[freq].append(num)

    arr = []
    while k > 0 and map2:
        nums = map2.pop(max(map2))
        while k > 0 and nums:
            arr.append(nums.pop())
            k -= 1
    return arr


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same
        row, column or 3x3 subgrid
        Time Complexity: O(1) - if table is always 9x9?
        Space Complexity: O(1) - if table is always 9x9?
    """
    def has_dupe(values):
        seen = set()
        for value in values:
            if value == ".":
                continue
            if value in seen:
                return True
            seen.add(value)
        return False
    # validate rows
    for row in table:
        if has_dupe(row):
            return False
    # validate columns
    for i in range(9):
        column = [num for row in table for num in row[i]]
        if has_dupe(column):
            return False
    # validate subgrid
    i = 0
    j = 0
    while i < 9:
        subgrid = []
        for row in range(i, i + 3):
            for column in range(j, j + 3):
                subgrid.append(table[row][column])
        if has_dupe(subgrid):
            return False
        j += 3
        if j == 9:
            i += 3
            j = 0

    return True
