from math import log
from minilib import *
import sys

"""
suggestion: 
easier to monitor if stream, not batch
easier to stream if incremental learning
faster to discuss in sample, not show all
easier to explain, control if ranges, not points
look before you leap (reason over sub-sub clusters, not top cluster)

"""
my = o( 
       era=128,
       char= o(ignore="?",
               less  = "<",
               more  = ">"),
       num= o(small= 0.38, #<0.38=small, <1=medium 
              conf = 95,
              p    = 2,
              bins = 10),
       row= o(doms=64),
       cluster= o(m=64, 
                  strange=1 # set to 0 to disable anomaly detection
                  )
      )

#----------------------------------------------------------
  class Sym(Thing):
  def __init__(i,inits=[], name="",w=1,pos=0): 
    i.w=w; i.pos=pos; i.name=name
    i.n=0; i.d={}; i.most=0;i.mode=None
    [i + x for x in inits]
  def __add__(i,x):
    i.n += 1
    m=i.d[x] = i.d.get(x,0) + 1
    if m >  i.most: i.most,i.mode = m,x
    return x
  def p(i,x):
    return  i.d.get(x,0) / n
  def prep(i,x): return x
  def norm(i,x): return x
  def variety(i):
    e = 0
    for v in i.d.values():
      p  = v/i.n
      e -= p * log(p,2)
    return e
  def dist(i,x,y):
    no = my.char.ignore
    if x==no or y ==no: return 1
    return 0 if x == y else 1

class cols(ok):pass

@cols
def _sym1():
  s = Sym(list('abbcccc'))
  assert close(s.variety(),1.3787836)
  assert s.mode == 'c'

#----------------------------------------------------------
class Num(Thing):
  # some stats thresholds
  z=  ((0,.5),(.25,.5987),(0.5,.6915),(0.75,.7734), (1,.8413),
       (1.25,.8944),(1.5,.9332),(1.75,.9599),(2,.9772),
       (2.25, .9878), (2.5,.9918),(2.75,.997), (3,.9987))
  t95=((1, 6.314),(5,2.015),(10,1.812),(20,1.725),(30,1.697))
  t99=((1,31.821),(5,3.365),(10,2.764),(20,2.528),(30,2.457))

  def __init__(i,inits=[],name="",pos=0,w=1):
    i.w=w; i.pos=pos; i.name=name
    i.n,i.mu,i.m2,i.sd = 0,0,0,0
    i.lo =10**32; i.hi = -1*i.lo
    [i + x for x in inits]
  def variety(i): return i.sd
  def __add__(i,x):
    x = i.prep(x)
    if x < i.lo: i.lo = x
    if x > i.hi: i.hi = x
    i.n  += 1
    d     = x - i.mu
    i.mu += d/i.n
    i.m2 += d*(x - i.mu)
    i.sd = (i.m2/(i.n - 0.99999))**0.5
    return x
  def __sub__(i,x):
    if i.n < 2:
      i.n,i.mu,i.m2 = 0,0,0
    else:
      i.n  -= 1
      d     = x - i.mu
      i.mu -= d/i.n
      i.m2 -= d*(x - i.mu)
      i.sd = (i.m2/(i.n - 0.99999))**0.5
  def norm(i,x):
    return  (x - i.lo) / (i.hi - i.lo +0.00000001)
  def dist(i,x,y):
    no = my.char.ignore
    if x==no and y ==no: return 1
    if x=="?":
      y = i.norm(y)
      x = 0 if y>0.5 else 1
    elif y=="?":
      x = i.norm(x)
      y = 0 if x>0.5 else 1
    else:
      x,y=i.norm(x),i.norm(y)
    return (x-y)**my.num.p
  def z(i,x):
    return  (x - i.mu)/i.sd
  def zbin(i,x):
    z = i.z(x)
    p = interpolate(abs(z),Num.z)
    return int((1-p if z < 0 else p) / my.nums.bins)
  def different(i,j):
    return i.hedges(j) and i.ttest(j)
  def ttest(i,j):
    df = min(i.n - 1, j.n - 1) 
    t= interpolate(df,Num.t95 if my.num.conf==95 else Num.t99)
    return abs(i.mu - j.mu)/(i.sd/i.n + j.sd/j.n)**0.5 >= t
  def hedges(i,j):
    num   = (i.n - 1)*i.sd**2 + (j.n - 1)*j.sd**2
    denom = (i.n - 1) + (j.n - 1)
    sp    = (num / denom )**0.5
    delta = abs(i.mu - j.mu) / sp  
    c     = 1 - 3.0 / (4*(i.n + j.n - 2) - 1)
    return delta * c >= my.num.small

class Int(Num):
  def prep(i,x): return int(x)
class Float(Num):
  def prep(i,x): return float(x)

