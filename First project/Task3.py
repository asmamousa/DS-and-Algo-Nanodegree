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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# I looked up for information about all the built-in functions that were used in this code.
# Part A:
def get_recieving_number(calls_list):

	for call in calls_list:
		caller_number = call[0]
		if caller_number.find('(080)') != -1:
			yield call[1]

def extract_recieving_prefixes(calls_list):
	list_of_prefixes = list()

	for number in get_recieving_number(calls_list):
		# check if it's fixed line
		if number.find('(') == 0:
			index = number.index(')')
			code = number[1:index]
			list_of_prefixes.append(code)

		# checks if mobile number
		elif len(number.split(" ")) == 2:
			if int(number[0]) in [7, 8, 9]:
				code = number[0:4]
				list_of_prefixes.append(code)
			

	return list_of_prefixes

def get_count_of_phone_calls(calls_list, caller_code, reciever_code):
	count = 0

	for i in range(len(calls_list)):
		caller_number = calls_list[i][0]
		reciever_number = calls_list[i][1]
		if (caller_number.find(caller_code) != -1) and (reciever_number.find(reciever_code) != -1):
			count+=1

	return count

prefixes = extract_recieving_prefixes(calls)
set_of_prefixes = set(prefixes)
sorted_prefixes = sorted(set_of_prefixes)
print ("The numbers called by people in Bangalore have codes:")
for i in range(len(sorted_prefixes)):
	print ("{}".format(sorted_prefixes[i]))


# Part B:
from_Bangalore_to_Bangalore = get_count_of_phone_calls(calls, '080', '080')
from_Bangalore_to_all = len(prefixes)
print ("{:.2f}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
	.format( (from_Bangalore_to_Bangalore/from_Bangalore_to_all)*100 ) )




