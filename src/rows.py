"""

# row.py: a place to store cells

"""
from row  import Row
from memo import memos
from lib  import Pretty

@memos
class Rows(Pretty):
  def __init__(i,name=None, headers=[]):
    "build the table, using the text in the headers"
    i.headers= headers
    i.name = name
    i.all  = [] # stores all the rows
    # reason about the headers
    col  = lambda j,s: (Num if my.num in s else Sym)([],s,j)
    i.cols = [col(c,txt) for c,txt in enumerate(headers)]
    for col in i.less: col.w = -1
    for col in i.more: col.w =  1
  def __add__(i,cells):
    "add a row, update the column headers"
    [col + cell for col,cell in zip(i.cols,cells)]
    row = Row(cells)
    i.all += [row]
    return row
  def clone(i):
    "return a new data table that is like me"
    return Table(name=name, headers=i.headers)
  # -- header stuff. Report different headers
  def klass0(i):
    for c in i.cols:
      if my.klass in c.txt: return c
  def nums0(i):
    return set(c for c in i.cols if
     my.num in c.txt or my.less in c.txt or my.more in c.txt)
  def syms0():  return set(i.cols) - i.nums
  def less0(i): return set(c for c in i.cols if my.less in c.txt)
  def more0(i): return set(c for c in i.cols if my.more in c.txt)
  def dep0(i):  return i.less & i.more & set([i.klass])
  def indep0(i):return set(i.cols) - i.dep
  def goals0(i):return i.less & i.more 