@cols
def _num1():
  n= Int([9,2,5,4,12,7,8,11,9,3,7,4,12,5,4,10,9,6,9,4])
  assert close(n.sd,3.0608)
  assert n.mu == 7

@cols
def _num2():
  seed(1)
  c=1
  while c<1.4:
    c+=0.025
    a= [r()**0.5 for _ in range(100)]
    b= [x*c for x in a]
    a= Float(a)
    b= Float(b)
    print("%5.3f %5.3f %5.3f %5.3f %5.3f " % (c,a.mu,b.mu, a.sd,b.sd),
          "hedges %5s ttest %5s both %5s" %(a.hedges(b), a.ttest(b), a.different(b)))

#----------------------------------------------------------
class Row(Thing):
  id=0
  def __init__(i,cells,history) : 
    i._memo={}
    i.history=history
    i.cells = cells
    i.id = Row.id = Row.id+1
  def __getitem__(i,k):  return i.cells[k]
  @memo
  def dominates(i):
    n     = my.row.doms
    goals = i.history.goals()
    return sum([i.dominate(one(i.history.rows),goals)
                for _ in range(n)])  / n
  def dominate(i,j,goals):   
    z = 0.00001
    s1, s2, n = z,z,z+len(goals) 
    for goal in goals:
      a,b = i[goal.pos], j[goal.pos]
      a,b = goal.norm(a), goal.norm(b)
      s1 -= 10**(goal.w * (a-b)/n)
      s2 -= 10**(goal.w * (b-a)/n)
    return s1/n < s2/n
  def dist(i,j):
    n,d,ps = =0.00000001,0,1/my.num.p
    for x,y,h in zip(i.cells,j.cells,i.history.seen):
      n += 1
      d += h.dist(x,y)
    return d**p/n**p
#----------------------------------------------------------
class Cluster(Pretty):
  def __init__(i, inits=[],history): 
    i.rows  = []
    i.dnum=Num()
    i.east,i.west = None,None
    i.left, i.right = None,None
    i.history = history
    i.where
    [i + x for x in inits]
  def clone(i):
   return Cluster(i.history)
  def __add__(i,row):
    if   i.west  is None: 
      i.west=row
    elif i.east is None: 
      i.east=row; c=i.west.dist(i.east)
    else:
      a = i.east.dist(row)
      b = i.west.dist(row)
      d = i.where[row.id] = (a**2 + b**2 - i.c**2)/2*i.c
      i.dnum + d
      if abs(i.dnum.z(d)) > my.cluster.strange: 
        i.rows += [row]
        if len(i.rows) > 2*my.cluster.era:
          i.left  = i.left  or clone()
          i.right = i.right or clone()
          if a < b:
            i.left.add(row)
          else:
            i.right.add(row)
            ## rows are different e in each luster
            ## history is global at the top, pased down
            ## rows dont have history built in
            ## two histoies, global and local
## only shuffle once at top
## must remember to add when we start
#----------------------------------------------------------
class History(Thing):
  def __init__(i,names=[],keep=True): 
    i.rows  = []
    i.keep  = keep
    i.names = names
    i.seen  = [None] * len(names)
  def clone(i):
    return History([x.name for x in i.seen])
  def goals(i):
    return [x for x in i.seen if 
            my.char.less in x.name or my.char.more in x.name]
  def __add__(i,row):
    for n,(cell,name) in enumerate(zip(row.cells,i.names)): 
      if cell !=my.char.ignore: 
        watcher = i.seen[n] = i.seen[n] or i.seeing(n,cell,name)
        row[n]  = watcher + cell
    row = Row(row)
    if i.keep:
      i.rows += [row]
    return row
  def seeing(i,n,x,name):
    try       : x=int(x); what=Int
    except    : 
      try     : x=float(x); what=Float
      except  : what=Sym
    return what(name=name,pos=n,
                w= -1 if my.char.less in name else 1)
   
def shuffled(src, b4):
  cache   = []
  history = b4.clone()
  for x in src:
    cache += [x]
    if len(cache) > my.era:
      random.shuffle(cache)
      for y in cache: 
        yield history + y, history
      cache = []
  if cache:
    random.shuffle(cache)
    for y in cache: 
      yield history + y, history

def data(rows=[], names=[], about=''):
  use  = [n for n,x in enumerate(names) if not my.char.ignore in x]
  cols = lambda lst: [lst[n] for n in use]
  return shuffled([Row(cols(row)) for row in rows], 
                  History(cols(names)))

class stories(ok): pass

@stories
def _auto():
  from auto import auto
  for row,history in data(**auto()):
    print(row.cells)
  lst = sorted(history.rows,
               key=lambda z:z.dominates(history))
  for row in lst[:5]+lst[-5:]:
    print(row)
###########################################################

if __name__ == "__main__":
  ok.main(sys.argv)

