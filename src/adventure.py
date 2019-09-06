#
# Dependencies
#

import re
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

  # TODO initialize Player (pass in map instance)
  main_player = Player('Joe', room['outside'])
  print(style.white.bold('*You wake up*\n'))

  print_commands()

  # print(f"// {str(main_player.current_room).upper()}\n")
  # print(textwrap.fill(main_player.current_room.description, 70), '\n')

  while True:
    # TODO check for win condition
    objective_a = False #grid.room('Watchtower of Ending').has_item('Red Parchment')
    objective_b = False #grid.room('Crimson Sanctum').has_item('Blue Parchment')

    if objective_a and objective_b:
      print('')
      print(style.green.bold(figlet.renderText('SUCCESS')))
      print('')
      sys.exit(0)

    user_input = input(main_player.status())

    # TODO take item
    # TODO drop item
    if main_player.health <= 0 or user_input in ['q', 'quit']:
      print(style.red.bold('\n*Death by exhaustion*\n'))
      print(style.white.bold('// GAME OVER\n'))
      sys.exit(0)
    elif user_input in ['h', 'help']:
      main_player.health -= 5
      print('')
      print_commands()
    elif user_input == ['n', 's', 'e', 'w']:
      main_player.move(user_input)
    elif re.match("^take", user_input):
      main_player.take(user_input)
    elif re.match("^drop", user_input):
      main_player.drop(user_input)
    elif user_input in ['i', 'inventory']:
      main_player.inventory()
    else:
      main_player.health -= 5
      print(style.yellow.bold("\n*You stare up in confusion*\n"))

#
# Initialize game
#

if __name__ == '__main__':
  try:
    adventure()
  except KeyboardInterrupt:
    print(style.red.bold('\n*Death by exhaustion*\n'))
    print(style.white.bold('// GAME OVER\n'))
    sys.exit(0)
