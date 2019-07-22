from math import log

class o:
  def __init__(i,**kw): i.__dict__.update(kw)

my = o( 
       read = o(ignore="?")
       misc = o(private="_")
      )

class Pretty(object):
  def __repr__(i):
    pairs = sorted([(k,v) for k,v in i.__dict__.items()
                    if k[0] != my.misc.private])
    pre = i.__class__.__name__ + '{'
    q=lambda z: "'%s'" % z if isinstance(z,str)  else str(z)
    return pre + ", ".join(['%s=%s' % (k,q(v)) 
                           for k,v in pairs]) + '}'

class Num(Pretty):
  def __init__(i): i.n=0; i.lo= 10**32; i.hi = -1*i.lo
  def __call__(i,x): 
    i.n  += 1
    x=i.prep(x)
    i.lo,i.hi = min(x,i.lo), max(x,i.hi)
    i.mu += (x - i.mu) /i.n
    return x
  def p(i,x): 
    a,c,b = i.lo, i.mu, i.hi
    if a <= x < c : return 2*(x-a)/((b-a)*(c-a))
    if c < x <= b : return 2*(b-x)/((b-a)*(b-c))
    if x==c       : return 2/(b-a)
    return 0
  def variety(i):
    a,c,b = i.lo, i.mu, i.hi
    return  (a*a + b*b +c*c - a*b - a*c - b*c)/18
    
class Int(Num):
  def prep(i,x): return int(x)
class Float(Num):
  def prep(i,x): return float(x)

class Sym(Pretty):
  def __init__(i): i.n=0; i.d={}; i.most=0;i.mode=None
  def __call__(i,x):
    i.n += 1
    m=i.d[x] = i.d.get(x,0) + 1
    if m >  i.most: i.most,i.mode = m,x
    return x
  def p(i,x):
    return  i.d.get(x,0) / n
  def variety(i):
    e = 0
    for v in i.d.values():
      p  = v/i.n
      e -= p * log(p,2)
    return e

class Row(Pretty):
  id=0
  def __init__(i,lst,seen) : 
    i.lst,i.seen = lst,seen
    i.id = Row.id = Row.id+1

def token(x,ako,name):
  if x=="?":return x,ako
  if ako   :return ako(x),ako
  try      :return int(x),Int(name)
  except: 
    try    :return float(x),Float(name)
    except :return x,Sym(name)

def rows(src):
  seen, txts = None,None
  for row in cols(src):
    seen = seen or [None] * len(row)
    if txts:
      for n,(one,txt,x) in enumerate(zip(seen,txts,row)):
        row[n], seen[n] = token(x,one,txt)
      yield Row(row,seen)
    txts = row

def cols(src):
 use,no = None,my.read.ignore
 for row in src:
   use = use or [n for n,x in enumerate(row) if no not in x]
   yield [row[n] for n in use]

def data(name="",  src=[]):
  for row in rows(src):
    yield row
