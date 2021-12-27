"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def get_max_time_spent_and_phone_number(list_of_calls, phone_number=0):
	# index 2 refers to date_time, while index 3 refers to duration in seconds
	out_dict = {}

	for call in list_of_calls:
		date_time = call[2]
		if date_time.find("09-2016") != -1:
			out_dict[call[0]] = out_dict.get(call[0], 0) + int(call[3])
			out_dict[call[1]] = out_dict.get(call[1], 0) + int(call[3])


	max_duration_key = max(out_dict, key=out_dict.get)

	return out_dict[max_duration_key], max_duration_key

total_time, phone_number = get_max_time_spent_and_phone_number(calls)
print ("'{}' spent the longest time, '{}' seconds, on the phone during September 2016."
	.format(phone_number, total_time))