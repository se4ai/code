import math
from memo import memo0
from thing import Thing

class Sym(Thing):
  "track symbols seen in a column"
  def __init__(i,inits=[]): 
    i.n,i.mode,i.bag = 0,None,{}
    i.memo = {}
    [i + x for x in inits]
  def spread(i): return i.ent()
  def expect(i): return i.mode
  def __add__(i,x):
    i.memo= {}
    i.n += 1
    i.bag[x] = i.bag.get(x,0) + 1
  def __sub__(i,x):
    i.memo={}
    if x in i.bag: 
      i.n -= 1
      i.bag[x] -= 1
  @memo0
  def mode(i):
    most=0
    for k,v in i.bag.items():
      if v > most:
        i.mode, most = k,v
    return i.mode
  @memo0
  def ent(i):
    e=0
    for v in i.bag.values():
      p  = v/i.n
      e -= p * math.log(p,2)
    return e
