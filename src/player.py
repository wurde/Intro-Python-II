#
# Dependencies
#

import sys
import random
import textwrap
import style

#
# Constants
#

directions = {
  'n': 'north',
  's': 'south',
  'e': 'east',
  'w': 'west',
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
    next_room_name = getattr(self.current_room, directions[direction])

    if next_room_name:
      next_room = self.grid.room(next_room_name)
      print(style.green.bold(f"*Move {directions[direction].upper()}*\n"))
      print(f"// {next_room_name.upper()}\n")
      print(textwrap.fill(style.white.bold(next_room.description), 70), '\n')
      print(style.white.bold(f"Items: {', '.join([item.name for item in next_room.items])}\n"))
      self.current_room = next_room
    else:
      print(style.yellow.bold(f"\n*You try to move {directions[direction].upper()}, but the way is blocked*.\n"))

    self.health -= 5

  def take(self, action):
    item_name = action.replace('take ', '')

    if self.current_room.has_item(item_name):
      item = self.current_room.take(item_name)

      if (random.randint(1, 100) < item.rng):
        self.health += item.health

      self.items.append(item)
      print(style.white.bold(f"Take: {item.name}\n"))
      print(style.white.bold(f"{item.description}\n"))
    else:
      self.health -= 5
      print(style.yellow.bold('*You stare up in confusion*\n'))

  def drop(self, action):
    item_name = action.replace('drop ', '')

    dropItem = None
    for item in self.items:
      if item.name.lower().strip() == item_name.lower().strip():
        dropItem = item

    if dropItem:
      print(style.white.bold(f"Drop: {dropItem.name}\n"))
      self.current_room.drop(dropItem)
      new_items = [item for item in self.items if item.name.lower().strip() != dropItem.name.lower().strip()]
      print('new_items', new_items)
      self.items = new_items
      # sys.exit(0)
      # self.items = [item for item in self.items if item.name.lower().strip() != dropItem.name.lower().strip()]
    else:
      self.health -= 5
      print(style.yellow.bold('*You stare up in confusion*\n'))

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
