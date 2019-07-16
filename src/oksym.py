"""

# oksym.py

"""
from ok import ok
from lib import *
from col import Col,Num,Sym
import math

s=Sym()
for x in 'abbcccc': s+x
print(s,s.mode, s.ent)

@ok
def _sym1():
  s = Sym()
  for x in list('abbcccc'):
    s + x
  assert close(s.ent,1.3787836)
  assert s.mode == 'c'

if __name__ == "__main__": ok()
