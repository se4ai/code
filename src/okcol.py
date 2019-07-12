
"""

# okcol.py

"""

from ok import ok
from lib import *
from col import Col,Num,Sym
import math

@ok
def _col1():
  c= Col()
  for x in [9,2,5,4,12,7,8,11,9,3,7,4,12,5,4,10,9,6,9,4]:
    c + x
    print(c.has.sd)
  assert close(c.has.sd,3.0608)
  assert c.has.mu == 7

@ok
def _sym1():
  c = Col()
  for x in list('abbcccc'):
    c + x
    print(c.has.ent, c.has.mode)
  assert close(c.has.ent,1.3787836)
  assert c.has.mode == 'c'

if __name__ == "__main__": ok()
