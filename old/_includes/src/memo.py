def memo0(f):
  name = f.__name__
  def g(i):
   if name not in i.memo:
     i.memo[name] = f(i)
   return i.memo[name]
  return g

