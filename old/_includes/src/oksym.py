import math,sym,ok

@ok.ok
def _sym1():
  n = sym.Sym(list('abbcccc'))
  assert math.isclose(n.ent(),1.3787836,abs_tol=0.001)
  assert n.mode == 'c'

if __name__ == "__main__": ok.ok()
