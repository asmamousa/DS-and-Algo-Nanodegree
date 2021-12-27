def mergesort(input_list):
    if len(input_list) <= 1:
        return input_list
    
    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)

def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def get_two_max_sums(sorted_list):

    # Extract the number of digits for each number
    num_of_digits_for_first_num = len(sorted_list)//2
    num_of_digits_for_second_num = len(sorted_list) - num_of_digits_for_first_num

    num_one = num_two = 0
    end_index = len(sorted_list)-1

    # the keys are 1, -1 in order to switch between them after each itertion
    # in the while loop
    target_number = {1: num_one,
                  -1: num_two  
                  }

    target_num_of_digits = {1: num_of_digits_for_first_num,
                            -1: num_of_digits_for_second_num  
                            }

    # Start with index -1 since it's represents the key for num_two in both dict
    index = -1
    while end_index >= 0:
        num = sorted_list[end_index]
        target_number[index] += num * (pow(10, target_num_of_digits[index]-1))
        target_num_of_digits[index] -= 1
        end_index -= 1

        # switch to another num key. If the current iteration is performed on num_two
        # then the next will be on num_one and vise verca
        index *= -1

    return target_number[1], target_number[-1]


def rearrange_digits(input_list):
    if input_list is None:
        return 

    if len(input_list) <= 1:
        return input_list

    # sort the list
    sorted_list = mergesort(input_list)

    return get_two_max_sums(sorted_list)


    
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[3, 7, 4, 9, 1, 3, 1], [9431, 731]])
test_function([[3], [3]])
test_function([[], []])
print(rearrange_digits(None))
# returns None