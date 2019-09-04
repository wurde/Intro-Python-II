#
# Dependencies
#

import sys
import textwrap
from room import Room
from player import Player

#
# Constants
#

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

#
# Link rooms together
#

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Define game
#

def adventure():
  main_player = Player('Joe', 'overlook')

  while True:
    print('You wake up.\n')
    print(f"// {main_player.current_room.upper()}\n")

    print(textwrap.fill(room[main_player.current_room].description, 70), '\n')

    user_input = input()

    if user_input == 'q' or user_input == 'quit':
      print('*Death by exhaustion*\n')
      print('// GAME OVER\n')
      sys.exit(0)

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.

#
# Initialize game
#

if __name__ == '__main__':
  adventure()
