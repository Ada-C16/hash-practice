from collections import defaultdict, deque
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    pass

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    freq = defaultdict(int)
    for num in nums: # O(n) where n is number of nums
        freq[num] += 1

    counts = defaultdict(deque)
    max_count = 0
    for num, count in freq.items(): # O(d) where d is number of distinct nums - at most equal to O(n) if all nums are distinct
        counts[count].append(num)
        if count > max_count:
            max_count = count

    results = []
    while len(results) < k and max_count > 0: # O(c) where c is the highest frequency - at most equal to O(n) if all nums are distinct
        if counts[max_count]:
            results.append(counts[max_count].popleft())
        else:
            max_count -= 1
    return results


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

