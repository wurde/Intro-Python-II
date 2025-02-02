#
# Dependencies
#

from room import Room
from item import Item

#
# Define class
#

class Grid:
  def __init__(self):
    ignot_item = Item(name="Glowing Ignot", description="Curiousity drives you to pickup the glowing object.", health=-15)
    red_parchment = Item(name="Red Parchment", description="You read instructions: 'Deliver to the Watchtower of Ending'", health=5)
    blue_parchment = Item(name="Blue Parchment", description="You read instructions: 'Deliver to the Crimson Sanctum'", health=5)

    self.rooms = [
      Room(name="Outside", description="Any direction will do.", north="Fairy Asylum", south="Crimson Sanctum", east="Dining Room of the Sigl", west="Watchtower of Ending", items=[ignot_item]),
      Room(name="Fairy Asylum", description="You pass through a twisted trail that leads passed countless rooms and soon you enter a dark area. Small holes and carved paths cover the walls, it looks like a community or burrow for small creatures.", south="Outside", west="Desolate Prison of the Miners", items=[ignot_item]),
      Room(name="Crimson Sanctum", description="A narrow granite door in a gloomy thicket marks the entrance ahead. Beyond the granite door lies a large, clammy room. It's covered in rat droppings, dead insects and puddles of water. Your torch allows you to see what seems like some form of a sacrificial chamber, destroyed and absorbed by time itself.", west="Outside", items=[ignot_item]),
      Room(name="Dining Room of the Sigl", description="Inside the room looks warm and cozy. It has been built with red bricks and has brown stone decorations. Tall, large windows brighten up the room and have been added in a fairly symmetrical pattern.", east="Room of Knowledge", west="Outside", items=[ignot_item]),
      Room(name="Room of Knowledge", description="Inside the room looks grandiose. It has been built with wheat colored bricks and has granite decorations. Small, triangular windows let in plenty of light and have been added to the room in a mostly symmetric way.", west="Dining Room of the Sigl", items=[ignot_item, red_parchment]),
      Room(name="Desolate Prison of the Miners", description="Beyond the boulder lies a large, dusty room. It's covered in remains, broken stone and rubble.", east="Fairy Asylum", items=[ignot_item]),
      Room(name="Watchtower of Ending", description="You pass many rooms and passages, it's one big labyrinth of twists and turns. You eventually make it to what is likely the final room. A mysterious granite door blocks your path. Dried blood splatters are all over it, you enter cautiously.", east="Outside", items=[ignot_item, blue_parchment]),
    ]

  def __str__(self):
    return f"Grid with {len(self.rooms)} rooms."

  def room(self, name):
    for room in self.rooms:
      if room.name == name:
        return room
    return None
