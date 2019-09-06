#
# Dependencies
#

from room import Room

#
# Define class
#

class Grid:
  def __init__(self):
    self.rooms = [
      Room("Outside Cave Entrance", 
           "North of you, the cave mount beckons"),
      Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
      Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
      Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
      Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")
    ]

  def __str__(self):
    return f"Grid with {len(self.rooms)} rooms."

  def room(self, name):
    for room in self.rooms:
      if room.name == name:
        return room
    return None
