
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    pass

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

