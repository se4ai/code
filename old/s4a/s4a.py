# /* vim: set ts=2 sts=2 sw=2 et : */
#--------- --------- --------- --------- --------- ---------

import lib,xxx

def helps(): return [
"""
Rally: a challenging approach to data mining.
(C) 2018, tim@menzies.us UNLICENSE
This is free and unencumbered software released into the public domain.
""","""
"Give me the fruitful error any time, full of seeds, bursting with
its own corrections. You can keep your sterile truth for yourself."
-- Vilfredo Pareto

""",
  # sway
  help("run unit tests",                   tests   = False),
  #elp("tiles display width",              tiles   = 40),
  #elp("small effect size (Cliff's dela)", cliff   = [0.147, 0.33, 0.474]),
  help("keep at most, say, 128 samples",   samples = [128,256,128,512,1024]),
  help("y-axis bins",                      bins    = [5,2,3,4,6,7,8,9,10]),
  help("era size",                         era     = 10),
  help("in pretty print, round numbers",   round   = 3),
  help("random number seed",               seed    = 61409389),
  help("ignore cells, cols characters",    ignore  = "?"),
  help("class character",                  klass   = "!"),
  help("repeats",                          repeats = [5,10]),
  help("n-ways",                           nways   = [3,5,10]),
  help("training data (csv format)",       train   = "train.csv"),
  help("testing data (csv format)",        test    = "test.csv"),
  help("verbose print",                    verbose = True),
  # --------------------------------------------------------------------
  # System
  help("Run some test function, then quit",       run       = "")
  ]

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

THE = options(*helps())



