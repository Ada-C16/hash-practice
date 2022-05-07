""" This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n log n)
        Space Complexity: O(n)
    """
def grouped_anagrams(strings):
    map = {}
    for string in strings:
        sort = str(''.join(sorted(string)))
        if sort not in map: 
            map[sort] = [string]
        else:
            list = map[sort]
            list.append(string)
            map[sort] = list
    
    lists = []
    for key in map:
        lists.append(map[key])
    return lists


def makeMap(string):
    map = {}

    for char in string:
        if not map.get(char):
            map[char] = 1
        else:
            map[char] += 1
    
    return map

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
    """    
    if not nums:
        return []

    map = makeMap(nums)

    pairs = []
    for key in map:
        pairs.append((map[key], key))

    pairs.sort()

    kItems = []
    index = -1
    count = 0
    while count < k:
        kItems.append(pairs[index][1])
        index -= 1
        count += 1

    print(kItems)
    return kItems 

def valid_sudoku(table):
    pass
#     """ This method will return the true if the table is still
#         a valid sudoku table.
#         Each element can either be a ".", or a digit 1-9
#         The same digit cannot appear twice or more in the same 
#         row, column or 3x3 subgrid
#         Time Complexity: ?
#         Space Complexity: ?
#     """
#     #need to manually check that every square, row, column is valid
#     #so make every square, row, column into a freq map
    
#     for row in table:
#         map = {}
#         for block in row:
#             if block not in map:
#                 map[block] = 1
#             elif block != ".": #if it's already in the map and NOT a ".", there's more than one 
#                 return False
    

#     columnNum = 0
#     while columnNum < 9:
#         rowNum = 0
#         map = {}
#         while rowNum < 9:
#             if table[rowNum][columnNum] not in map:
#                 map[table[rowNum][columnNum]] = 1
#             elif block != ".":
#                 return False
#             rowNum += 1
#         columnNum += 1
    
    #now i wanna slice for the squares
    #square 1 is 
    #table[0][0:3]
    #table[1][0:3]
    #table[2][0:3]

    #square 2 is
    #table[0][3:6]
    #table[1][3:6]
    #table[2][3:6]

    #square 3 is
    #table[0][6:9]
    #table[1][6:9]
    #table[2][6:9]

    #square 4 is
    #table[3][0:3]
    #table[4][0:3]
    #table[5][0:3]

    # squares = []
    # rowNum = 0
    # while rowNum < 7:
    #     start = 0
    #     stop = 3
    #     square = []
    #     while stop < 10:
    #         square.append(table[rowNum][start:stop])

    



    
    