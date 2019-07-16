from main import my
from rows import Rows

def cols(src):
 "Skip columns that start with a name containing my.ignore."
 wants = None
 for row in src:
   wants = wants or [n for n,x in enumerate(row)
                     if my.rows.ignore not in x]
   yield [row[want] for want in wants]

def data(name="",  rows=[]):
  out = None
  for row in cols(rows):
    if out: out + row
    else  : out = Rows(name, row)
  return out 
