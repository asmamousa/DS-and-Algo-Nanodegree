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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# I looked up for information about all the built-in functions that were used in this code.

def get_callers_set(calls_list):

	callers_set = set()

	for caller in calls_list:
		callers_set.add(caller[0])

	return callers_set

def get_receivers_set(calls_list):
	receivers_set = set()

	for receiver in calls_list:
		receivers_set.add(receiver[1])

	return receivers_set

def get_senders_set(texts_list):
	sender_set = set()

	for sender in texts_list:
		sender_set.add(sender[0])

	return sender_set

def get_text_receives_set(texts_list):
	text_receives_set = set()

	for receiver in texts_list:
		text_receives_set.add(receiver[1])

	return text_receives_set


def get_set_of_possible_telemarketers():
	set_of_possible_telemarketers = set()

	# first step -> caller but didn't receive any calls
	caller_set = get_callers_set(calls)
	receivers_set = get_receivers_set(calls)

	set_of_possible_telemarketers = (caller_set.union(receivers_set)) - receivers_set

	# second step -> what we got for now but not text senders.
	sender_set = get_senders_set(texts)
	set_of_possible_telemarketers = set_of_possible_telemarketers.union(sender_set) - sender_set

	# third step -> what we got for now but not text receivers.
	text_receives_set = get_text_receives_set(texts)
	set_of_possible_telemarketers = set_of_possible_telemarketers.union(text_receives_set) - text_receives_set

	return set_of_possible_telemarketers

set_of_possible_telemarketers = get_set_of_possible_telemarketers()
sorted_set = sorted(set_of_possible_telemarketers)

print ("These numbers could be telemarketers: ")
for i in sorted_set:
	print ("{}".format(i))





