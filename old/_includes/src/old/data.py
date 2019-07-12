# vim: ts=2 sw=2 sts=2 et:
#-------- -------- -------- -------- -------- --------
from config import *

def eras(src,shuffle=True,n=my.era):
  eras,lst = -1,[]
  for x in src:
    lst +=  [x]
    if len(lst) == n:
      eras += 1
      if shuffle: random.shuffle(lst)
      for y in lst: yield eras,y
      lst = []
  eras += 1
  if shuffle: random.shuffle(lst)
  for y in lst: yield eras,y

def data(name=None,headers=[], src=[], ignore="?"):
  "iterator that skips over ignore cols"
  tbl  = None
  skips = [ignore in txt for txt in headers]
  for cells in src:
    cells = [cell for cell,skip 
             in zip(cells,skips) if not skip]
    if tbl:
      yield tbl,cells
    else:
      tbl = Table(name=name,headers=headers)


src= eras('01230123012301230123012301230123',n=4)
for e,x in  src:
  print(e,x)
