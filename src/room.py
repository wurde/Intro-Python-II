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
      self.north = None

    if 'south' in kwargs:
      self.south = kwargs['south']
    else:
      self.south = None

    if 'east' in kwargs:
      self.east = kwargs['east']
    else:
      self.east = None

    if 'west' in kwargs:
      self.west = kwargs['west']
    else:
      self.west = None

  def __str__(self):
    return self.name

  def has_item(self, name):
    items = [item.name.lower().strip() for item in self.items]

    if name.lower().strip() in items:
      return True
    else:
      return False

  def take(self, name):
    fetchItem = None

    for item in self.items:
      if item.name.lower().strip() == name.lower().strip():
        fetchItem = item

    self.items = [item for item in self.items if item.name.lower().strip() != name.lower().strip()]

    return fetchItem

  def drop(self, item):
    self.items.append(item)
