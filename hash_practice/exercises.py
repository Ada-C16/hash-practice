
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ? O(n)
        Space Complexity: ? 0(n)
    """
    # guard clause
    if not strings:
        return strings

    # create a empty array to hold arrays of anagrams
    anagrams = []

    # create an empty dictionary to hold sorted string keys and list of strings values
    ana_dict = {}
    
    def hash_func(string):
        sorted_string = ''.join(sorted(string))
        if sorted_string not in ana_dict:
            ana_dict[sorted_string]=[string]
        else:
            ana_dict[sorted_string].append(string)

    # iterate through the list of strings
    for string in strings:
        hash_func(string)
    
    for key, value in ana_dict.items():
        anagrams.append(value)

    #return list of lists
    return anagrams


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element. OUR ANSWER
        Time Complexity: ? O(nlogn)
        Space Complexity: ? O(n)
    """
    if nums == []:
        return []
    freq_dict = {}
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else: 
            freq_dict[num] = 1
    nums_set = set(nums) 
    nums = list(nums_set)
    nums.sort(reverse=True, key=lambda lol: freq_dict[lol])
    return nums[0:k:1]

# maybe later
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