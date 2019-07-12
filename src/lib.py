"""

# lib.py: misc utilities


"""
import random
from main import my
from collections.abc import Iterable   


"""

## Misc

### Random numbers

"""

r = random.random
any = random.choice

"""

## Pretty Bring

"""

class Pretty:
  def __repr__(i):
    pairs = sorted([(k,v) for k,v in i.__dict__.items() 
                    if k[0] != my.private])
    pre = i.__class__.__name__ + '{'
    quote=lambda z: "'%s'" % z if stringp(z) else str(z)
    return pre + ", ".join(['%s=%s' % (k,quote(v)) for k,v in pairs]) + '}'

"""

## Meta

### iterp, nump: truth predicates

"""

def iterp(x) : return not isinstance(x,str) \
                      and isinstance(x,Iterable)
def nump(x)  : return isinstance(x,(float,int))

def stringp(x): return isinstance(x,str)
"""

## Math

"""

def close(x,y,near=0.01): return y*(1-near) <=x<= y*(1+near)

"""

## Lists

### Iterate through anything

#### items: over top level

"""

def items(x): 
   for y in (x if iterp(x) else [x]): yield y

"""

#### ritems: recursively, over all levels

"""
def ritems(x): 
  if iterp(x):
    for y in x:
      for z in ritems(y): yield z
  else: yield x

