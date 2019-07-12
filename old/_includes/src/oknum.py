import math,num,ok 
from num import Num

@ok.ok
def _num1():
  n= Num([9,2,5,4,12,7,8,11,9,3,7,4,12,5,4,10,9,6,9,4])
  assert math.isclose(n.sd,3.0608,abs_tol=0.001)
  assert n.mu == 7

@ok.ok
def _num3():
  l1= [9,2,5,4,12,7,8,11,9,3,7,4,12,5,4,10,9,6,9,4]
  l2= [x*100 for x in l1]
  l0= l1 + l2
  n1=Num(l1)
  n2=Num(l2)
  n0=Num(l0)
  print(n0.simpler(n1,n2))

if __name__ == "__main__": ok.ok()
