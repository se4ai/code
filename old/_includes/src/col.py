from config import my
from num    import Num
from sym    import Sym

class Col:
  def __init__(i,inits=[],txt="",pos=0):
    i.txt,i.pos,i.has = txt,pos,None
    [i + x for x in inits]
  def n(i):
    return i.has.n if i.has else 0
  def spread(i):
    return i.has.spread() if i.has else 0
  def __add__(i,x):
    nump = lambda z: isinstance(z, (int,float))
    if x != my.ignore: 
      if not i.has:
        what  = Num if nump(x) else Sym
        i.has = what()
    i.has + x
  def __sub__(i,x):
    if x != my.ignore and i.has: 
      i.has - x
