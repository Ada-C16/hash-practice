
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """
    if not strings:
        return []
    anagrams = {}
    for string in strings:
        sorted_string = "".join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    return list(anagrams.values())

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if not nums:
        return []
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_counts[:k]]

def valid_row(row):
    if not row:
        return False
    for i in range(1, 10):
        if str(i) not in row:
            return False
    return True

def valid_subgrid(subgrid):
    if not subgrid:
        return False
    for row in subgrid:
        if not valid_row(row):
            return False
    return True

def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """

    if not table:
        return False
    for row in table:
        if not valid_row(row):
            return False
    for col in zip(*table):
        if not valid_row(col):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not valid_subgrid(table[i:i+3], table[j:j+3]):
                return False
    return True


