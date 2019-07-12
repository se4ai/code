from config import * 
from col import Col
from copy import deepcopy 

def chops(lst, q= my.bins, 
           getx= lambda z:z,     # for list of numbers
           gety= lambda g,z: z,  # for lst of numbers
           #y= lambda g,z: z[g], # for lst of lists
           epsilon=None, 
           #isa=Num,   # to split on symbols, use Sym
           goals=[0], # list of gety's first argument
           ):
  # these 3 functions let an item have 1 to many goals
  def create(): return [(isa(),g) for g in goals]
  def update(ys,item):
    for y,g in ys: 
      val = gety(g,item)
      if val != my.ignore: y + val
  def better(ys0,ys1,ys2):
    for (y0,_),(y1,_),(y2,_) in zip(ys0,ys1,ys2):
      if y0.simpler(y1,y2): return True
  #------
  lst = sorted([z for z in lst if z != my.ignore], key=getx)
  n   = len(lst)
  w   = int(n/q) # a chop must be at least w wide
  if epsilon == None: # set epsilon from value near the median
    epsilon = getx(lst[int(n*(0.5+my.ncohen))]) - \
              getx(lst[int(n*0.5           )])
  print(dict(w=w,e=epsilon))
  y0, y1, y2 = create(), create(), create()
  nchops, chop = 0, []
  for j,item in enumerate(lst):
    if getx(item) != my.ignore:
      chop += [item] 
      update(y0, item)
      update(y2, item)
      print([gety(g,item) for g in goals])
      if len(chop) >= w: # enough to chop
       if j <= n-w: # after chop, enough for other chops
        if getx(item) != getx(lst[j+1]):  # dont split same thing
         # does chop divide nums by more then epsilon?
         if getx(chop[-1]) - getx(chop[0]) >= epsilon:
          # is this chop better than that last one?
          if not nchops or better(y0, y1, y2): 
            nchops += 1
            y0 = deepcopy(y2)
            y1 = deepcopy(y2)
            y2 = create()
            yield chop 
            chop = []
  if chop: 
    yield chop

"""
def xchops(lst, epsilon=0, x=lambda z:z,width=20): 
  "assumes list is sorted"
  chop = []
  for j,item in enumerate(lst):
    if x(item) != my.ignore:
      chop += [item] 
      if len(chop) >= w: # enough to chop
       if j <= n-w: # after chop, enough for other chops
        if x(item) != x(lst[j+1]):  # dont split same thing
         # does chop divide nums by more then epsilon?
         if x(chop[-1]) - x(chop[0]) >= epsilon:
          # is this chop better than that last one?
          yield chop 
          chop = []
  if chop: 
   yield chop

def chops(lst, q= my.bins, 
           x= lambda z:z,     # for list of numbers
           #y= lambda g,z: z[g], # for lst of lists
           epsilon=None, 
           ):

  def create(): return [(isa(),g) for g in goals]
  def add(ys,item):
    for y,g in ys: 
      val = gety(g,item)
      if val != my.ignore: y + val
  def better(ys0,ys1,ys2):
    for (y0,_),(y1,_),(y2,_) in zip(ys0,ys1,ys2):
      if y0.simpler(y1,y2): return True
lst = sorted([z for z in lst if z != my.ignore], key=x)
  n   = len(lst)
  width = int(n/q) # a chop must be at least w wide
  if epsilon == None: # set epsilon from value near the median
    epsilon = getx(lst[int(n*(0.5+my.ncohen))]) - \
              getx(lst[int(n*0.5           )])
  tmp = [chop for chop in xchops(lst,epsilon,x,width)]
  """


def div(lst, epsilon=None,q=my.bins, cohen=my.ncohen,
         x=lambda z:z[0], y=lambda z:z[0]):
  "Divide lst of (num1,num2) using variance of num2."
  #----------------------------------------------
  def xpect(a,b):
    n = a.n() + b.n()
    return a.n()/n*a.spread() + b.n()/n*b.spread()
  def small(lst):
    f=lambda z: x(lst[int(z*len(lst))])
    return f(0.5+cohen)- f(0.5)
  #----------------------------------------------
  def argmin(lst): #Find best divide of 'lst'
    lhs, rhs  = Col(), Col(y(z) for z in lst)
    least, cut = rhs.spread(), None
    lo, hi    = x(lst[0]), x(lst[-1])
    for j,z in enumerate(lst): 
      x1, y1 = x(z), y(z)
      rhs - y1
      lhs + y1    
      if lhs.n() > width and rhs.n() > width: 
        x2 = x(lst[j+1])
        if x1 != x2:
          if x1 - lo >= epsilon:
            if hi - x2 >= epsilon:
              tmp = xpect(rhs,lhs) 
              print(tmp,least)
              if tmp < least :  
                 cut, least = j+1, tmp
    return cut
  #----------------------------------------------
  def recurse(lst):
    cut = argmin(lst)
    if cut: 
      recurse(lst[:cut])
      recurse(lst[cut:])
    else:   
      cuts.append(lst)
  #---| main |-----------------------------------
  cuts=[]
  if lst: 
    lst = sorted([z for z in lst if z != my.ignore],key=x)
    if epsilon == None: epsilon = small(lst)
    width = max(2,int(len(lst)/q))
    print(width)
    recurse(lst)
  return cuts

