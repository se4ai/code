from ok import ok

@ok
def ok1():
  """always check that the test 
     engine knons about failure"""
  assert 1==2,'well that is a complete surprise'

@ok
def ok2():
  "this should work"
  x=4/2
  assert x==2

@ok
def ok3():
  "and this too"
  x=4/2
  assert x==2


