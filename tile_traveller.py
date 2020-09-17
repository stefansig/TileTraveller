#Þurfum að bjóða notanda möguleika n/s/e/v
#hann velur eitthvað af möguleikunum og færist um reit
#þá fær hann aftur boð um möguleika
#ef hann velur eh sem er ekki möguleiki fær hann invalid direction
#þá fær hann aftur boð um möguleika
#forritið þarf að vita í hvaða reit leikmaður er í svo hann geti
#boðið honum rétta möguleika.
#leikmaður byrjar í reit 1.1

POSITION = 1.1


def new_position(value, POSITION):
    '''Takes in a direction input from user and returns new position'''
    NORTH = 'n' or 'N'
    SOUTH = 's' or 'S'
    WEST = 'w' or 'W'
    EAST = 'e' or 'E'
    if value == "n":
        POSITION += + 0.1
    elif value == "s":
        POSITION -= 0.1
    elif value == "w":
        POSITION -= 1.0
    elif value == "e":
        POSITION += 1.0
    return round(POSITION,1)



def options(position):
    if position == 1.1:
        print("You can travel: (N)orth.")
        return "n"
    elif position == 1.2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        return "nes"
    elif position == 1.3:
        print("You can travel: (E)ast or (S)outh.")
        return "es"
    elif position == 2.1:
        print("You can travel: (N)orth.")
        return "n"
    elif position == 2.2:
        print("You can travel: (N)orth or (S)outh or (W)est.")
        return "nsw"
    elif position == 2.3:
        print("You can travel: (E)ast or (W)est.")
        return "ew"
    elif position == 3.1:
        print("You can travel: (N)orth.")
        return "n"
    elif position == 3.2:
        print("You can travel: (N)orth or (S)outh.")
        return "ns"
    elif position == 3.3:
        print("You can travel: (S)outh or (W)est.")
        return "sw"






while POSITION != 3.1:
    legal = options(POSITION)
    direction = input('Direction: ').lower()
    if direction in legal:
        POSITION = new_position(direction, POSITION)
    else:
        print("Not a valid direction!")



#present_position = new_position(direction)
#options = options(present_position)


#print('You can travel: ')
#direction = input('Direction: ')
#print('Not a valid direction!')

print('Victory!')





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




