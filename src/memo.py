"""

# memo.py

## About

Defines a memo wrapper for methods that caches
memo results in the dictionary `i._memo`. 

## The Code

"""

from functools import wraps

def memo0(f):
  "Memo index does NOT includes first argument"
  name = f.__name__
  @wraps(f)
  def g(i, *arg, **kw):
   if name not in i._memo:
     i._memo[name] = f(i, *arg, **kw)
   return i._memo[name]
  return g

def memo1(f):
  "Memo index includes first argument"
  name = f.__name__
  @wraps(f)
  def g(i, *arg, **kw):
   key=(name,arg[0])
   if key not in i._memo:
     i._memo[key] = f(i, *arg, **kw)
   return i._memo[key]
  return g

"""

## memos: class decorator

Convert all class methods ending in `0` or `1`' to
properties that call memoed functions. For example
the method `sd0` would be converted into a property `aa`
that calls the function `aa0` memoed using `memo0`.
Also `aa1` would become a property calling a function
memoed via `memo1`.

Also, the decorate adds
`i._memo={}` to the initialization method.

"""
def memos(k):
  setattr(k, "__init__", fresh(getattr(k,"__init__")))
  memoPrim(k,'0',memo0)
  memoPrim(k,'1',memo1)
  return k

def memoPrim(k, what='0', decorator=memo0):
  "Turn  methods ending with 'what' into a memoed property"
  for f in dir(k):
    if callable(getattr(k, f)):
      if f[-1] == what:
        setattr(k,f[:-1], property(decorator(getattr(k,f))))

def fresh(f):
  "Add `_memo` initialization to the constructor"
  @wraps(f)
  def g(i,*lst,**kw):
    i._memo={}
    f(i,*lst,**kw)
  return g

"""

## Useful Idiom

The idiom `i._memo={}` resets the memos and forces
a recalculation of all vales. This is recommended
when:

- A class' internal state changes;
- You you want all the memos recalculated.

## Example Usage

See [col](col.md/#Num)

"""
