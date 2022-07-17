
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(nklog(k)), where k is the length of the string 
        Space Complexity: O(log(n))
    """
    if not strings:
        return []

    result = {}
    for word in strings:
        key = ''.join(sorted(word))
        if key in result:
            result.get(key).append(word)
        else:
            result[key] = [word]
    return result.values()
    

 


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if not nums:
        return []
    count = {}
    frequency = [[] for i in range(len(nums)+1)]
    for n in nums:
        if n not in count:
            count[n] = 0
        count[n] += 1

    for key, val in count.items():
        frequency[val].append(key)
    

    result = []
    for i in range(len(frequency)-1, 0, -1):
        for n in frequency[i]:
            result.append(n)
            if len(result) == k:
                return result


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: o(n^2)
        Space Complexity: O(n)
#     """
from collections import defaultdict     
def validSudoku(board):
    if board == None:
        return None
    N = 9
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)

    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                continue
            if(board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[(row // 3, col // 3)]):
                return False
            cols[col].add(board[row][col])
            rows[row].add(board[row][col])
            squares[(row // 3, col // 3)].add(board[row][col])
    return True
