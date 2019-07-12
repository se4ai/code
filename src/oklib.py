"""

# oklib.py

"""

from ok import ok
from lib import *

@ok
def _items():
  assert [5]       == [x for x in items(5)]
  assert [1,2,3,4] == [x for x in items([1,2,3,4])]

@ok
def _ritems():
  assert ['a','b'] == [x for x in ritems(dict(a=1,b=2))]
  assert [1,2,3,4] == [x for x in ritems([1,(2,[3]),[4]])]

class Fred(Pretty):
  def __init__(i):
    i.a="a"
    i.b=dict(c=1,d=2)
    i.e=100
    i._has=i

print(Fred())
if __name__ == "__main__": ok()
