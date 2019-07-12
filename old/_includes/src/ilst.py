class has:
  def __init__(i,lst=[]):
    i.lst, i.new = lst, True
  def __getitem__(i,k  ): return i.lst[k]
  def __setitem__(i,k,v): return i.new=True; i.lst[k]=v
  def __repr__(i)       : return '<%s' % i.lst
  def sorted(i):
    if i.changed:
      i.lst = sorted(i.lst,key=lambda z:z)
      i.changed = False
    return i.lst

