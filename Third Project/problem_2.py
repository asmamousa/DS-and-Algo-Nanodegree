def rotated_array_search(input_list, number):
    # log n
    index_of_min =find_index_of_min_number(input_list, 0, len(input_list)-1)

    # it's either this part or that and the t.c is log n
    index_from_part_one = find_number_in_list(input_list, 0, index_of_min-1, number)

    index_from_part_two = find_number_in_list(input_list, index_of_min, len(input_list)-1, number)

    if index_from_part_one == -1 and index_from_part_two == -1:
        return -1

    if index_from_part_one != -1:
        return index_from_part_one

    if index_from_part_two != -1:
        return index_from_part_two



def find_number_in_list(listt, start, end, number):
    if (number < listt[start]) or (number > listt[end]):
        return -1

    if start == end:
        if listt[start] == number:
            return start
        else:
            return -1

    mid_shift = (end-start)//2 if (end-start) >=2 else (end-start)
    mid = start + mid_shift

    if listt[mid] == number:
        return mid

    elif listt[mid] > number:
        return find_number_in_list(listt, start, mid-1, number)

    elif listt[mid] < number:
        return find_number_in_list(listt, mid+1, end, number)


def find_index_of_min_number(input_list, start, end):
    # check if the list is rotated by comparing the first and last numbers
    # if not rotated then return 0 as it's the index for the min number
    if input_list[-1] > input_list[0]:
        return 0 

    mid_shift = (end-start)//2 if (end-start) >=2 else (end-start)
    mid_index = start + mid_shift

    if input_list[mid_index] > input_list[mid_index+1]:
        return mid_index+1

    if input_list[mid_index] < input_list[mid_index-1]:
        return mid_index

    # After checking that the mid is gt the previous number and lt next number
    # compare the first and mid numbers if they are sorted then the min will 
    # be located in the right part (next to mid)
    if input_list[start] < input_list[mid_index]:
        return find_index_of_min_number(input_list, mid_index+1, end)

    # if the mid and the start element not sorted then look up 
    # for the min in the left part (previous to mid)
    else:
        return find_index_of_min_number(input_list, start, mid_index-1)



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


# cases that got me discovered the base cases to find min of rotated sorted array
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 6])
test_function([[7, 8, 9, 10, 1, 2, 3, 4, 5, 6], 1])

test_function([[10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0])

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 600])
test_function([[2, 3, 4, 5, 6, 7, 0, 1], 0])
test_function([[2, 3, 4, 5, 6, 7, 0], 0])
