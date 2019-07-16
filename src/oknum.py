"""

# oknum.py

"""

from ok  import ok
from lib import *
from num import Num

n=Num()
for x in [1,2,3,4]: n+x
print(n,n.sd)

@ok
def _num():
  n= Num()
  for x in [9,2,5,4,12,7,8,11,9,3,7,4,12,5,4,10,9,6,9,4]:
    n + x
  assert close(n.sd,3.0608)
  assert n.mu == 7
