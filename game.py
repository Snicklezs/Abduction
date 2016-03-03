from sys import exit 

def Introduction():
	""" Introduction to the game """ 
	global N 
	N = "\n" 
	
	print N 
	print "=" * 27
	print "Welcome to abduction."
	print "=" * 27
	print "ENTER to CONTINUE"
	print "CNTRL-Z at any time to EXIT"
	print "=" * 27
	print N  
	
	CONTINUE = raw_input("> ") 
	Opening()
 	
def Opening(): 
	""" Background story for the Human Race and Spratnuk """ 
	print N 
	print "Year, 4022"
	print "Planet, X-52" 
	print N 
	print "About 1000 years ago the human race had their home"
	print "planet destroyed by planet X-52 during the war."
	print "You're probably asking yourself the following question: Why?"
	print "Well around the year 2900 planet Earth had almost completely"
	print "depleted their resources (the biggest resource being their water)"
	print "So being the greedy consumers humans have always been; they seeked"
	print "a new planet with more resources, so in the year 3000 they"
	print "forcibly attempted to take our beautiful planet (X-52),"
	print "in response to their display of savagery, the race of X-52"
	print "Waged a full blown war, blowing up the humans home planet"
	print "In the process."
	print N 
	print "Ever since the Human Race and the Spratnuk Race of X-52 have been at war."
	print "The humans have stopped at no lengths to inflitrate X-52's security."
	print "Abductions are not uncommon, and our naive youth are their biggest target..."
	print N 
	print "Press ENTER to continue" 
	print N 
	
	CONTINUE = raw_input("> ") 
	RoomZero() 
	


def RoomZero():
	""" Here you begin your adventure, your goal is to escape from the room """  
	print N 
	print "Ding! " * 5
	print "The sound of a ringing alarm violates your ears."
	print "As you begin to gather your senses - you realize what has happened."
	print "Panic-stricken you try to get up, but your torso has been strapped",
	print "down."
	print N 
	print "What are you going to do? You hear someone coming..."
	print N 
	print "Note: Type hint if you're ever truly stuck.",
	print "Just keep in mind this will take you back to the introduction."
	print N 
	
	option = raw_input("> ")
	
	if "hint" in option:
		hint("Look around.")
		Introduction() 
	elif "look around" in option: 
		print N 
		print "The room is almost pitch black - a small, shiny, inanimate"
		print "object can be made out to your left, just within reach."
		RoomZero1() 
	elif "Look around" in option: 
		print N 
		print "The room is almost pitch black - a small, shiny, inanimate"
		print "object can be made out to your left, just within reach."
		RoomZero1() 
	else:
		print hint("Look around")
		Introduction()

def RoomZero1():
	print N 
	print "You can try and grab the 'shiny object', however, this could",
	print "prove to be dangerous."
	print "Type a number between 1-200"
	print N 
	
	guess = int(raw_input("> ")) 
	
	# More than 1 lessar than 100 
	if 0 < guess < 100:
		print N 
		print "Your number was: %d" % guess 
		print "You're in luck... You've successfully obtained a small knife!" 
		ItemList('small Knife', True) 
	# greater than 100, lessar than 200 
	elif 101 < guess < 201:
		print "Fail"
	else:
		hint("You must type a number between 100 and 200") 
		



# Anything under here is globally used 
# Testing an Inventory appender 
# May need to set up a way to RM all elements of the list for when game resets 	
def ItemList(Object, True):
	""" Item appender/Inventory checker, still being tested """ 
	ItemList = []
	
	if True == False:
		print "Here's your inventory:"
		print "%s" % ItemList 
		
	elif True == True:
		print "Adding %s to your inventory" % Object 
		ItemList.append(Object) 

	
				
def hint(hint):
	print N 
	print "Here's a hint: ", hint 
	Introduction() 
	
def dead(why):
	print N 
	print "Good job! ", why 
	exit(0) 
	
Introduction() 
