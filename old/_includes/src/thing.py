from config import my

class Thing:
  def simpler(i,j,k):
    n   = j.n + k.n
    assert i.n == n, "sub things not of same size"
    new = j.n/n * j.spread() + k.n/n * k.spread()
    old = i.spread() * (1-my.simplerBy)
    #print(dict(inn=i.n,ie=i.spread(), jn=j.n,jsd=j.spread(), kn=k.n,ksd=k.spread()))
    return new < old
