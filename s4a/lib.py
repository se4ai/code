# /* vim: set ts=2 sts=2 sw=2 et : */
#--------- --------- --------- --------- --------- ---------
import argparse,random

r  = random.random
any= random.choice

#--------- --------- --------- --------- --------- ---------
def showd(d):
  ok   = lambda z  : isinstance(z,str) and z[0] != "_"
  show = lambda k,v: '%s=%s' % (k,v)
  lst  = sorted([show(k,v) for k,v in d.items() if ok(k)])
  return ', '.join(lst)

class o:
  def __init__(i,**d): i.__dict__.update(d)
  def __repr__(i): 
    return i.__class__.__name__+'{'+ showd(i.__dict__)+'}'

#--------- --------- --------- --------- --------- ---------
def cli(about):
  parser = argparse.ArgumentParser(
            epilog          = about.get("_epilog",""), 
            description     = about.get("_describe",""),
            formatter_class = argparse.RawDescriptionHelpFormatter)
  for key in about:
    if key[0] == "_": continue
    h,v = about[key]
    add = lambda **z: parser.add_argument("--"+key,**z)
    d   = v[0] if isinstance(v,list) else v
    if   isinstance(d,int)  : m,t= "I",int
    elif isinstance(d,float): m,t= "F",float
    else                    : m,t= "S",str
    if v is False :
      add(help=h, action="store_true")
    elif isinstance(v,list):
      add(help=h, choices=v,default=d,metavar=m ,type=t)
    else:
      add(help=h+("; e.g. %s"%v),default=d,metavar=m,type=t)
  return o(**parser.parse_args().__dict__)

#--------- --------- --------- --------- --------- ---------
