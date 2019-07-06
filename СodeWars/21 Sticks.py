# Create a robot that will always win the game. Your robot will always go first. 
# The function should take an integer and returns 1, 2, or 3.

def make_move(sticks):
    bro = sticks % 4
    if bro != 0:
        return bro
    else:
        return 1

# //////////////////////////////////////////////

def makeMove(sticks):
    return max(sticks % 4, 1)

# /////////////////////////////////////

def makeMove(sticks):
    return sticks % 4 or 1