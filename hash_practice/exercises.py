
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n^2)? The fucntion only loops through the length of strings for 
                                the number of letters in each string?
        Space Complexity: O(n)? Theres only 2 varaibles being stored...sortedWord and anagramsHash?
    """
    anagramsHash = {}
    for string in strings:
        sortedWord = "".join(sorted(string))
        if sortedWord in anagramsHash:
            anagramsHash[sortedWord].append(string)
        else:
            anagramsHash[sortedWord] = [string]
    return list(anagramsHash.values())
    

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity:  O(n^2)? 
    """
    freqHash = {}
    finalList = [] 
    
    if len(nums) == 0:
        return finalList
    for number in nums:
        if number not in freqHash:
            freqHash[number] = 0
        else:
            freqHash[number] += 1
    
    count = 1
    
    while count <= k:
        finalList.append(sorted(freqHash, key=freqHash.get)[-count])
        count += 1
    return finalList

    



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

