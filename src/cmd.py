import sys,re,random,argparse,traceback,time,math,copy,pprint
class default: pass
  def __call__(i): return i.default
 
class runs(default):
  def __init__(i,txt="",x=0,lo=0,hi=1): 
    i.txt=txt; i.default=x; i.lo=lo; i.hi=hi
class has(default):
  def __init__(i, txt="", lst=[]): 
    i.txt=txt; i.default=lst[0]; i.lst=lst
class bool(default):
  def __init__(i, txt="", x=False): 
    i.txt=txt; i.default=x; i.lst=[False,True]
class val(default):
  def __init__(i, x): i.default=x

def defaultp(x): 
 return isinstance(x,(default))


def helps(): 
  def options(): return O(
    header=z("""
          Rally: a challenging approach to data mining.
          (C) 2018, tim@menzies.us UNLICENSE
          This is free and unencumbered software released into the public domain.
          """),
    mantra="""
          Ethics are choices. And not choosing is unethical.
          """,
    sway = O(
             tests = bool("run unit tests"),
             tiles = num("devisions for stats", 2,100),
             samples = one("keep at most, say, 128 samples", [128,256,128,512,1024]),
             ),
    other =  one("y-axis bins",[5,2,3,4,6,7,8,9,10]),
    stuff = O(
             era= one("era size",[10,20,30,40]),
             round= int("in pretty print, round numbers", 1,5))
  )
  class O:
    def __init__(i,**kw): i.__dict__.update(kw)
  class Within:
    def __init__(i,txt,lst,zero): i.txt, i.oneOf, default=txt,lst,zero
  class Over:
    def __init__(i,txt,lo,hi,intp=False): i.txt, i.loi,i.hi, i.intp= txt,lo,hi,intp
  def bool(s)       : return Within(s,[True,False],False)
  def one(s,lst)    : return Within(s,lst,lst[0])
  def num(s,lo,hi): return Over(s,lo,hi)
  def int(s,lo,hi)  : return Over(s,lo,hi,intp=True)
  def z(s): return "\n".join([s.lstrip() for s in  s.splitlines() if s])
  return options()

helps()

def help(h, **d):
  def help1():
    if val is False :
      return dict(help=h, action="store_true")
    if isinstance(val,list):
      return dict(help=h, choices=val,default=default, metavar=m ,type=t)
    else:
      return dict(help=h + ("; e.g. %s" % val), default=default, metavar=m, type=t)
  key,val = list(d.items())[0]
  default = val[0] if isinstance(val,list) else val
  m,t = "S",str
  if isinstance(default,int)  : m,t= "I",int
  if isinstance(default,float): m,t= "F",float
  return "--" + key, help1()

def options(before, after, *lst):
  parser = argparse.ArgumentParser(epilog=after, description = before,
              formatter_class = argparse.RawDescriptionHelpFormatter)
  for key, rest in lst:
    parser.add_argument(key,**rest)
  return parser.parse_args()

#THE = options(*helps())


