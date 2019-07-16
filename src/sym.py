"""

### Sym

"""
from memo import memos, fresh
from lib  import *
import math

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

- What does the `@memos` class decorator do?
- What does the `@fresh` method decorator do?
- What would happen if the above `__add__` and `__sub__` methods 
  neglected to `@fresh`en?
- This code uses `__add__` and `__sub__`. What does
  that mean for how items can be added or deleted ?
- Write down the equation for entropy.
- What is the entropy of a list of 10 idenitical items?
- Consider the following  boxes. Intuitively, which is most/least diverse? Check your intution: on an x-y
  plot, lay out box 1,2,3,4,5 on the x-axis and compute their entropy (recorded on the y-axis). Where is
  entropy maximal? Minimal? FYI: log2(1)=0, log2(0.75)=-0.42, log2(0.5)=-1, log2(0.25)=-2.
  - box 1: [apple\*4] 
  - box 2: [apple\*3,orange\*1] 
  - box 3: [apple\*2,orange\*2] 
  - box 4: [apple\*1,orange\*3] 
  - box 5: [orange\*4]
- What does the `@memos` class decorator do?
- What does the `@fresh` method decorator do?
- What would happen if the above `__add__` and `__sub__` methods 
  neglected to `@fresh`en?

"""
