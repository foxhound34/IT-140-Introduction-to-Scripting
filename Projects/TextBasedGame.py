# Code Developed by Derek Bamford
# imports time module to sleep text
import time

# Intro Screen
print()
print('* * * * * * * * * * *')
print('*                   *')
print('*  The Pirate Life  *')
print('*                   *')
print('* * * * * * * * * * *')

print()
print('A Text Adventure Game')
print()
print('Written and Coded by:')
print('   Derek Bamford')
print()

# input keystroke to start game
print('Press Enter to start.')
start_game = input()

# Story Screen
print('Your name is Henry Williams and you are seeking revenge on the deadly pirate Blackbeard for the death of '
      'your family.\nYou have tracked his ship,\"The Queen Anne\'s Revenge\", to the island of Tortuga and in the dead '
      'of night stowed aboard while it set sail from port.\n')
time.sleep(14)

print('Your goal is to move throughout the ship and collect all six items '
      'aboard before facing Blackbeard and taking your revenge.\n')
time.sleep(8)
print(
    'Movement allowed: North, South, East, West.\nTo pick up item type, take.\nTo end game type \"Exit\" when '
    'prompted for direction')
time.sleep(6)


def inventory_grab():
    if rooms[current_room]['Item'] not in inventory:
        print('Item:', rooms[current_room]['Item'])
        get_item = input('Take item before moving on: ').lower()
        if get_item == 'take':
            inventory.append(rooms[current_room]['Item'])
            print('Current inventory:\n', inventory)
    elif rooms[current_room]['Item'] in inventory:
        print('Items: None')


# Nested Dictionary of rooms and directions
rooms = {
    'Main Deck': {'West': 'Quarter Deck', 'North': 'Galley', 'East': 'Officers Quarters', 'South': 'Crew Cabin'},
    'Crew Cabin': {'North': 'Main Deck', 'East': 'Gundeck Starboard', 'Item': 'Rope'},
    'Gundeck Starboard': {'West': 'Crew Cabin', 'Item': 'Ammo'},
    'Quarter Deck': {'East': 'Main Deck', 'Item': 'Flintlock'},
    'Officers Quarters': {'West': 'Main Deck', 'Item': 'Treasure Map'},
    'Captain Cabin': {'East': 'Exit'},
    'Galley': {'South': 'Main Deck', 'East': 'Gundeck Port', 'Item': 'Dried Meat'},
    'Gundeck Port': {'West': 'Galley', 'Item': 'Master Key'},
}
direction = ''  # Set empty variable for direction
current_room = 'Main Deck'  # Set Starting Room
new_room = ''  # Set empty new room variable
inventory = []  # Sets player inventory to an empty list
exit_room = ''  # Sets variable for exit

print('You climbed up the side of the ship and arrived on the Main Deck.\nYou can move. North, South, East, West')

#  A while loop that is True until the user input is exit
while direction != 'Exit':
    #  I used a try and except statement to check for invalid user inputs
    try:
        direction = input('\nChoose a direction: ').capitalize()
        if direction == 'Exit':
            break
        # This else statement is where the movement occurs by swapping directions
        # and rooms for the dictionary and user input
        else:
            next_choices = rooms[current_room]
            new_room = next_choices[direction]
            current_room = new_room
            print('\nYou are in the', current_room, '.', 'You can move', *rooms[current_room], '.')
            inventory_grab()
        if len(inventory) == 6:
            print('You have collected all the items, go to the Captain\'s Cabin for the final showdown with Blackbeard')
        # Code that locks final room until all items are in inventory
        if current_room == 'Officers Quarters' and len(inventory) != 6:
            print('You do not have enough items to confront Blackbeard yet, head West to the Main Deck')

        elif current_room == 'Officers Quarters' and len(inventory) == 6:
            print('You are ready for the final battle, head North to face Blackbeard')
            final_room = input('Choose a direction: ').capitalize()
            if final_room == 'North':
                current_room = "Captain Cabin"
            else:
                current_room = 'Officers Quarters'

        if current_room == 'Captain Cabin':
            print('You confront Blackbeard and after a lengthy fight you shoot him dead with your flintlock.\n '
                  'You must now escape East out the back window to a row boat that awaits below')
            exit_game = input('Type, East,to escape: ').capitalize()
            if exit_game == 'East':
                print('\nYou use the rope to escape out the window and down the back of the ship.\n\n'
                      'Congratulations.\n\n'
                      'With Blackbeard dead and the treasure map in hand, things are starting to look up')
                break
            elif exit_game == 'South':
                current_room = 'Officers Quarters'
                print('You return to the Officers Quarters.  Where you are promptly murdered by the crew')
                break

    #  Invalid input continues the loop from the try/except loop
    except KeyError:
        print('\nNot a valid move, try again')
        continue

#  Display from the exit input break above
print('Game Over')
