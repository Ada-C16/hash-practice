
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    dict = {}
    
    for word in strings:
        sortedWord = "".join(sorted(word))
        
        if sortedWord in dict:
            dict[sortedWord].append(word)
            
        else:
            dict[sortedWord] = [word]
            
    return list(dict.values())
        

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    dict = {}
    arr = []
    if nums == []:
        return []
    #loops thru arr and adds to dict along with count of occurence
    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    # after add to dict, sort dict key by value and use splice to get k
    arr = sorted(dict, key = dict.get, reverse = True)
    return arr[:k]



def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    # checks rows
    for row in range(9):
        row_dict = {}
        for col in range(9):
            if table[row][col] != ".":
                if table[row][col] in row_dict:
                    return False
                else:
                   row_dict[table[row][col]] = 1
     # checks cols              
    for col in range(9):
        col_dict = {}
        for row in range(9):
            if table[row][col] != ".":
                if table[row][col] in col_dict:
                    return False
                else:
                   col_dict[table[row][col]] = 1
    # checks squares           
    for row in range(3):
        for col in range(3):
            square_dict = {}
            for i in range(3):
                for j in range(3):
                    if table[row*3 + i][col*3 + j] != ".":
                        if table[row*3 + i][col*3 + j] in square_dict:
                            return False
                        else:
                            square_dict[table[row*3 + i][col*3 + j]] = 1
    return True