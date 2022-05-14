from collections import defaultdict

def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    anagram_dict = defaultdict(list)
    result = []

    for word in strings:
        for char in word:
            result.append(char) #gets all the characters in a word, ie "e", "a", "t"
        result.sort()
        letter_tuple = tuple(result)
        anagram_dict[letter_tuple].append(word)
        result = []

    for item in anagram_dict.values():
        result.append(item)
    
    return result
    

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    elements_dict = defaultdict(int)
    result = []
    stop = -1-k

    for num in nums:
        elements_dict[num] += 1
    
    elements = list(elements_dict.items())
    elements.sort(key= lambda tup: tup[1])

    for tup in elements[-1:stop:-1]:
        result.append(tup[0])
    
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
    valid_element = {
        '1':1, '2':1, '3':1, '4':1, '5':1,
        '6':1, '7':1, '8':1, '9':1, '.':1
    }
    
    vertical_check = True
    vertical = vertical_sudoku(table, valid_element)
        

    horizontal_check = True 
    horizontal = horizontal_sudoku(table, valid_element)

    grid_check = [grid_sudoku(table, 0, 0),
    grid_sudoku(table, 0, 3),
    grid_sudoku(table, 0, 6),
    grid_sudoku(table, 3, 0),
    grid_sudoku(table, 3, 3),
    grid_sudoku(table, 3, 6),
    grid_sudoku(table, 6, 0),
    grid_sudoku(table, 6, 3),
    grid_sudoku(table, 6, 6)]
   

    if horizontal == True and vertical == True and False not in set(grid_check):
        return True
   
    return False

def vertical_sudoku(table, valid_element):
    i = 0
    flattened_table = []
    column = []

    for item in table:
        flattened_table += item

    while i < 9:
        column.append(flattened_table[i::9])
        i+= 1
    
    for col in column:
        for item in valid_element:
            if item != '.' and col.count(item) > 1:
                return False
        
    return True

def horizontal_sudoku(table, valid_element):
    for row in table:
        for item in valid_element:
            if item != '.' and row.count(item) > 1:
                return False

    return True

def grid_sudoku(table, i, j):
    sub_grid = [
        table[i][j], table[i][j+1], table[i][j+2],
        table[i+1][j], table[i+1][j+1], table[i+1][j+2],
        table[i+2][j], table[i+2][j+1], table[i+2][j+2]
        ]

    for square in sub_grid:
        if square != '.' and sub_grid.count(square) > 1:
            return False
    
    return True


    