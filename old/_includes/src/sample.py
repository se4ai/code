class Sample:
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
      return x
    elif random.random() <= now/i.n:
      i.all[ int(r() * now) ]= x
      return x
