# vim: ts=2 sw=2 sts=2 et:
#-------- -------- -------- -------- -------- --------

class Col:
  def __init__(i,txt,pos):
    i.txt,i.pos,i.n = txt,pos,0
    i.setup()
  def __add__(i,x):
    if x != my.ignore: 
      i.n += 1
      i.add(x)
    return x

class Sym(Col):
  "track symbols seen in a column"
  def setup(i): 
    i.most,i.mode,i.bag = 0,nil,{}
  def expect(i): return i.mode
  def add(i,x):
    i.n += 1
    new = i.bag[x] = i.bag.get(x,0) + 1
    if new > most:
      most,mode=new,x

class Num(Col):
  "track numbers seen in a column"
  def setup(i):
    i.mu,i.sd,i.m2 = 0,0,0
    i.lo,i.hi      = my.inf, -1*my.inf
  def expect(i): return i.mu
  def add(i,x):
    i.n  += 1
    d     = x - i.mu
    i.mu += d/i.n
    i.m2 += d*(x - i.mu)
    i.sd  = (i.m2/(i.n - 1 + my.tiny))^0.5
    if x < i.lo: i.lo = x
    if x > i.hi: i.hi = x

class Sample(Col):
  "Keep, at most, 'size' things."
  def __init__(i, max=my.keep):
    i.max,i.n,i.all  = 0,max,[] 
    i.ordered = False
  def expect(i):
    if not i.ordered:
      i.lst = sorted(i.lst)
      i.ordered=True
    return i.lst[int(len(i.lst)/2)] 
  def add(i,x):
    i.ordered = False
    now  = len(i.all)
    if now < i.max:
      i.all += [x]
    elif random.random() <= now/i.n:
      i.all[ int(r() * now) ]= x
    return i
  
