
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    hash_table = {}
    for str in strings:
        key = ''.join(sorted(str))
        if key in hash_table.keys():
            hash_table[key].append(str)
        else:
            hash_table[key] = []
            hash_table[key].append(str)

    result = []
    for key, value in hash_table.items():
        result.append(value)
    return result


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    frequency = {}
    for num in nums:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] = frequency[num] + 1

    frequency = dict(
        sorted(frequency.items(), key=lambda x: x[1], reverse=True))

    result = list(frequency.keys())[:k]

    return result


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """
    seen = set()
    for i in range(9):
        for j in range(9):
            number = str(table[i][j])
            if number != '.':
                row = number + 'in row' + str(i)
                col = number + 'in col' + str(j)
                # // for integer
                block = number + 'in block' + str(i//3) + str(j//3)
                if row in seen or col in seen or block in seen:
                    return False
                seen.add(row)
                seen.add(col)
                seen.add(block)
    return True
