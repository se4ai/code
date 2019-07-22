"""

# row.py: a place to store cells

"""
from main import my
from row  import Row
from col  import Col
from memo import memos
from lib  import Pretty
import sys

@memos
class Rows(Pretty):
  def __init__(i,name=None, headers=[]):
    "build the table, using the text in the headers"
    i.headers = headers
    i.name    = name
    i.all     = [] # stores all the rows
    i.cols    = set([Col(pos=n, txt=txt) 
                     for n,txt in enumerate(headers)])
    for col in i.less: col.w = -1
    for col in i.more: col.w =  1
  def __add__(i,cells):
    "add a row, update the column headers"
    for col in i.cols:
      col + cells[col.pos]
    row = Row(cells)
    i.all += [row]
    return row
  def clone(i):
    "return a new data table that is like me"
    return Table(name=i.name, headers=i.headers)
  def klass0(i):
    for c in i.cols:
      if my.rows.klass in c.txt: return c
  def nums0(i):
    return set(c for c in i.cols if my.rows.nums in c.txt or 
             my.rows.less in c.txt or my.rows.more in c.txt)
  def syms0(i):  return i.cols - i.nums
  def less0(i):  return set(c for c in i.cols if my.rows.less in c.txt)
  def more0(i):  return set(c for c in i.cols if my.rows.more in c.txt)
  def dep0(i):   return i.less | i.more | set([i.klass])
  def indep0(i): return i.cols - i.dep
  def goals0(i): return i.less | i.more 
