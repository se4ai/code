# vim: ts=2 sw=2 sts=2 et:
#-------- -------- -------- -------- -------- --------

from config import *

class Row:
  id = 0
  def __init__(i,lst,table=None):
    i.has, i.table = lst,table
    i.id = row.id = row.id + 1
  def __getitem__(i, k   ): return i.has[k]	
  def __setitem__(i, k, v): return i.has[k] = v
  def __repr__(i)         : return 'row%s' % i.has

def kept(f):
  name = f.__name__
  def g(i):
   if name not in i._kept:
     i.kept[name] = f(i)
   return i.kept[name]
  return g

class Table:
  def __init__(i,name=None, headers=[]):
    "build the table, using the text in the headers"
    i.headers= headers 
    i.name = name
    i.rows = [] # stores all the rows
    col    = lambda j,s: Num(s,j) if my.num in s else Sym(s,j)
    i.cols = [col(pos,txt) for pos,text in enumerate(headers)]
    i.kept=  {}
  def __add__(i,cells):
    "add a row, update the colum summaries"
    [col + cell for col,cell in zip(i.cols,cells)]
    row = Row(cells,table=i)
    i.rows += [row]
    return row@keep
  def clone(i):
    "return a new data table that is like me"
    return Table(name=name, headers=i.headers)
  @kept
  def nums(i):
    return set(c for c in i.cols if 
     my.num in c.txt or my.less in c.txt or my.more in c.txt)
  @kept
  def syms():
    return  set(i.cols) - i.nums()
  @kept
  def less(i):
    return set(c for c in i.cols if my.less in c.txt)
  @kept
  def more(i):
    return set(c for c in i.cols if my.more in c.txt)
  @kept
  def klass(i):
    for c in i.cols:
      if my.klass in c.txt: return c
  @kept
  def dep(i):
    return i.less() & i.more() & set([i.klass()])
  @kept
  def indep(i):
    return set(i.cols) - i.dep()
  
