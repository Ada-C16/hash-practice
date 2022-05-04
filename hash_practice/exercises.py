
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
        Time Complexity: ?
        Space Complexity: ?
    """
    dict = {}
    arr = []
    if nums == []:
        return []
    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    arr2 = sorted(dict.items())

    for i in range(k):
        arr.append(arr2[i][0])
    return arr




def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    pass