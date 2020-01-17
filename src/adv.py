from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'coins': Item('Coins', 'You will unlock everything in this coins'),

    'key': Item('Key', 'get the key access to all the doors'),

    'pencil': Item('pencil', 'Just write your dream')
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['treasure'].add_item('gold')
room['overlook'].add_item('key')
room['overlook'].add_item('mud')

#####################################
#                                   #
#          overlook  #   treasure   #
#           foyer       narrow      #
#          Outside                  #
#####################################


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player(input("Please enter your name: "), room['outside'])
print(player.current_room)
current_room = player.current_room

# Create basic REPL loop
while True:
    # Read command

    directions = ["n", "s", "e", "w"]
    actions = ["get", "drop"]
    cmd = input("~~> ").lower().split(" ")
    player_action = cmd[0]
    if len(cmd) > 1:
        item_of_interest = cmd[1]

    # Check if it's n/s/e/w/q
    if player_action in directions:
        # Make player travel in that direction
        player.travel(player_action)
    elif player_action == "q":
        # Quit
        print("Goodbye!")
        exit()
    elif player_action == "i":
        player.list_inventory()
    elif player_action == "l":
        current_room.items_avail()
    elif player_action in actions:
        if player_action == "get":
            item_location = current_room.item_locate(item_of_interest)
            if item_location:
                player.add_item_in(item_location)
                current_room.delete_item(item_location)
            else:
                print("Can't find this item\n")
        elif player_action == "drop":
            item_removed = player.remove_item_in(item_of_interest)
            current_room.add_item(item_removed)
    else:
        print("I did not recognize that command")


### REFACTORED SOLUTION ###
# def initialize():
#     player_name = input('What is your name?\n')

#     current_player = Player(player_name, room['outside'])

#     print(
#         f'Welcome {current_player.get_name()}! Your current location is: {current_player.get_location().name}\n'
#     )

#     directions = ["n", "s", "e", "w"]

#     def print_current_location():
#         print(f'You are now in the {current_player.get_location().name}\n')

#     def is_valid_move(move):
#         if move != None:
#             return True
#         else:
#             return False

#     while True:
#         player_input = input('Which direction will are you planning?\n')

#         if player_input == 'n' or player_input == 's' or player_input == 'e' or player_input == 'w':
#             if player_input == 'n':

#                 if is_valid_move(current_player.get_location().n_to):
#                     current_player.set_location(
#                         current_player.get_location().n_to
#                     )

#                     print_current_location()

#             elif player_input == 's':
#                 if is_valid_move(current_player.get_location().s_to):
#                     current_player.set_location(
#                         current_player.get_location().s_to
#                     )

#                     print_current_location()

#             elif player_input == 'e':
#                 if is_valid_move(current_player.get_location().e_to):
#                     current_player.set_location(
#                         current_player.get_location().e_to
#                     )

#                     print_current_location()

#             else:
#                 if is_valid_move(current_player.get_location().w_to):
#                     current_player.set_location(
#                         current_player.get_location().w_to
#                     )

#                     print_current_location()

#         elif player_input == 'q':
#             print(
#                 f'Goodbye {current_player.get_name()}, we hope you\'ll play again!')
#             break
#         else:
#             print(
#                 'Invalid command: Navigate using "n", "s", "e", or "w", or press "q" to quit'
#             )


# initialize()
