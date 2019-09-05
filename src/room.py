#
# Define class
#

class Room:
  def __init__(self, **kwargs):
    self.name = kwargs['name']
    self.description = kwargs['description']
    self.items = kwargs['items']

    if 'north' in kwargs:
      self.north = kwargs['north']
    else:

    if 'south' in kwargs:
      self.south = kwargs['south']

    if 'east' in kwargs:
    self.east = kwargs['east']
    self.west = kwargs['west']

  def __str__(self):
    return self.name

  def has_item(self, name):
    items = [item.name.lower().strip() for item in self.items]

    if name.lower().strip() in items:
      return True
    else:
      return False
