"""

# col.py : summarize columns of numbers or symbols

"""
from main import my
from memo import memos, fresh
from lib import nump,items
import math
"""

Tables of data have columns. `Col`umns can be `Num`eric
or `Sym`bolic. Some column values may be marked
as unknown (using the character found in `my.ignore`),
Sometimes, we know the number offset (the `pos`)
of the column and the column's name (the `txt`).

`Col`umns can be initialized with an `inits` column.  Internally,
`Col`umns keep a `has` variable which is initially empty. As things
arrive, (if they are not `my.ignore`), then the first thing
that is a symbol or a number triggers the creation of a new `Num` or `Sym` for the `i.has` variable.


"""
class Col(Pretty):
  def __init__(i,inits=[],txt="",pos=0,has=None):
    i.txt,i.pos,i.has = txt,pos,has() if has else None
    i + inits
  def n(i):      return i.has.n        if i.has else 0
  def delta(i):  return i.has.delta()  if i.has else 0
  def expect(i): return i.has.expect() if i.has else 0
  def __add__(i,x):
    for y in items(x): # x could a single thing or list of items
      if y != my.ignore:
        if not i.has: 
          i.has = Num() if nump(y) else Sym()
        i.has + y
  def __sub__(i,x):
    if x != my.ignore and i.has: i.has - x
"""


### Num

"""

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
    return (x - i.lo) / (i.hi - i.lo - my.tiny)
"""

Note that there is a numerical methods
issue with the `__sub__` method of `Num`: it becomes
inaccurate when the tracked numbers are very small and the sample
size is small (e.g. `i.n` less than 5). So if using
`aNum - x` to walk backwards down a sequence,
have a stopping rule of `i.n` > 5 (say).

### Sym

"""
@memos
class Sym(Pretty):
  "track symbols seen in a column"
  def __init__(i,inits=[]):
    i.n,i.bag = 0,{}
    [i + x for x in inits]
  def delta(i) : return i.ent()
  def expect(i): return i.mode
  @fresh
  def __add__(i,x):
    i.n += 1
    i.bag[x] = i.bag.get(x,0) + 1
  @fresh
  def __sub__(i,x):
    if x in i.bag:
      i.n -= 1
      i.bag[x] -= 1
  def mode0(i):
    most,out = 0,None
    for k,n in i.bag.items():
      if n > most:
        out, most = k,n
    return out
  def ent0(i):
    e=0
    for v in i.bag.values():
      p  = v/i.n
      e -= p * math.log(p,2)
    return e

"""

## Check Your Comprehension 

- This code uses `__add__` and `__sub__`. What does
  that mean for how items can be added or deleted ?
- `Num` and `Sym` are not sub-classes of `Col`. Why? 
  Hint: `Col` _has_ zero or one `Num` or `Sym`.
- Write down the equation for entropy, standard deviation.
- What is the standard deviation of a list with one item?
- What is the entropy of a list of 10 idenitical items?
- Consider the following  boxes. Intuitively, which is most/least diverse? Check your intution: on an x-y
  plot, lay out box 1,2,3,4,5 on the x-axis and compute their entropy (recorded on the y-axis). Where is
  entropy maximal? Minimal? FYI: log2(1)=0, log2(0.75)=-0.42, log2(0.5)=-1, log2(0.25)=-2.
  - box 1: [apple\*4] 
  - box 2: [apple\*3,orange\*1] 
  - box 3: [apple\*2,orange\*2] 
  - box 4: [apple\*1,orange\*3] 
  - box 5: [orange\*4]
- Match the X to the Y following: X={standard deviation, entropy}  apply to Y={symbolic and numeric}quantities.
- What is the _same_ about standard deviation and entropy?
- What is  _different_ about standard deviation and entropy?
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
