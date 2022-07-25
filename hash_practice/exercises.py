import collections
import heapq

def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: While there appears only a single for-loop, 
        .join() adds O(N) & sorted() adds O(nlogn) during their ideal case
        Space Complexity: We're adding a new data structure, the anagrams_hash,
        meaning we're adding linear O(N) space based on the size of this new hash table
        We're also adding an auxiliary sorted_anagram string
    """
    anagrams_hash = {}
    for anagram in strings:
        sorted_anagram = "".join(sorted(anagram))
        if sorted_anagram in anagrams_hash:
            anagrams_hash[sorted_anagram].append(anagram)
        else:
            anagrams_hash[sorted_anagram] = [anagram]

    return list(anagrams_hash.values())


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: Traversing through the list once to calculate the frequency, which is Linear O(N). 
           In addition, we're using heap to sort & find frequent words, which is Linear-Log O(NlogK)
           where N is the number of items in the list -> overall time complexity O(NlogK)
        Space Complexity: Linear O(N) - we're initializing new data structures
    """
    if nums == []:
        return []

    nums_dict = collections.defaultdict(int)
    for n in nums:
        nums_dict[n] += 1

    output = []
    heap_list = [(-freq, key) for key, freq in nums_dict.items()]
    heapq.heapify(heap_list)
    
    while(len(output) < k):
        output.append(heapq.heappop(heap_list)[1])
    
    return output


# 4 helper functions for sudoku
def not_in_row(arr, row):
    # Set to store characters seen so far
    temp_set = set()
 
    for i in range(0, 9):
 
        # If already encountered before, return false
        if arr[row][i] in temp_set:
            return False
 
        # If it is not an empty cell, insert value
        # at the current cell in the set
        if arr[row][i] != '.':
            temp_set.add(arr[row][i])
     
    return True

def not_in_col(arr, col):
    temp_set = set()
    for i in range(0, 9):
        # If already encountered before,return false
        if arr[i][col] in temp_set:
            return False
 
        # If it is not an empty cell, insert
        # value at the current cell in the set
        if arr[i][col] != '.':
            temp_set.add(arr[i][col])
     
    return True

def not_in_box(arr, startRow, startCol):
    temp_set = set()
    for row in range(0, 3):
        for col in range(0, 3):
            curr = arr[row + startRow][col + startCol]
 
            # If already encountered before, return false
            if curr in temp_set:
                return False
 
            # If it is not an empty cell,
            # insert value at current cell in set
            if curr != '.':
                temp_set.add(curr)
         
    return True

def is_valid(arr, row, col):
    return (not_in_row(arr, row) and not_in_col(arr, col) and
            not_in_box(arr, row - row % 3, col - col % 3))


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: Quadratic O(N^2) - nested for loop
        Space Complexity: Constant O(1) - not initializing any new data structures;
        unless we're counting temp sets from our helper functions

    """
    length = len(table)
    for i in range(0, length):
        for j in range(0, length):
            # If current row or current column or
            # current 3x3 box is not valid, return false
            if not is_valid(table, i, j):
                return False
         
    return True
