
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    # start with empty dictionary
    anagram_dict = {}
    # iterate through each string
    for string in strings:
        # sort each string alphabetically
        word_sorted = "".join(sorted(string))
        # if the sorted string is not in the dictionary
        if word_sorted not in anagram_dict:
            # store word sorted as key and original string as value
            anagram_dict[word_sorted] = [string]
        else:
            # else, we have an anagram, so add the original string to the value list
            anagram_dict[word_sorted].append(string)
    # return the values of the dictionary as an array of arrays which is contained in values of the dictionary
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
    # account for a tie
    most_common = sorted(most_common.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in most_common[:k]]

    


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n**2)
        Space Complexity: O(1)
    """
    # Note from Lizet to instructor: I know this doesn't pass the last 2 tests, but I'm not sure why.
    # test cases but submitting as is since this last function is optional
    # iterate through each row
    for row in table:
        # iterate through each element in the row
        for element in row:
            # if the element is not a "."
            if element != ".":
                # if the element is not a digit 1-9
                if element not in "123456789":
                    return False
                # if the element is a digit 1-9
                else:
                    # if the element is in the same row
                    if row.count(element) > 1:
                        return False
                    # if the element is in the same column
                    if [row[i] for i in range(9)].count(element) > 1:
                        return False
                    # if the element is in the same 3x3 subgrid
                    if [table[i][j] for i in range(3) for j in range(3)].count(element) > 1:
                        return False
    return True