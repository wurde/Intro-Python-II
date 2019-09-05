#
# Dependencies
#

import random

#
# Define class
#

class Item:
  def __init__(self, **kwargs):
    self.name = kwargs.name
    self.description = kwargs.description
    self.health = kwargs.health
    if self.health > 0:
      self.rng = random.randint(1, 100)
    else:
      self.rng = random.randint(1, 100) + 15

  def __str__(self):
    return self.name
