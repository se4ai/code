from main import my
from rows import Rows

def cols(src):
 "Skip columns that start with a name containing my.ignore."
 skips = None
 for row in src:
   skips = skips or [x for x in row if my.ignore in x]
   yield [x for x,skip in zip(row,skips) if not skip]

def data(name="", header=[], rows=[]):
  out = None
  for row in cols(rows):
    if out: out + row
    else  : out = Rows(name, row)
  return out 
   
