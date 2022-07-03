
from attr import has


def grouped_anagrams(strings):
    """ 
    - Use a hash table to solve a coding problem
    - Identify how a hash table can produce a more attractive runtime over alternative solutions
    Given an array of strings, group anagrams together.
    ### Example
    ```
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
    ["ate","eat","tea"],
    ["nat","tan"],
    ["bat"]
    ]
    ```
    Note:
    - All inputs will be in lowercase.
    - The order of your output does not matter

        This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        
        Time Complexity: O(m * nlogn) - | python sorting algorithm -> O(n. logn).
        Space Complexity: O(n) 
    """
    # return empty list if no words 
    if len(strings) == 0:
        return []

    hash_table = {}
    for item in strings:
        # sort time complexity => O(n. logn).
        string = "".join(sorted(item))
        if string not in hash_table:
            hash_table[string] = [item]
        else:
            hash_table[string].append(item)

    print(hash_table.values())
    return list(hash_table.values())


print(grouped_anagrams(["eat", "tae", "tea", "eta", "aet", "ate"]))

def top_k_frequent_elements(nums, k):
    """ 
    ## Most Frequent K Elements
    Given a non-empty array of integers, return the *k* most frequent elements.
    ## Example 1
    ```
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
    ```
    ## Example 2
    ```
    Input: nums = [1], k = 1
    Output: [1]
    ```
    ## Note

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.

    You should be able to equal or beat O(n log n), where n is the array's size.
        This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    # if empty list return an empty array

    if len(nums) == 0:
        return []
    # count the frequency  of each element
    hash_table = {}
    frequency = [[] for i in range(len(nums) +1)]

    for item in nums:
        # coutn how many times an item occurs , return 0 if doesn't exists
        hash_table[item] = 1 + hash_table.get(item,0)
    # loop thorugh key-value pair 
    for item, count in hash_table.items():
        # append to the the freq list 
        frequency[count].append(item)

    result = []
    
    # loop though all the way up until zero
    # range(start, stop, step)
    for index in range(len(frequency) -1, 0, -1):
        for elem in frequency[index]:
            result.append(elem)
            if len(result) == k:
                return result

print(top_k_frequent_elements([9,9,8,8,7],2))

def valid_sudoku(table):
    """
    OPTIONAL
    This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    # Optional QUESTION - 
    pass

