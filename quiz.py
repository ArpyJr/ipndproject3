# ****** Comments are made below the entry that it is describing.

def onLoad():
#function to run on load. If user input is invalid, then function will run until
#user enters a valid input; Easy, Medium, or Hard
	print 'Please choose a difficulty "easy" / "medium" / "hard"'
	difficulty = raw_input('choose difficulty ')
	#difficulty stores user input
	diff = difficulty.lower()
	#diff converts difficulty to lower case
	if diff == "easy":
		print 'You chose ' + diff + '!'
		return diff
	elif diff == "medium":
		print 'You chose ' + diff + '!'
		return diff
	elif diff == "hard":
		print 'You chose ' + diff + '!'
		return diff
	else:
		onLoad()
		#if user does not input a valid response then user is thrown
		#back to the beginning of the onLoad function

difficulty = onLoad()
#runs onLoad function and stores difficulty in variable 'difficulty'

#difficulty -----easy-----
easy_paragraph = """
Butterflies are amazing creatures. Their life cycles has four stages.
They begin life as an ___1___. The egg hatches and a ___2___ emerges.
The caterpillar eats for several days until it is ready to make a coccoon.
The caterpillar gestates inside the ___3___ and eventually re-emerges as a beautiful butterlfy.
The ___4___ will go on to feed and pollinate flowers.
"""
easy_paragraph_words = ['egg', 'caterpillar', 'cocoon', 'butterfly']


#difficulty -----medium-----
medium_paragraph = """
The ___1___ is a favourite summer spot for many, and there are plenty of options for what to do.
If you're in tropical waters, you may enjoy ___2___, as almost any level swimmer can take part.
You'll be able to see lots of ___3___ and enjoy the clear waters.
If you're feeling brave, you might try guided ___4___ diving.
Explore the depths and see hidden treasures and wild sea life not accesible at the surface.
"""
medium_paragraph_words = ['beach', 'snorkeling', 'fish', 'scooba']


#difficulty -----hard-----
hard_paragraph = """
David Bowie is a music icon who has influenced generations of musicians.
He was born David ___1___ Jones in 1948, and quickly went on to become an influential figure in the music world.
Bowie's first major hallmark was his album 'The Rise and Fall of ___2___ Stardust and the Spiders From Mars.'
From that point, Bowie continued to reinvent himself and redefine the ___3___ through the ages.
Bowie was awarded five posthumous awards for his latest album '___4___' after his tragic passing in 2016.
"""
hard_paragraph_words = ['Roberts', 'Ziggy', 'genre', 'Blackstar']


def returnParagraph():
#this function will return the paragraph corresponding to the diffuculty
#that the user has chosen. It will also return modified paragraph as
#user continues to guess the missing words.
	if difficulty == 'easy':
		return easy_paragraph
	elif difficulty == 'medium':
		return medium_paragraph
	else:
		return hard_paragraph
print returnParagraph()

current_quiz_location = 1
#location of the current missing word. It is used to calculate current_missing_word
current_missing_word = '___' + str(current_quiz_location) + '___'

print current_missing_word

def enterWord():
#this function will prompt the user to enter a replacement word for the missing word.
#example : Please enter a word for ___1___
#then it will return a word that the user entered.
	replacement_word = raw_input('Enter a word for ' + current_missing_word)