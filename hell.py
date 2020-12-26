from sys import exit

def hell_room():
	print """
    You have entered Hell. Say Hello to Satan. He wants to play a game. If
	you roll an odd number, you serve him for eternity. If you roll an even
	number, you live. Roll the dice..."""
    
    import random
    
    print "Roll the dice"
        next = raw_input("> ")
        
        if "roll" or "roll dice" in next:
        
        dice = random.randint(1,6)
        
        print "You rolled a %s" % dice


def start_room():
    print """
    You have entered the puzzle room. Choose your challenge to free yourself 
    from certain death. Which door do you choose?
    """
    door = raw_input("> ")
    
    if "1" in door:
        math_puzzle()
    elif "2" in door:
        literature_puzzle()
    elif "3" in door:
        psych_puzzle()
    else:
        hell_room()


def math_puzzle():
    print """
    So, you have chosen to try your hand at math. Good luck and here is your problem:
    
    You have 