from collections import defaultdict

def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(N)
        Space Complexity: O(N)
    """
    if len(strings) == 0:
        return []

    anagrams = {}
    for s in strings:
        a = tuple(sorted(s))
        if a in anagrams:
            anagrams[a].append(s)
        else:
            anagrams[a] = [s]
    return list(anagrams.values())

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(N)
        Space Complexity: O(N)
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

def valid_sudoku(board):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ON^2
        Space Complexity: ON+K
    """
    """
    Clarifying 
    Period is blank/not filled in
    empty return True
    3 variables
    1 - track rows 
    2 - track columns
    3 - track squares(subgrid)
    subgrid - (// 3)
    in range
    for current index range(0, 9)

    guard clause
    if not digit 

    key value - 
    input validation checking for 1-9
    return false

    if duplicates in either 1, 2, 3
    return False

    return True

    """

    row = defaultdict(set) 
    col = defaultdict(set)        
    block = defaultdict(set) 

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".": 
                continue
            if (board[r][c] in row[r]) or (board[r][c] in col[c]) or (board[r][c] in block[(r//3, c//3)]):
                return False
            row[r].add(board[r][c])
            col[c].add(board[r][c])
            block[(r//3, c//3)].add(board[r][c])
    return True



    

