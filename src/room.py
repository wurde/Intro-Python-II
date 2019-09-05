#
# Define class
#

class Room:
  n_to = None
  s_to = None
  e_to = None
  w_to = None

  def __init__(self, **kwargs):
    self.name = kwargs.name
    self.description = kwargs.description

  def __str__(self):
    return self.name
