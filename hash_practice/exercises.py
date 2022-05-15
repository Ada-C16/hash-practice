
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if len(strings) == 0:
        return []

    hash = {}
    for string in strings:
        #sort out the word alphabetically since we are working with anagrams and make that the key
        #sorted returns a list and we need to change it back to a string by using join
        key = ''.join(sorted(string))
        if key not in hash:
            #bracket notation to add it in as a list
            #we're adding in the actual, not sorted, version of the string
            hash[key] = [string]
        else:
            #since the list is already there, append to it
            hash[key].append(string)
    print(hash.values())
    return hash.values()

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    #edge case
    if len(nums) == 0:
        return []

    #create a hashmap
    hash = {}

    #Build the hashmap for the elements
    for value in nums:
        #if the value is in the hashmap, increment it
        if value in hash:
            hash[value] = hash[value] + 1
        #otherwise, add it in
        else:
            hash[value] = 1
    
    #make the list to hold the k elements
    result = []
    #we only want to loop as much as k
    for i in range(k):
        #get the key that has the highest value
        maximum = max(hash, key = hash.get)
        #add it to the result to return
        result.append(maximum)
        #remove it from the hash so we can use max again in the next cycle
        hash.pop(maximum)

    #return the result holding the k highest elements
    return list(result)





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

grouped_anagrams(["eat", "tae", "tea", "eta", "aet", "ate"])