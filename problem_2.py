def find_rotated_array_pivot(input_list):
    """
    Find the index of the pivot in a rotated sorted array.

    Args:
        input_list(array): a sorted, rotated array

    Returns:
        int: index of pivot
    """
    lower = 0
    upper = len(input_list) - 1
    if input_list[lower] < input_list[upper]:
        # list is not rotated
        return 0
    pivot = upper // 2
    while lower < pivot:
        if input_list[pivot] < input_list[lower]:
            upper = pivot
            pivot = (lower + pivot) // 2
        else:
            lower = pivot
            pivot = (lower + upper) // 2
    return pivot

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot = find_rotated_array_pivot(input_list)
    if input_list[pivot] == number:
        return pivot

    lower = 0
    upper = len(input_list) - 1
    if number < input_list[0]:
        lower = pivot + 1
    elif pivot > 0:
        upper = pivot

    index = (upper + lower) // 2
    while lower < index:
        if input_list[index] == number:
            
            return index
        if number < input_list[index]:
            upper = index
        else:
            lower = index
        index = (upper + lower) // 2
    
    if input_list[index] == number:
        return index
    return -1    

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4], 2])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
