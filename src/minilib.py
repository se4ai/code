import sys,re,traceback,random

r=random.random
seed=random.seed
one=random.choice

def lt(x,y): return x < y
def gt(x,y): return x > y

def close(x,y,near=0.01): return y*(1-near) <=x<= y*(1+near)

def interpolate(x, xy):
  x1, y1 = xy[0]
  if x < x1: return y1
  for x2, y2 in xy[1:]:
    if x1 <= x < x2:
      return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    x1, y1 = x2, y2
  return y2

class Thing(object):
  def __repr__(i):
    pairs = sorted([(k,v) for k,v in i.__dict__.items()
                    if k[0] != "_"])
    pre = i.__class__.__name__ + '{'
    q=lambda z: "'%s'" % z if isinstance(z,str)  else str(z)
    return pre + ", ".join(['%s=%s' % (k,q(v)) 
                          for k,v in pairs]) + '}'
class o(Thing):
  def __init__(i,**kw): i.__dict__.update(kw)


from functools import wraps

def memo(f):
  "Memo index does NOT includes first argument"
  name = f.__name__
  @wraps(f)
  def g(i, *arg, **kw):
   if name not in i._memo:
     i._memo[name] = f(i, *arg, **kw)
   return i._memo[name]
  return g

def memos(k, what='0', decorator=memo):
  "Turn  methods ending with 'what' into a memoed property"
  for f in dir(k):
    if callable(getattr(k, f)):
      if f[-1] == what:
        setattr(k,f[:-1], property(decorator(getattr(k,f))))
  return k


def shuffle(lst):
  random.shuffle(lst)
  return lst

class ok:
  tries,fails = 0,0  #  tracks the record so far
  d={}
  def __init__(i,fun):
    k=i.__class__.__name__
    ok.d[k] = ok.d.get(k,[]) + [fun]
  def run1(fun,k):
    def score(t, f): 
      return f"PASS= {t-f} FAIL= {f} %PASS = {(t-f)/(t+0.0001):.0%}"
    try:
      ok.tries += 1
      if fun.__doc__:
        print("# "+ re.sub(r'\n[ \t]*',"\n# ", fun.__doc__))
      fun()
    except Exception:
      ok.fails += 1
      print(traceback.format_exc())
    print("##",k,score(ok.tries, ok.fails),':',fun.__name__)
  def run(k=None):
    if k:
      for fun in ok.d.get(k,[]): ok.run1(fun,k)
    else:
      for k,funs in ok.d.items(): ok.run(k) 
  def main(lst):
    if len(lst)> 1 and lst[1] in ok.d:
      ok.run(lst[1])
    else:
      ok.run()
    if ok.fails>0: sys.exit(1)
 
