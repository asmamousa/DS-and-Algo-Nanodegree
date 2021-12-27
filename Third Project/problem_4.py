def sort_012(input_list):

    if input_list is None:
        return

    if len(input_list) <= 1:
        return input_list
        
    pos0_index = 0
    pos2_index = len(input_list)-1
    left = 0

    while left <= pos2_index:
        if input_list[left] == 0:
            if input_list[pos0_index] != 0:
                input_list[left] = input_list[pos0_index]
                input_list[pos0_index] = 0
            pos0_index += 1
            left += 1

        elif input_list[left] == 2:
            if input_list[pos2_index] != 2:
                input_list[left] = input_list[pos2_index]
                input_list[pos2_index] = 2
            pos2_index -= 1

        else:
            left += 1


    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
print (sort_012([0]))
print (sort_012(None))

