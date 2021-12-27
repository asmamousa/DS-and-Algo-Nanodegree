class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        self.tail.next = Node(value)
        self.tail = self.tail.next



def convert_linked_list_values_to_set(list_head):
    out_set = set()
    temp = list_head
    while temp:
        out_set.add(temp.value)
        temp = temp.next

    return out_set

def union(llist_1, llist_2):

    if llist_1 is None and llist_2 is None:
        return

    if llist_1 is None and llist_2:
        return llist_2

    if llist_2 is None and llist_1:
        return llist_1

    set_of_values1 = convert_linked_list_values_to_set(llist_1.head)
    set_of_values2 = convert_linked_list_values_to_set(llist_2.head)
    union_result = LinkedList()
    
    for value in set_of_values1:
        union_result.append(value)

    for value in set_of_values2:
        if value not in set_of_values1:
            union_result.append(value)

    return union_result

    

def intersection(llist_1, llist_2):

    if llist_1 is None and llist_2 is None:
        return

    if llist_1 is None and llist_2:
        return llist_2

    if llist_2 is None and llist_1:
        return llist_1

    intersection_result = LinkedList()
    set_of_values1 = convert_linked_list_values_to_set(llist_1.head)
    set_of_values2 = convert_linked_list_values_to_set(llist_2.head)


    for value in set_of_values1:
        if value in set_of_values2:
            intersection_result.append(value)

    return intersection_result


linked_list = LinkedList()
linked_list.append(3)
linked_list.append(7)
linked_list.append(9)
linked_list.append(12)

linked_list2 = LinkedList()
linked_list2.append(5)
linked_list2.append(9)
linked_list2.append(11)
linked_list2.append(12)
linked_list2.append(3)

# Note: the results will be printed out in diffferent order for each run because I used set
# test case 1:
result1 = union(linked_list, linked_list2)
print (str(result1))
# returns a linked list of 3,7,9,12,5,11 

result2 = intersection(linked_list, linked_list2)
print (str(result2))
# returns a linked list of 3,9,12 



# test case 2: None values
# when list 1 is None and list 2 has nodes
result3 = union(linked_list, None)
print (str(result3))
# returns a linked list of 3,7,9,12

# when list 2 is None and list 1 has nodes
result3 = union(None, linked_list2)
print (str(result3))
# returns a linked list of 5,9,11,12,3 




# test case 3: no intersect
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)

linked_list2 = LinkedList()
linked_list2.append(2)
linked_list2.append(4)
linked_list2.append(6)
linked_list2.append(8)
linked_list2.append(10)

result4 = union(linked_list, linked_list2)
print (str(result4))
# returns a linked list of 1,3,5,7,2,4,6,8,10

result5 = intersection(linked_list, linked_list2)
print (str(result5))
# returns None


# test case 4: two linked lists have the same nodes
linked_list = LinkedList()
linked_list.append(90)
linked_list.append(80)
linked_list.append(70)
linked_list.append(60)

linked_list2 = LinkedList()
linked_list2.append(90)
linked_list2.append(80)
linked_list2.append(70)
linked_list2.append(60)

result6 = union(linked_list, linked_list2)
print (str(result6))
# returns a linked list of 90,80,70,60 



# test case 5: two linked lists that has duplicates
linked_list = LinkedList()
linked_list.append(2)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(4)
linked_list.append(10)

linked_list2 = LinkedList()
linked_list2.append(90)
linked_list2.append(80)
linked_list2.append(70)
linked_list2.append(60)
linked_list2.append(60)
linked_list2.append(70)
linked_list2.append(10)
linked_list2.append(4)

result7 = union(linked_list, linked_list2)
print (str(result7))
# returns a linked list of 10,2,3,4,70,80,90,60 

result8 = intersection(linked_list, linked_list2)
print (str(result8))
# returns a linked list 10,4