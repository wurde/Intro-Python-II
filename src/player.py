#
# Constants
#

directions = {
  'n': 'NORTH',
  's': 'SOUTH',
  'w': 'WEST',
  'e': 'EAST',
}

#
# Define class
#

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room

  def __str__(self):
    return self.name

  def move(self, direction):
    print(f"\nYou move {directions[direction]}.\n")
