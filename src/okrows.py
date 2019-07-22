

"""

# okrows.py

"""
from ok   import ok
from lib  import *
from data import data
from auto import auto
from weather2 import weather2

@ok
def _data():
  rows = auto()
  lst  = sorted(rows.all,
          key=lambda z:z.doms(rows))
  for row in lst[:5] + lst[-5:]:
    print(row.id, row.doms(rows),
         [ row[g.pos] for g in rows.goals])

if __name__ == "__main__": ok()
