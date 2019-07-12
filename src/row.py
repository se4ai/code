"""

# row.py: a place to store cells

A `row` has `cells` which can be
accessed via `aRow.cells[j]` or
(more conveniently) `aRow[j]`.
A `row` caches a `doms` score
which is an approximate
guess of how often this row has
best goals.

Rows will know how to mutate their cells, soon.

"""
from memo import memos,fresh
from lib  import Pretty

@memos
class Row(Pretty):
  id = 0
  def __init__(i,lst):
    i.cells = lst
    i.id = Row.id = Row.id + 1
  @fresh
  def __setitem__(i, k, v): i.cells[k] = v
  def __getitem__(i, k   ): return i.cells[k]
  def doms0(i,rows):
    n = my.someDom
    return sum([ i.dominates( any(rows.all), rows)
                 for _ in range(n) 
              ]) / n
  def dominates(i,j,rows):   
    s1, s2, n = 0, 0, len(rows.goals()) 
    for goal in rows.goals():
      a,b = i[goal.pos], j[goal.pos]
      a,b = goal.norm(a), goal.norm(b)
      s1 += 10**(goal.w * (a-b)/n)
      s2 += 10**(goal.w * (b-a)/n)
    return s1/n < s2/n

"""

## Comprehension Questions

1. Read [A Guide to Python's Magic Methods](https://rszalski.github.io/magicmethods/).  What do the methods `__init__, __getitem__, __setitem__, __repr__` do?
2. Read [memo.py](memo.md). What does the class decorate `@memos` do?
3. In [Num](col.md#num), what does normalization do?
4. This code often crashes if, in `dominates`, the `a,b` values are not normalized.
   Why?
5. Read [On the Value of User Preferences in Search-Based Software
   Engineering](http://bit.ly/2LfLaFP), Section III.c to learn the
   difference between continuous and discrete domination. Then read
   the "%correct" column of Table 8, noting that IBEA uses continuous
   domination while all the other optimizers use discrete domination.
   Based on that table, when is boolean domiantion better than continuous?

"""
