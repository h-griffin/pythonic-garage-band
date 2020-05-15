class Band:
  band_list = []

  def __init__(self, name='none', members='[jane, john]'):
    self.name = name    #'this is a band name'   #band name / slipknot
    self.members = members
    Band.band_list.append(self)

  # def play_solo(self):
  #   pass

  def __str__(self):
    return f'str band name: {self.name}'

  def __repr__(self):
    return f'repr band name: {self.name}'

  @classmethod
  def to_list(cls):
    print(cls)
    return cls.band_list    #return all created bands Band.to_list()

  @staticmethod
  def will_never_change(self):    #is not modified by state of class ^^
    pass
    
class Musician():
  musician_list = []
  #super().__init__(name) //    things need to happen in the super class init
  def __init__(self, name='none'):
    self.name = name
    Musician.musician_list.append(self)

  def __str__(self):
    return f'str Musician name: {self.name}'

  def __repr__(self):
    return f'repr Musician name: {self.name}'


  @classmethod
  def to_list(cls):
    return cls.musician_list
    

class Guitarist():
  def __init__(self, name='none'):
    self.name = name    #member name / cory taylor
  def get_instrument(self):
    return 'guitar'
  def play_solo(self):
    return 'shredding guitar solo'

class Bassist():
  def __init__(self, name='none'):
    self.name = name
  def get_instrument(self):
    return 'bass'
  def play_solo(self):
    return 'thundering bass solo'

class Drummer():
  def __init__(self, name='none'):
    self.name = name
  def get_instrument(self):
    return 'drums'
  def play_solo(self):
    return 'booming drum solo'

if __name__ == "__main__":
  slipknot = Band('Slipknot', ['corey, james'])
  corey = Musician('Corey')
  print(slipknot.__str__())
  print(slipknot.__repr__())
  print(corey.__str__())
  print(corey.__repr__())
