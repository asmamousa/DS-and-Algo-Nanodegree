"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def get_telephone_numbers_from_list(input_list):
	for i in range(len(input_list)):
		yield input_list[i][0], input_list[i][1]
		

def get_count_of_telephone_numbers(list1, list2):
	set_of_nummers = set()

	for number_one, number_two in get_telephone_numbers_from_list(list1):
		set_of_nummers.add(number_one)
		set_of_nummers.add(number_two)

	for number_one, number_two in get_telephone_numbers_from_list(list2):
		set_of_nummers.add(number_one)
		set_of_nummers.add(number_two)

	return len(set_of_nummers)

output = get_count_of_telephone_numbers(texts, calls)
print ("There are '{}' different telephone numbers in the records.".format(output))