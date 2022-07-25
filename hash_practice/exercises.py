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
        Time Complexity: ?
        Space Complexity: ?
    """
    num_frequency = {}
    frequency_dict = {}
    for i in nums:
        if i not in num_frequency:
            num_frequency[i] = 1
        else:
            num_frequency[i] += 1
    
    for key, value in num_frequency.items():
        if value not in frequency_dict:
            frequency_dict[value] = [key]
        else:
            frequency_dict[value].append(key)

    top_k_freq_ele = []
    for i in range(len(nums), 0, -1):
        if i in top_k_freq_ele:
            top_k_freq_ele.extend(frequency_dict[i])
        if len(top_k_freq_ele) >= k:
            break

    return top_k_freq_ele

def not_in_row(arr, row):
 
    # Set to store characters seen so far.
    st = set()
 
    for i in range(0, 9):
 
        # If already encountered before,
        # return false
        if arr[row][i] in st:
            return False
 
        # If it is not an empty cell, insert value
        # at the current cell in the set
        if arr[row][i] != '.':
            st.add(arr[row][i])
     
    return True

def not_in_col(arr, col):
 
    st = set()
 
    for i in range(0, 9):
 
        # If already encountered before,
        # return false
        if arr[i][col] in st:
            return False
 
        # If it is not an empty cell, insert
        # value at the current cell in the set
        if arr[i][col] != '.':
            st.add(arr[i][col])
     
    return True

def not_in_box(arr, startRow, startCol):
 
    st = set()
 
    for row in range(0, 3):
        for col in range(0, 3):
            curr = arr[row + startRow][col + startCol]
 
            # If already encountered before,
            # return false
            if curr in st:
                return False
 
            # If it is not an empty cell,
            # insert value at current cell in set
            if curr != '.':
                st.add(curr)
         
    return True

def isValid(arr, row, col):
 
    return (not_in_row(arr, row) and not_in_col(arr, col) and
            not_in_box(arr, row - row % 3, col - col % 3))


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    for i in range(0, n):
        for j in range(0, n):
 
            # If current row or current column or
            # current 3x3 box is not valid, return false
            if not isValid(table, i, j):
                return False
         
    return True
