#### Abduction V2 #### 

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
	print "Type hint if you ever need a refresher on some of the commands that are available." 
	print "Press ENTER to continue" 
	print N 
	
	CONTINUE = raw_input('> ') 
	roomOne() 
	
def roomOne():
	""" Escape by flipping the switch, once you are no longer trapped you will be able to exit roomOne """ 
	
	foodBrick = False 
    
	print N 
	print "You wake up from a deep coma - lightning like bars engulf you from making any escape."
	print "It hits you like a Spratnuk folly ball; You've been abducted."
	print "Using your intuition; You must escape." 
	print N 
	
	while True:
		
		option = raw_input("> ").lower().split()

		if 'look' in option:
			print N 
			print "=" * 70
			observe('An electronic switch mounted on the wall', ' A brick of something, presumed to be food', 'A wall - Appears to be of no signifigance', ' A locker')
			print "=" * 70
			print N 
			
		elif 'north' in option and foodBrick is True:
			print N 
			north("You stare at the switch, then at your hefty brick of grossness...\nLooks like this is the only way...")
			print N 
			throwFood() 
			
		elif 'north' in option:
			print N 
			print "You peer through the vibrant electricity towards the northside wall - Wondering what signifigance the switch holds."
			print N 
		
		# foodBrick bool should be determined on user input in getfood
		elif 'east' in option and foodBrick is False:
			print N 
			east("A brick of food lays here, it looks disgusting.") 
			getFood() 
			foodBrick = True 
			print N 
		
		elif 'east' in option and foodBrick is True:
			print N 
			east("A brick of food used to lay here... Now it's just a grimy floor")
			print N 
			
		elif 'south' in option:
			print N 
			south("A wall... You should probably quit wasting time.") 
			
		elif 'west' in option:
			print N 
			west("A locker stands tall next to the west-end wall, you wonder what's inside it") 

# Need to change dead for 'n' in getbrick to print something different. and then somehow change getbrick bool from inside this function 			
def getFood():
	print N 
	print "Do you want to append 'food brick' to your personell (no bad will come of it)?: Y/N"
	print N
	
	getBrick = raw_input("> ").lower().split() 
	
	if 'y' in getBrick:
		print N 
		print "You append %s to your personell" % 'food brick' 
	
	elif 'n' in getBrick:
		dead("Pick it up next time - This is a bug at the moment - Will fix soon") 
		
	else:
		dead("You're now dead because you couldn't make a simple decision") 
		
def throwFood():
	print "A good throw could get you outta here."
	print N 
	
	throw = raw_input("> ").lower().split()
	
	if 'throw' in throw: 
		print N 
		print "Good job! The switch has been turned off and the bars surrounding you are no more!" 
		print N 
		print "You are now free to explore the room - though it looks pretty dead... Perhaps the locker might contain something useful." 
		print N 
	
	else:
		dead("You fumble around and die - Cause unknown - But we do know you're an' idiot")
		
def RoomEscaped():
	""" You are now escaped - Go to the locker and grab the code for the door """ 
	
	escaped = raw_input("> ").lower().split() 
	locker = False 
	
	while True:
	
		if "north" in escaped:
			north("The switch is now switched ON. A door is next to the switch, it appears to require some sort of code") 
		
		elif "east" in escaped:
			east("A bare wall is here") 
		
		elif "south" in escaped:
			south("Another wall - What do ya expect it's a prison cell") 
		
		elif "west" in escaped and locker is False:
			west("A locker stands tall on the west-side wall, fortunately their appears to be no lock") 
			Locker() 
			locker = True 
			
def Locker():
	
	open = raw_input("> ").lower().split() 
	while True:
		if 'open' in open:
			print N 
			print "You open the locker - A strange document presents itself, it reads:"
			print "1001 starting from left to right add 1s as powers of 2"
		else:
			print N 
			print "" 
			
###############################################################################
#                  Anything under here is globally used                       #            
#                  Testing an inventory appender                              #                                                                          
###############################################################################
	
def dead(why):
	""" Kills the program when user dies """ 
	print N 
	print "Good job!", why 
	print "Try again."
	exit(0) 
	
def observe(No, Ea, So, We):
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
	
def inventory(self, True): 
	iventory = [] 
	
	if True == True: 
		print "Adding '%s' to your inventory." % self 
		iventory.append(self) 
		
	elif True == False: 
		print "Removing %s from your inventory." % self 
		inventory.remove(self) 
		
	else:
		dead("")  	
	
	
Introduction()
