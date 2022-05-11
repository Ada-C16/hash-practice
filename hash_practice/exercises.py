
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n) -> where n equals the total number of characters in all the words
        Space Complexity: O(n)
    """
    
    anagrams = {}
    for word in strings:
        alphabet = [0] * 26
        for letter in word:
            alphabet[ord(letter.lower()) - ord("a")] += 1
        if tuple(alphabet) in anagrams:
            anagrams[tuple(alphabet)].append(word)
        else: 
            anagrams[tuple(alphabet)] = [word]
    return_list = []
    for k, v in anagrams.items():
        return_list.append(v)
    return return_list



def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n) --> Reduced from O(3n)
        Space Complexity: O(n)
    """
    if len(nums) <= 1:
        return nums

    freq_table = {}
    for num in nums:
        if num not in freq_table:
            freq_table[num] = 0
        freq_table[num] += 1

    return_list = [None] * len(nums)

    for key, value in freq_table.items():
        if return_list[value] == None:
            return_list[value] = [key]
        else:
            return_list[value].append(key)

    top_k = []

    for i in range(len(return_list) -1, 0, -1):
        if len(top_k) == k:
           return top_k
        if return_list[i] == None:
            continue
        for val in return_list[i]: 
            top_k.append(val)
            if len(top_k) == k:
                return top_k



def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
    """

    # Check Rows
    for row in table: 
        blank_dict = {}
        for col in row:
            if col == ".":
                continue
            if col in blank_dict:
                return False
            blank_dict[col] = 1

    # Check Columns
    col = 0 
    while col < len(table[0]):
        row = 0
        blank_dict = {}
        while row < len(table):
            if table[row][col] == ".":
                row += 1
                continue # Go to next row
            elif table[row][col] in blank_dict:
                return False
            else: 
                blank_dict[table[row][col]] = 1
                row += 1
        col += 1

    # Check Squares
    threes = [[0,1,2], [3,4,5], [6,7,8]]
    three_by_threes = []
    for i in range(3):
        for j in range(3):
            one_square = (threes[i], threes[j])
            three_by_threes.append(one_square)
    
    for square in three_by_threes:
        blank_dict = {}
        row = square[0]
        column = square[1]
        for r in row:
            for c in column:
                if table[r][c] == ".":
                    continue
                elif table[r][c]in blank_dict:
                    return False
                else:
                    blank_dict[table[r][c]] = 1
    return True


