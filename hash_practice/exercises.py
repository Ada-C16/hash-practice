
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n * m log m ) (where n is the number of strings and m is the average length of the strings)) 
        Space Complexity: O(n)
    """
    
    sorted_hash = {}
    for string in strings:
        sorted_string = "".join(sorted(string))
        if sorted_string in sorted_hash:
            sorted_hash[sorted_string].append(string)
        else:
            sorted_hash[sorted_string] = [string]
    
    grouped_anagrams = []
    for group in sorted_hash:
        grouped_anagrams.append(sorted_hash[group])
    
    return grouped_anagrams

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
    """
    if not nums:
        return []
    
    frequency_map = {}
    for num in nums:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
    
    sorted_elements = sorted(frequency_map.keys(), key=lambda map_key:frequency_map[map_key], reverse=True)

    return sorted_elements[:k]  


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(1) (because the table is always the same size)
        Space Complexity: O(1) (because the table is always the same size)
    """
    
    return valid_rows(table) and valid_columns(table) and valid_squares(table)

def valid_rows(table):
    for row in table:
        used = set()
        for num in row:
            if num in used:
                return False
            if num != ".":
                used.add(num) 

    return True

def valid_columns(table):
    for i in range(9):
        used = set()
        for j in range(9):
            if table[j][i] in used:
                return False
            if table[j][i] != ".":
                used.add(table[j][i])
        
    return True 

def valid_squares(table):       
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            used = set()
            for x in range(i, i+3):
                for y in range(j, j+3):
                    if table[x][y] in used:
                        return False
                    if table[x][y] != ".":
                        used.add(table[x][y])

    return True

