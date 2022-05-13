
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: ?
    """
    anagrams = {}
    for word in strings:
        sorted_word= ''.join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        else:
            anagrams[sorted_word].append(word)
    list_of_lists = []
    for item in anagrams.values():
        list_of_lists.append(item)
    return list_of_lists


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    "e.g.: Input: nums = [1,1,1,2,2,3], k = 2, Output: [1,2]"
    
    dict={}
    list=[]
    if nums == []:
        return []
    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    other_list = sorted(dict.items(), key=lambda x:x[1], reverse=True) ##anonymous function

    for i in range(k):
        list.append(other_list[i][0])
    return list

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

