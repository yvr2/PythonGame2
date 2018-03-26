import time
import random

playername = input('Please enter your name:')
time.sleep(1)
playername = playername[::-1]
playername = playername.lower()
playername = playername.capitalize()
playername = 'Commodore {}'.format(playername)

endgames = {'end1': 'Your thrusters fail and the ship floats helplessly, humanity will face extinction in the the cold depths of deep space...\nGAME OVER', 'end2': 'You are ambushed by a pirate fleet and are lasered into oblivion\nGAME OVER', 'end3': 'The ship\'s crew disagree with your command and incite rebellion, humanity\'s last survivors descend into fierce civil war aboard the starship...\nGAME OVER'}

class Ship:

    def __init__(self, name, hull, description):
        self.name = name
        self.hull = hull
        self.description = description
        #need to define input name uising raw input, possibly above, into a vartiable

npc_1 = Ship('Abandoned Freighter', 0, 'A long-abandoned relic of past intersteller conflict')
npc_2 = Ship('Karalax Trader Frigate', 1, 'A seemigly harmless trading ship, moving slowly across the galaxy in search of fortune')
npc_3 = Ship('Karalax Escort Convoy', 4, 'A fast moving strike team of fighter corvettes, clearing star systems without remorse for the Karalax Empire')


print('You are {}  of the marooned starship Eanna, the last remaining city-ship of the human civilization in the year 43,792...'.format(playername))
time.sleep(4)
print('All of humanity is aboard, desperately in search of a suitable planet to call home.')
time.sleep(3)
print('You are their only hope...')
class Location:

    def __init__(self, name, description):
        self.name = name
        self.description = description



location_1 = Location('Centaurus A', 'Centaurus A is a galaxy in the constellation of Centaurus.')
location_2 = Location('Cygnus X', 'A massive star formation region located in the constellation of Cygnus.')
location_3 = Location('Orion Spur', 'Along the edges of the Milky Way, humanity\'s original home')
location_4 = Location('Rosette Nebula', 'A large spherical H II formation, near one end of a giant molecular cloud in the Monoceros region of the Andromeda Galaxy')
location_5 = Location('IC 1318', 'Known to ancient wandering fleets as the Sadr region, you are amidst the diffuse emission nebula surrounding Gamma Cygni.')



time.sleep(2)
print('________________________________________________________________________________________________________________________')
print('You awake from extended cryostasis to find your ship off course, drifting amidst the distant galaxy {}.'.format(location_1.name))
time.sleep(4)
print('You proceed to the command bay and find the ship\'s captain manning the cockpit.')
time.sleep(3)
print ('\"Sleep well, {}?...In which direction shall we maneuver the ship?\"'.format(playername))
time.sleep(.5)
print('________________________________________________________________________________________________________________________')
time.sleep(1)
selection = input('Please enter a directional command to steer the ship, then press \'Enter\' to initialize thrusters: \n W- forward \n A - turn left \n S - reverse \n D - turn right \n')
time.sleep(1)
print('________________________________________________________________________________________________________________________')
selection = selection.upper()

while selection == 'W':
    print('* * * * * * * * Traversing Spacetime... * * * * * * * * ')
    time.sleep(1)
    print(' * * * * * * * * * * * * * * * * * * * * * * * * * * * ')
    print('Navigation crew reports we are now in the galaxy {}'.format(location_2.name))
    time.sleep(1)
    print('{}'.format(location_2.description))
    time.sleep(1)
    print('Our scouts report minimal activity in this galaxy...')
    time.sleep(1)
    print('...It\'s oddly quiet')
    selection = input('Please input a directional command:')
    selection = selection.upper()

    if selection == 'W':
            print('You\'ve encountered a black hole that has disabled your ship!')
            time.sleep(1)
            repair = input('Press R to initialize critical repair protocols...:\n')
            repair = repair.upper()
            if repair == 'R':
                repair = random.randint(1, 2)
            else:
                print('Command not recognized...')
                time.sleep(2)
                continue
            if repair == 1:
                print('The ship has been successfully repaired!')
                continue
            if repair == 2:
                print('Your crew is unable to repair the ship, humanity will face extinction in the the cold depths of deep space...')
            exit()

    elif selection == 'A':
        print(endgames['end{}'.format(random.randint(1, 3))])
        exit()
    elif selection == 'S':
        print('Initiating reverse thrusters...')
        time.sleep(1)
        print('Captain reports ship is on course...')
        time.sleep(1)
        print('Research team reports that we may have missed colonizable planets in Cygnus X. We should investigate further...Continuing to next galaxy...')
        break
    elif selection == 'D':
        print(endgames['end{}'.format(random.randint(1, 3))])
        exit()

while selection == 'A':
    print('* * * * * * * * Traversing Spacetime... * * * * * * * * ')
    time.sleep(1)
    print(' * * * * * * * * * * * * * * * * * * * * * * * * * * *')
    print('You are in the galaxy {}'.format(location_3.name))
    time.sleep(1)
    print('{}'.format(location_3.description))
    time.sleep(1)
    selection = input('Please input a directional command:')
    selection = selection.upper()

    if selection == 'W':
        print(endgames['end{}'.format(random.randint(1, 3))])
        exit()

    elif selection == 'A':
        print(endgames['end{}'.format(random.randint(1, 3))])
        exit()

    elif selection == 'S':
        print('Scouts report a large vessel in the vicinity with no discernable broadcast signal...')
        time.sleep(1)
        print('Would you like to investigate further?')
        time.sleep(1)
        investigate = input('Input Y/N\n:')
        investigate = investigate.upper()
        if investigate == 'Y':
            print('Reconnaissance team has discovered {}, with hull strength {}. {}.'.format(npc_1.name, npc_1.hull, npc_1.description))
            time.sleep(1)
            salvage = input('Press S to initialize salvage operation...:\n')
            time.sleep(1)
            salvage = salvage.upper()
            if salvage == 'S':
                salvage = random.randint(1, 2)
            else:
                print('Command not recognized...')
                time.sleep(2)
                continue
            if salvage == 1:
                print('The ship has been successfully salvaged!')
                time.sleep(1)
                continue
            if salvage == 2:
                print('Your crew is unable to salvage the ship...')
                time.sleep(1)
                continue
        if investigate == 'N':
            print('Moving on...')
        break

    elif selection == 'D':
        print('Initiating right turn...')
        time.sleep(1)
        print('Captain reports ship is on course...')
        time.sleep(1)
        print('Research team reports no colonizable planets in the Orion Spur. Onward to the next galaxy...')
        break


