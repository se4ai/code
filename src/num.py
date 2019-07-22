"""

### Num

"""
from main import my
from memo import memos, fresh
from lib import nump,items,Pretty

@memos # turns the method sd0 into a property i.sd
class Num(Pretty):
  "Track numbers seen in a column"
  def __init__(i,inits=[]):
    i.n,i.mu,i.m2 = 0,0,0
    i.lo,i.hi     = my.inf, -1*my.inf
    [i + x for x in inits]
  def delta(i) : return i.sd()
  def expect(i): return i.mu
  def sd0(i):
    return 0 if i.n < 2 else (i.m2/(i.n - 1 + 10**-32))**0.5
  @fresh # this method updates state, so  blast the memos
  def __add__(i,x):
    if x < i.lo: i.lo = x
    if x > i.hi: i.hi = x
    i.n  += 1
    d     = x - i.mu
    i.mu += d/i.n
    i.m2 += d*(x - i.mu)
  @fresh # this method updates state, so  blast the memos
  def __sub__(i,x):
    if i.n < 2:
      i.n,i.mu,i.m2 = 0,0,0
    else:
      i.n  -= 1
      d     = x - i.mu
      i.mu -= d/i.n
      i.m2 -= d*(x - i.mu)
  def norm(i,x):
    return  (x - i.lo) / (i.hi - i.lo - my.tiny)
"""

Note that there is a numerical methods
issue with the `__sub__` method of `Num`: it becomes
inaccurate when the tracked numbers are very small and the sample
size is small (e.g. `i.n` less than 5). So if using
`aNum - x` to walk backwards down a sequence,
have a stopping rule of `i.n` > 5 (say).


## Quiz

- What is the standard deviation of a list with one item?
- According to Cohen,
  a _small effect_ (i.e. Of negligible size) is less that 30% of the standard deviation.
  Add a method called `cohen` to `Num` class that returns a _negligible_ amount_ (edit `main.py` to
  define a 
  `negligible` parameter of 30\%). 
  Add a test function to `okcol.py` that uses that `cohen` method
- What does the `@memos` class decorator do?
- What does the `@fresh` method decorator do?
- What would happen if the above `__add__` and `__sub__` methods 
  neglected to `@fresh`en?

"""
