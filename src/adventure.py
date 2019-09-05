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

  # TODO fill out all data
  grid = Grid()
  print(grid.rooms[0])
  sys.exit(0)

  main_player = Player(grid, grid.room('Outside'))
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