while selection == 'S':
    print('* * * * * * * * Traversing Spacetime... * * * * * * * * ')
    time.sleep(1)
    print(' * * * * * * * * * * * * * * * * * * * * * * * * * * * ')
    print('You have discovered the galaxy {}'.format(location_4.name))
    print('{}'.format(location_4.description))
    selection = input('Please input a directional command:')
    selection = selection.upper()

    if selection == 'W':
        print(endgames['end{}'.format(random.randint(1, 3))])
        exit()

    elif selection == 'A':
            time.sleep(1)
            print('Research team reports discpvery of Kepler-442b, near-Earth-sized exoplanet, likely rocky, orbiting within the habitable zone of the K-type main-sequence star Kepler-442.')
            time.sleep(1)
            print('You have discovered a new home for humanity!')
            time.sleep(1)
            print('WELL DONE, YOU WIN!')
            exit()

    elif selection == 'S':
        print('Scouts report a large vessel in the vicinity with a hostile broadcast signal...')
        time.sleep(1)
        print('Would you like to investigate further?')
        time.sleep(1)
        investigate = input('Input Y/N\n:')
        investigate = investigate.upper()
        while investigate == 'Y':
            print('Reconnaissance team has discovered {}, with hull strength {}. {}.'.format(npc_2.name, npc_2.hull, npc_2.description))
            time.sleep(1)
            combat = input('Press C to initialize combat operation and fire ion cannons...:\n')
            time.sleep(1)
            combat = combat.upper()
            if combat == 'C':
                combat = random.randint(1, 2)
            else:
                print('Command not recognized...')
                time.sleep(2)
                continue
            if combat == 1:
                npc_2.hull = npc_2.hull - 1
                print('The ship has been successfully damaged! It\'s hull strength is now {}'.format(npc_2.hull))
                time.sleep(1)
                break
            if npc_2.hull == 0:
                print('The ship has been destroyed!')
                break
            if combat == 2:
                print('Your cannons have missed the ship...preparing to fire again')
                time.sleep(1)
                continue
        if investigate == 'N':
            print('Moving on...')
            break

    elif selection == 'D':
        print('Initiating right turn...')
        time.sleep(1)
        print('Captain reports ship is on course...')
        time.sleep(1)
        print('Research team reports no colonizable planets in the Rosette Nebula. Onward to the next galaxy...')
        break


while selection == 'D':
    print('* * * * * * * * Traversing Spacetime... * * * * * * * * ')
    time.sleep(1)
    print(' * * * * * * * * * * * * * * * * * * * * * * * * * * *')
    print('You have discovered the galaxy {}'.format(location_5.name))
    time.sleep(1)
    print('{}'.format(location_5.description))
    time.sleep(1)
    print('Research team reports potential life-supporting conditions on planets in this galaxy...')
    time.sleep(1)
    print('...and scouts report unidentified signals to the south.')
    time.sleep(1)
    selection = input('Please input a directional command:')
    selection = selection.upper()


    if selection == 'W':
        print(endgames['end{}'.format(random.randint(1, 3))])
        exit()

    elif selection == 'A':
        time.sleep(1)
        print('Research team reports discpvery of Kepler-442b, an extrasolar planet orbiting within the empirical habitable zone of the Sun-like star Kepler-22.')
        time.sleep(1)
        print('You have discovered a new home for humanity!')
        time.sleep(1)
        print('WELL DONE, YOU WIN!')
        exit()


    elif selection == 'S':
        print('Scouts report a large vessel in the vicinity with a hostile broadcast signal...')
        time.sleep(1)
        print('Would you like to investigate further?')
        time.sleep(1)
        investigate = input('Input Y/N\n:')
        investigate = investigate.upper()
        while investigate == 'Y':
            print('Reconnaissance team has discovered {}, with hull strength {}. {}.'.format(npc_3.name, npc_3.hull, npc_3.description))
            time.sleep(1)
            combat = input('Press C to initialize combat operation and fire ion cannons...:\n')
            time.sleep(1)
            combat = combat.upper()
            if combat == 'C':
                combat = random.randint(1, 2)
            else:
                print('Command not recognized...')
                time.sleep(2)
                continue
            if combat == 1:
                npc_3.hull = npc_3.hull - 1
                print('The ship has been successfully damaged! It\'s hull strength is now {}'.format(npc_2.hull))
                time.sleep(1)
                break
            if npc_2.hull == 0:
                print('The ship has been destroyed!')
                break
            if combat == 2:
                print('Your cannons have missed the ship...preparing to fire again')
                time.sleep(1)
                continue
        if investigate == 'N':
            print('Moving on...')
            break

    elif selection == 'D':
        print('Initiating left turn...')
        time.sleep(1)
        print('Captain reports ship is on course...')
        time.sleep(1)
        print('Research team reports that we may have missed colonizable planets in IC 1318. We should investigate further...')
        break




print(endgames['end{}'.format(random.randint(1, 3))])
exit()
