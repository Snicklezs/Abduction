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
		print "Note: Type hint if you're ever truly stuck.",
		print N 
	
		option = raw_input("> ").lower() 
	
		if option in ("look around", "observe"): 
			print N 
			print "The room is almost pitch black - a small, shiny, inanimate"
			print "object can be made out to your left, just within reach."
			RoomZero1()
			break 
		elif "hint" in option: 
			hint("You should probably look around")
	
def RoomZero1():
	""" 1-100 == RoomZero Success ; Failure results in dead function """ 
	print N 
	print "You can try and grab the 'shiny object'"
	print "Type a number between 1-200"
	print N 

	guess = int(raw_input("> ")) 
	
	if guess in range(1, 100):
		print N 
		print "Your number was: %d" % guess 
		print "You're in luck... You've successfully obtained a small knife!" 
		ItemList('small knife', True) 
		RoomZeroSuccess() 
	elif guess in range(100, 200):
		dead("You clumsily drop the scissors like a true Mongoloid.") 
		
def RoomZeroSuccess():
	""" May add a while loop here """ 
	while True:
		print N
		print "You can't waste any more time... The footsteps are getting closer." 
		print N 
	
		escape = raw_input("> ").lower()  
	
		if "cut straps" in escape: 
			print N 
			print "You successfully escaped your bonds:"
			print "A human voice is terriffingly close;",
			print "use your intuition to not get caught..."
			RoomZeroEscaped()
			break l;',
			
		elif "cut ties" in escape: 
			print N 
			print "You successfully escaped your bonds:"
			print N 
			print "A human voice is terriffingly close;",
			print "use your intuition to not get caught..."
			RoomZeroEscaped() 
			break 
			
def RoomZeroEscaped():
	""" We need to plan some fun/hard stuff here! A while loop may be in order! """
	while True:
		print N 
		
		#########################################
		# Having some issues here with north,   #
		# Hide in locker must be local to north #
	    #########################################
		
		choice = raw_input("> ").lower() 
	
		if choice in ("look around, observe"):
			observe("A locker", " A locked door", "A chair", " A flashing red light")
		if choice in ("walk north", "go north", "north"):
			print N 
			north("A locker stands tall infront of you, the lock has been unlocked")
		if choice in ("hide in locker", "climb in locker", "get in locker", "hide") and AtLocker == True:
			print N 
			print "You climb into the locker..."
			print "After about a minute the door bursts open wildly, a human... A dirty disgusting",
			print "ugly god dammed human!"
			print "You watch as he throws down a document and storms out - phew - good thing he didn't notice you were MIA."
			print "You get out of the locker. It appears that he slammed the document down towards the west by a"
			print "table next to the strobing light" 
		elif choice in ("walk east", "go east", "east"):
			print N 
			east("A door presents itself... You give it a shove but it's no use - you'll have to find the key") 
		elif choice in ("walk south", "go south", "south"):
			print N 
			south("A chair sits here... A small key sits on it...")  
		elif choice in ("walk west", "go west", "west"):
			print N 
			west("A strobing emergency light beams off the wall, providing the little light there is.")
			
	
###############################################################################
#                  Anything under here is globally used                       #            
#                  Testing an inventory appender                              #                                                                          
############################################################################### 

def ItemList(Object, True):
	""" still testing """ 
	ItemList = []
	
	# displays users items 
	if True == False:
		print N 
		print "Here's your inventory:"
		print "%s" % ItemList 
	# well append object to ItemList  	
	elif True == True:
		print N 
		print "Adding 1 %s to your inventory." % Object 
		ItemList.append(Object)			
	elif True == remove:
		print N 
		print "Removing %s from your list." % Object 
		ItemList.remove(object) 
		
def hint(hint):
	""" Provides a hint to the user """ 
	print N 
	print "Here's a hint: ", hint 
	
def dead(why):
	""" Kills the program when user dies """ 
	print N 
	print "Good job!jbhk", why 
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

		
Introduction() 
