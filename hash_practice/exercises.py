""" This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
def grouped_anagrams(strings):
    map = {}
    for string in strings:
        sort = str(''.join(sorted(string)))
        if sort not in map: #whats the time complexity here
            #what's the time complexity diff between this and .get()
            map[sort] = [string]
        else:
            list = map[sort]
            list.append(string)
            map[sort] = list
    
    lists = []
    for key in map:
        lists.append(map[key])
    return lists

    #check out default dict for this problem too
    #it's a way to only add things to the dict with certain conditions 

    #there is a way to solve this without sort, like with something like counting 


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
        Time Complexity: ?
        Space Complexity: ?
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
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    #


    pass

