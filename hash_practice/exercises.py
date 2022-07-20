
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    anagram_dict = {}

    for string in strings: 
        word_sorted = "".join(sorted(string))
        if word_sorted not in anagram_dict: 
            anagram_dict[word_sorted] = [string]
        else: 
            anagram_dict[word_sorted] = [string]

    return list(anagram_dict.values())

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    most_common = {}
    for num in nums: 
        if num in most_common: 
            
            most_common[num] += 1 
        else: 
            most_common[num] = 1 
    most_common = sorted(most_common.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in most_common[:k]]



def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n2)
        Space Complexity: O(1)
    """
    for row in table: 
        for element in row: 
            if element != ".":
                if element not in "123456789":
                    return False 
                else: 
                    if row.count(element) >1: 
                        return False 
                    if [row[i] for i in range(9)].count(element)>1:
                        return False 
                    if [table[i][j] for i in range(3) for j in range(3)].count(element) >1: 
                        return False 
    return True 



