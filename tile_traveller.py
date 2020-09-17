#Þurfum að bjóða notanda möguleika n/s/e/v
#hann velur eitthvað af möguleikunum og færist um reit
#þá fær hann aftur boð um möguleika
#ef hann velur eh sem er ekki möguleiki fær hann invalid direction
#þá fær hann aftur boð um möguleika
#forritið þarf að vita í hvaða reit leikmaður er í svo hann geti
#boðið honum rétta möguleika.
#leikmaður byrjar í reit 1.1

POSITION = 1.1
NORTH = 'n' or 'N'
SOUTH = 's' or 'S'
WEST = 'w' or 'W'
EAST = 'e' or 'E'

def new_position(value):
    '''Takes in a direction input from user and returns new position'''
    if value == NORTH:
        POSITION += 0.1
    elif value == SOUTH:
        POSITION -= 0.1
    elif value == WEST:
        POSITION -= 1.0
    elif value == EAST:
        POSITION += 1.0
    return POSITION


direction = input('Direction: ')
present_position = new_position(direction)
options = options(present_position)

def options(position):
    if POSTION == 1.1:
        print("You can travel: (N)orth.")
    elif POSTION == 1.2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif POSTION == 1.3:
        print("You can travel: (E)ast or (S)outh.")
    elif POSTION == 2.1:
        print("You can travel: (N)orth.")
    elif POSTION == 2.2:
        print("You can travel: (N)orth or (S)outh or (W)est.")
    elif POSTION == 2.3:
        print("You can travel: (E)ast or (W)est.")
    elif POSTION == 3.1:
        print("You can travel: (N)orth.")
    elif POSTION == 3.2:
        print("You can travel: (N)orth or (S)outh.")
    elif POSTION == 3.3:
        print("You can travel: (S)outh or (W)est.")




def get_move():
    move = input("Direction")


def make_move():







While POSTION != 3.3


#Player starts at position 1,1.

#1,1 : n
#1,2 : n / e / s
#1,3 : s / e
#2,1 : n
#2,2 : s / w
#2,3 : w / e
#3,1 : n victory
#3,2 : s / n
#3,3 : s / w


print('You can travel: ')
direction = input('Direction: ')
print('Not a valid direction!')
print('Victory!')

