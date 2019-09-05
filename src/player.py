#
# Dependencies
#

import textwrap
import style

#
# Constants
#

directions = {
  'n': 'NORTH',
  's': 'SOUTH',
  'e': 'EAST',
  'w': 'WEST',
}

#
# Define class
#

class Player:
  def __init__(self, grid, current_room):
    self.grid = grid
    self.current_room = current_room
    self.health = 100
    self.items = []

  def __str__(self):
    return "Main player"

  def move(self, direction):
    # TODO rework to use new Grid system
    if direction == 'n' and self.current_room.n_to:
      print(f"\nYou move {directions[direction]}.\n")
      print(f"// {str(self.current_room.n_to).upper()}\n")
      print(textwrap.fill(self.current_room.n_to.description, 70), '\n')
      self.current_room = self.current_room.n_to
    elif direction == 's' and self.current_room.s_to:
      print(f"\nYou move {directions[direction]}.\n")
      print(f"// {str(self.current_room.s_to).upper()}\n")
      print(textwrap.fill(self.current_room.s_to.description, 70), '\n')
      self.current_room = self.current_room.s_to
    elif direction == 'e' and self.current_room.e_to:
      print(f"\nYou move {directions[direction]}.\n")
      print(f"// {str(self.current_room.e_to).upper()}\n")
      print(textwrap.fill(self.current_room.e_to.description, 70), '\n')
      self.current_room = self.current_room.e_to
    elif direction == 'w' and self.current_room.w_to:
      print(f"\nYou move {directions[direction]}.\n")
      print(f"// {str(self.current_room.w_to).upper()}\n")
      print(textwrap.fill(self.current_room.w_to.description, 70), '\n')
      self.current_room = self.current_room.w_to
    else:
      print(f"\n*You try to move {directions[direction]}, but the way is blocked*.\n")

  def status(self):
    if self.health < 20:
      return style.red.bold('(╯°□°）╯︵ ┻━┻ ')
    elif self.health < 50:
      return style.yellow.bold('(ಠ_ಠ) ')
    else:
      return style.green.bold('(ʘ‿ʘ)  ')

  def inventory(self):
    items = [item.name for item in self.items]
    items_str = ", ".join(items)
    print(style.white.bold(f"\nInventory: {items_str}\n"))
