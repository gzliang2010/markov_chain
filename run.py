from markov_python.cc_markov import MarkovChain
from fetch_data import fetch_data
import pickle
import os

def database_builder(markov_text):
	trainning = True
	while trainning:
		link=raw_input("Enter a link of the data (webpage or local file): ")
		raw_data = fetch_data(link)
		markov_text.add_string(raw_data)
		print len(markov_text.lookup_dict)
		flag = raw_input("Continue? Y/N: ").upper()
		if flag == "N":
			trainning = False
		elif flag == "Y": 
			pass
		else:
			flag = raw_input("Invalid input! Please enter 'Y' or 'N': ").upper()

	with open("lookup_dict.txt", "w") as fl:
		# save the database into a external file
		pickle.dump(markov_text.lookup_dict, fl)


mctext = MarkovChain(2)
# Initialize mctext.lookup_dict using the existing database.
if os.path.getsize("lookup_dict.txt") != 0:
	with open("lookup_dict.txt", "r") as fl:
		# restore the database
		mctext.lookup_dict = pickle.load(fl)
else:
	# In case lookup_dict.txt is empty.
	print "The database is empty, let's build it."
	database_builder(mctext)
	print "Length of initial lookup_dict: %d" %len(mctext.lookup_dict)

# Add more data to the database if you want.
train = raw_input("Continue to build the database? (Y/N): ").upper()
if train == "Y":
	database_builder(mctext)
	
print "\nLength of Final lookup_dict: %d\n" %len(mctext.lookup_dict)

gen = True
while gen:
	num = int(raw_input("How many words you want to generate: "))
	print "Here you go:"
	text = mctext.generate_text(num)
	text = ' '.join(text)
	print unicode(text, 'utf-8')

	if raw_input("Continue? (Y/N): ").upper() == "N": 
		gen = False