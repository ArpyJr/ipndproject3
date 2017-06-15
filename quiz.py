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
The caterpillar eats for several days until it is ready to make a cocoon.
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
medium_paragraph_words = ['beach', 'snorkeling', 'fish', 'scuba']


#difficulty -----hard-----
hard_paragraph = """
David Bowie is a music icon who has influenced generations of musicians.
He was born David ___1___ Jones in 1948, and quickly went on to become an influential figure in the music world.
Bowie's first major hallmark was his album 'The Rise and Fall of ___2___ Stardust and the Spiders From Mars.'
From that point, Bowie continued to reinvent himself with characters like ___3___ Sane and the Thin White Duke,
and redefined the ___4___ through the ages. Bowie was known for his creative flexibility, and for his range of styles, 
from glam ___5___ to pop and experimental industrial in his 'Tin Machine' period. Bowie was awarded five posthumous 
awards for his latest album '___6___' after his tragic passing in 2016.

"""
hard_paragraph_words = ['Robert', 'Ziggy', 'Aladdin', 'genre', 'rock', 'Blackstar']



#function declaration ------------------------------- START -------------------------------
#declaration for functions that will be called by game_engine function
def paragraph_set():
#this function sets paragraph so that other functions can
#refer to those variables and does not require if, elif, or else statements
	if difficulty == 'easy':
		return easy_paragraph
	elif difficulty == 'medium':
		return medium_paragraph
	else:
		return hard_paragraph

def words_list_set():
#this function sets words_list so that other functions can
#refer to those variables and does not require if, elif, or else statements
	if difficulty == 'easy':
		return easy_paragraph_words
	elif difficulty == 'medium':
		return medium_paragraph_words
	else:
		return hard_paragraph_words

def enterWord(current_missing_word):
#this function will prompt the user to enter a replacement word for the missing word
#example : Please enter a word for ___1___
#then it will return a word that the user entered
	return raw_input('Enter a word for ' + current_missing_word + ' ')


#function declaration ------------------------------- END -------------------------------


#game engine -------------------------------START -------------------------------
def game_engine():
	paragraph = paragraph_set()
	words_list = words_list_set()
	end_quiz_location = len(words_list)
	current_quiz_location = 1
	current_missing_word = '___' + str(current_quiz_location) + '___'
	#this sets the value for when the game should end
	while current_quiz_location < end_quiz_location + 1:
	#while loop will run for the number of words that are missing in the paragraph
	#for each loop, it should print out a paragraph without the current and later words
	#but it should include previous words answered
		print paragraph
		replacement_word = enterWord(current_missing_word).lower()
		#prompts the user to enter the missing word
		if replacement_word == words_list[current_quiz_location - 1].lower():
			print ''
			print 'Correct!'
			paragraph = paragraph.replace(current_missing_word, words_list[current_quiz_location - 1])
			current_quiz_location += 1
			current_missing_word = '___' + str(current_quiz_location) + '___'
		else:
			print ''
			print 'Please try again'
	print paragraph
	return 'You won! Thank you for playing!'


print game_engine()