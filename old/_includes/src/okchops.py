import timeit,chops 
from ok import ok
from sym import Sym
from num import Num
import random as r

r.seed(1)
@ok
def _chops1(n=40):
  lst = [[int(100*r.random()/20)] for _ in range(n)]
  for chop in chops.div(lst,q=4):
     print(len(chop),chop)

#@ok
def _chops2(n=1000):
  lst = sorted([r.random()**2 for _ in range(n)])
  for chop in chops.chops(lst,q=10):
     print(len(chop),chop[0],chop[-1])

#@ok
def _chops2(n=100):
  p = lambda z: int(10*z)
  lst  = [p(r.random()*10) for _ in range(n)]
  lst += [p(r.random()*20) for _ in range(n)]
  lst += [p(r.random()*30) for _ in range(n)]
  lst  = sorted(lst)
  print(lst[:int(n*1.5)])
  print("\n ")
  print(lst[int(n*1.5):])
  for chop in chops.chops(lst,q=10,epsilon=50):
     u, v = chop[0],chop[-1]
     print(len(chop),u,v, v-u)

#@ok
def _chops3():
  data= [
      ["overcast", 64, 65,"TRUE","yes"],
      ["rainy", 65, 70,"TRUE","no"],
      ["rainy", 68, 80,"FALSE","no"],
      ["sunny", 69, 70,"FALSE","yes"],
      ["rainy", 70, 96,"FALSE","no"],
      ["rainy", 71, 91,"TRUE","no"],
      ["overcast", 72, 90,"TRUE","no"],
      ["sunny", 72, 95,"FALSE","no"],
      ["rainy", 75, 80,"FALSE","yes"],
      ["sunny", 75, 70,"TRUE","yes"],
      ["sunny", 80, 90,"TRUE","yes"],
      ["overcast", 81, 75,"FALSE","yes"],
      ["overcast", 83, 86,"FALSE","ues"],
      ["sunny", 85, 85,"FALSE","yes"],
      ]
  #col1 = [x[1] for x in nums]
  #col2 = [x[2] for x in nums]
  get = lambda z:z[1]
  for chop in chops.chops(data,q=5,
               getx=get,
               isa=Sym,
               goals=[4],
               gety=lambda g,z:z[g]):
    u, v = get(chop[0]), get(chop[-1])
    print(len(chop),u,v, v-u)
    

#@ok
def _chops4():
  data= [
      [25,150,75,60,1,1750,1750,102.4],
      [193,98,70,36,1,1902,1902,105.2],
      [70,27,0,12,0.8,535,428,  11.1],
      [40,60,20,12,1.15,660,759,21.1],
      [10,69,1,9,0.9,478.89,431,28.8],
      [13,19,0,23,0.75,377.33,283,10],
      [34,14,0,5,0.8,256.25,205,8],
      [17,17,15,5,1.1,262.73,289,4.9],
      [45,64,14,16,0.95,715.79,680,12.9],
      [40,60,20,15,1.15,690.43,794,19],
      [41,27,29,5,1.1,465.45,512,10.8],
      [33,17,8,5,0.75,298.67,224,2.9],
      [28,41,16,11,0.85,490.59,417,7.5],
      [43,40,20,35,0.85,802.35,682,12],
      [7,12,13,8,0.95,220,209,4.1],
      [28,38,24,9,1.05,487.62,512,15.8],
      [42,57,12,5,1.1,550.91,606,18.3],
      [27,20,24,6,1.1,363.64,400,8.9],
      [48,66,13,50,1.15,1073.91,1235,38.1],
      [69,112,21,39,1.2,1310,1572,61.2],
      [25,28,4,22,1.05,476.19,500,3.6],
      [61,68,0,11,1,694,694,11.8],
      [15,15,6,3,1.05,189.52,199,0.5],
      [12,15,0,15,0.95,273.68,260,6.1],
      ]
  get = lambda z:z[1]
  for chop in chops.chops(data,q=4,
               getx=get,
               isa=Num,
               goals=[0],
               gety=lambda g,z:z[g]):
    u, v = get(chop[0]), get(chop[-1])
    print(len(chop),u,v, v-u)
    
if __name__ == "__main__": ok()
