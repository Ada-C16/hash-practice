
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(N)
        Space Complexity: O(N)
    """
    if len(strings) == 0:
        return strings

    anagram_dict = {}
    for word in strings:
        sorted_string = "".join(sorted(word))
        if sorted_string not in anagram_dict:
            anagram_dict[sorted_string] = [word]
        else:
            anagram_dict[sorted_string].append(word)
    return list(anagram_dict.values())

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    dict = {}
    new_dict = {}
    
    for num in nums: 
        if num in dict:
            dict[num] += 1
        if num not in dict:
            dict[num] = 1
    
    
    for ele,freq in dict.items():
        if freq in new_dict:
            new_dict[freq].append(ele)
        else:
            new_dict[freq] = [ele]
    
    order_freq = sorted(dict.values(),reverse=True)
    new_list = []
    for freq in order_freq:
        new_list += new_dict[freq]
    return new_list[:k]
        
    

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

