from sys import exit
 
Author = "William DeBattista"
Email = "williamsecord@hotmail.com" 

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
	print "in response to their act of savagery, the race of X-52"
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
	""" Here you begin your adventure, your goal is to get to RoomZero1 by grabbing the 'shiny
		object' """  
	
	while True:
		print N 
		print "Ding! " * 5
		print "The sound of a ringing alarm violates your ears."
		print "As you begin to gather your senses - you realize what has happened."
		print "Panic-stricken you try to get up, but your torso has been strapped",
		print "down."
		print N 
		print "What are you going to do? You hear someone coming..."
		print "Note: Type hint if you're truly stuck.",
		print N 
	
		option = raw_input("> ").lower().split()
	
		if 'look' in option:
			print N 
			print "The room is almost pitch black - a small, shiny, inanimate"
			print "object can be made out to your left, just within reach."
			RoomZero1()
		
		elif 'observe' in option:
			print N 
			print "The room is almost pitch black - a small, shiny, inanimate"
			print "object can be made out to your left, just within reach."
			RoomZero1()
		
		elif "hint" in option: 
			hint("You should probably look around")
		
		else:
			dead("Way to go! Jack-Ass!")
	
def RoomZero1():
	""" 1-100 == RoomZero Success ; Failure results in dead function """ 
	
	print N 
	print "You can try and grab the 'shiny object'"
	print "Type a number between 1-200"
	print N 

	guess = (raw_input("> ")) 
	
	if guess in range(1, 100):
		print N 
		print "Your number was: %d" % guess 
		print "You're in luck... You've successfully obtained a small knife!" 
		ItemList('small knife', True)
		RoomZeroSuccess() 
	
	elif guess in range(100, 200):
		dead("You clumsily drop the knife like a true Mongoloid.") 
	
	else:
		dead("Typing a number between 1 and 200... I didn't think you could make that hard.") 
		
def RoomZeroSuccess():
	""" May add a while loop here """ 
	
	while True:
		
		print N
		print "You can't waste any more time... The footsteps are getting closer." 
		print N 
	
		escape = raw_input("> ").lower().split() 
	
		if "cut" in escape: 
			print N 
			print "You successfully escaped your bonds:"
			print "A human voice is terriffingly close;",
			print "use your intuition to find a spot and HIDE!"
			RoomZeroEscaped()
		
		else:
			dead("Try cutting something next time.") 

			
def RoomZeroEscaped():
	""" We need to plan some fun/hard stuff here! A while loop may be in order! """
	cz
	# 1.) Once hidden == True; 'hide' will no longer run. 
	# 2.) Once getkey == True; 'get key' will no longer run. 
	# 3.) locker Bool will stop player from being able to hide while they're not
	# 3.) at the locker. 
	
	locker = False 
	getkey = False 
	hidden = False 
	
	while True:
	
		print N 
		choice = raw_input("> ").lower().split() 
		
		if "look" in choice:
			observe("A locker", " A locked door", "A chair", " A flashing red light")
			getkey = False
			locker = False 
			
		elif "north" in choice:
			print N 
			north("A locker stands tall infront of you, the lock has been unlocked")
			locker = True
			getkey = False 
			
		elif "east" in choice:
			print N 
			east("A big iron door with an electronic lock... ") 
			getkey = False
			locker = False 
			unlock('electronic key') 
			
		elif "south" in choice:
			print N 
			south("A chair sits here... A small key sits on it...")
			getkey = True 
			locker = False 
		
		elif "west" in choice:
			print N 
			west("A strobing emergency light beams off the wall, providing the little light there is.")
			getkey = False 
			locker = False 
		
		elif "hide" in choice and locker == True and hidden == False:
			print N 
			print "You climb into the locker..."
			print "After about a minute the door bursts open wildly, a human... A dirty disgusting",
			print "ugly god dammed human!"
			print "You watch as he throws down a document and storms out - phew - good thing he didn't notice you were MIA."
			print "You get out of the locker. It appears that he slammed the document down towards the west by a"
			print "table next to the strobing light" 
			hidden = True 
		
		elif "hide" in choice and locker == False:
			print "" 
		
		elif "key" in choice and getkey == True:
			print N 
			print "You pick up an' electronic key, this looks like it might be useful!"
			ItemList('electronic key', True) 
			
		elif "key" in choice and getkey == False:
			print ""
			
		else:
			dead("I've never seen anyone screw up that badly before") 
			
###############################################################################
#                  Anything under here is globally used                       #            
#                  Testing an inventory appender                              #                                                                          
############################################################################### 

def ItemList(self, True):
	""" still testing """ 
	ItemList = []
	
	# displays users items 
	if self == "" and True == False :
		print N 
		print "Here's your inventory:"
		print "%s" % ItemList 
	
	# well append object to ItemList  	
	elif True == True:
		print N 
		print "Adding %s to your inventory." % self 
		ItemList.append(self)
	else:
		ItemList.remove(self) 
		
	return ItemList
			
def hint(hint):
	""" Provides a hint to the user """ 
	print N 
	print "Here's a hint: ", hint 
	
def dead(why):
	""" Kills the program when user dies """ 
	print N 
	print "Good job!", why 
	print "Try again."
	exit(0) 
	
def observe(No, Ea, So, We):
	print N
	print "You observe your surroundings:"
	print "To your North is: ", No 
	print "To your East is: ", Ea 
	print "To your South is: ", So 
	print "To your West is: ", We 
	
def north(self):
	print "You are now north:", self 
	
def east(self):
	print "You are now East:", self 
	
def south(self):
	print "You are now South:", self 

def west(self): 
	print "You are now West:", self 
	
def unlock(key):
		print N 
		self = raw_input("This door can be opened - Enter the name of the key to open the door: ").lower() 
		
		if key and self == "electronic key":
			print "Good job"
			
Introduction() 

