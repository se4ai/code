# vim: ts=2 sw=2 sts=2 et:
#-------- -------- -------- -------- -------- --------

from config import * 

def chops(lst,q=my.bins,e=0,cohen=my.cohen):
  """divide lst into 'q' groups, where max-min of each
   group is larger than epsilon 'e' (and if 'e' is
   None, compute from a small chunk near middle of list)"""
  lst = sorted(lst) 
  n   = len(lst) 
  q   = min(q,n-1)
  if e is None:
    e = lst[int(n*(0.5+cohen/2))] - lst[int(n*0.5)]
  w   = int(n/q)
  out = [lst[0]]
  i   = 0
  while i < n - w - 1:
    i += w
    while i < n - 1 and (
      lst[i] == lst[i+1]     # the next is the same
      or lst[i] <  out[-1]+e # or this chop is trivial
      ): i += 1              # so jump ahead
    if i<n: 
      out += [lst[i]]
  return out
