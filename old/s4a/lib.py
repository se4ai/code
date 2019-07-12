# /* vim: set ts=2 sts=2 sw=2 et : */
#--------- --------- --------- --------- --------- ---------
import random,re,sys,zipfile

#--------- --------- --------- --------- --------- ---------
from about import *
from boot import *

my = cli(about())

#--------- --------- --------- --------- --------- ---------
def err(a,b):
    sys.stderr.write(("#E> "+a+"\n")%b)
    sys.exit()

#--------- --------- --------- --------- --------- ---------
class ok:
  tries,fails = 0,0  #  tracks the record so far
  def __init__(i,fun=None):
    def score(t, f): 
      return f"# PASS= {t-f} FAIL= {f} %PASS = {(t-f)/(t+0.0001):.0%}"
    if not fun:     
      return print(score(ok.tries, ok.fails))
    try:
      ok.tries += 1
      print("### ",fun.__name__)
      fun()
    except Exception:
      ok.fails += 1
      print(ok.fails,ok.tries)
      import traceback
      print(traceback.format_exc())
      print(score(ok.tries, ok.fails),':',fun.__name__)

#--------- --------- --------- --------- --------- ---------
r  = random.random
any= random.choice

