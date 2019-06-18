# Create a robot that will always win the game. Your robot will always go first. 
# The function should take an integer and returns 1, 2, or 3.

def make_move(sticks):
    i = 2
    for i  sticks:
        sticks = sticks - i
        i = input('Input number 1>=3: ')  
    return sticks
make_move(3)