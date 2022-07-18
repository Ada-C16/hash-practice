# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

def sortString(string):
    sorted_letters = sorted(string)
    sorted_string = "".join(sorted_letters)
    return sorted_string

def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each sub-array will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    temp = {}
    array_words = []

    for word in strings:
        sorted_word = sortString(word)
        if sorted_word in temp:
          temp[sorted_word].append(word)
        else:
            temp[sorted_word] = [word]

    for key in temp:
        array_words.append(temp[key])
    return array_words


    
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occurring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    hash_table = {}
    for num in nums:
        if num in hash_table:
            hash_table[num] += 1
        else:
            hash_table[num] = 1

    # get keys with highest count based on k
    sorted_keys = sorted(hash_table.keys(), key=hash_table.get, reverse=True)
    return sorted_keys[0:k]


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

