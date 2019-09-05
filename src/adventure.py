#
# Dependencies
#

import sys
import textwrap
import style
from pyfiglet import Figlet
from grid import Grid
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
# Define commands
#

def print_commands():
  print(style.white.bold('Navigation: n, s, e, w'))
  print(style.white.bold('Items: take ITEM, drop ITEM, inventory'))
  print(style.white.bold('Exit: q, quit\n'))

#
# Define game
#

def adventure():
  figlet = Figlet(font='slant')
  print(style.white.bold(figlet.renderText('ADVENTURE')))

  grid = Grid()
  sys.exit(0)

  # TODO initialize Player (pass in map instance)
  main_player = Player('Joe', room['outside'])
  print(style.white.bold('*You wake up*\n'))

  print_commands()

  # print(f"// {str(main_player.current_room).upper()}\n")
  # print(textwrap.fill(main_player.current_room.description, 70), '\n')

  while True:
    user_input = input('$ ')

    if user_input == 'n':
      main_player.move('n')
    elif user_input == 's':
      main_player.move('s')
    elif user_input == 'e':
      main_player.move('e')
    elif user_input == 'w':
      main_player.move('w')
    elif user_input == 'q' or user_input == 'quit':
      print('\n*Death by exhaustion*\n')
      print('// GAME OVER\n')
      sys.exit(0)
    else:
      print('\n*You stare up in confusion*\n')

#
# Initialize game
#

if __name__ == '__main__':
  try:
    adventure()
  except KeyboardInterrupt:
    print('\n\n*Death by exhaustion*\n')
    print('// GAME OVER\n')
    sys.exit(0)
