# import pytest
from pythonic_garage_band import __version__
from pythonic_garage_band.garage_band import Band, Musician, Guitarist, Bassist, Drummer
# from pythonic_garage_band.garage_band import Musician
# from pythonic_garage_band.garage_band import Guitarist
# from pythonic_garage_band.garage_band import Bassist
# from pythonic_garage_band.garage_band import Drummer

def test_version():
    assert __version__ == '0.1.0'

def test_band_list():
  assert Band.to_list() == []
  slipknot = Band('Slipknot', '[Corey, James]')
  assert len(Band.to_list()) == 1
  
def test_band_list_attributes():
  Band.band_list = []
  Musician('Corey')
  # assert Musician.musician_list()[0].name == 'Corey'
  assert len(Musician.to_list()) == 1

def test_play_solo():
  
# @pytest.fixture(autouse=True)
# def prep():
#   Band.count = 0
#   Band.to_list = []
  # def test_(prep) / autouse

# @pytest.fixture
# def band():
#   return Band('Nirvana', [
#     Guitarist('Kurt Cobain'),
#     Bassist('Krist Novoselic'),
#     Drummer('Dave Grohl')
#   ])
