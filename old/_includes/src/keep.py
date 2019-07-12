def kept(f):
  name = f.__name__
  def g(i):
   if name not in i._kept:
     i.kept[name] = f(i)
   return i.kept[name]
  return g

