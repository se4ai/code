# /* vim: set ts=2 sts=2 sw=2 et : */
#--------- --------- --------- --------- --------- ---------
#iterate over strings, files, zipped files

from xy import *

def string(s):
  for line in s.splitlines(): yield line

def file(fname):
  with open(fname) as fs:
      for line in fs: yield line.rstrip()

def zipped(archive,fname):
  with zipfile.ZipFile(archive) as z:
     with z.open(fname) as f:
        for line in f: yield line

def rows(src, doomed = r'([\n\t\r ]|#.*)'):
  """e.g. for row in rows(file("weather.csv")): ... """
  use, txt = [], ""
  want = lambda z: z[0] != no
  for line in src:
    txt += re.sub(doomed, '', line)
    if txt and txt[-1] != my.sep:
      lst = txt.split(my.sep) 
      if lst:
        txt = ""
        use = use or [n for n,s in enumerate(lst) 
                      if s[0] != my.ignore] 
        if len(lst) < len(use):
          err("wanted %s cells, got %s in %s", 
              (len(use), len(lst),lst))
        yield [lst[n] for n in use]

#--------- --------- --------- --------- --------- ---------
#iterate over rows in file, coercing columns to data types

def cells(src):
  funs = None
  def ako(x):
    try: return int(x) and int
    except:
      try: return float(x) and float
      except ValueError: return str
  def prep(n,x):
    if x is my.ignore: return x
    fun = funs[n] = funs[n] or ako(x)
    try: return fun(x)
    except ValueError:
      err("wanted %s in col %s, got [%s]",
          ( fun.__name__,n,x))
  for lst in src:
    if not funs:
      funs = funs or [None for _ in lst]
      yield lst
    else:
      yield  [prep(n,x) for n,x in enumerate(lst)]

#--------- --------- --------- --------- --------- ---------
# iterate over cells, diviting them into independent and
# dependent cells

def xy(src, goalp=my.less+my.more+my.klass):
  xs, ys = [], []
  for lst in src:
    if not xs:
      for n,s in enumerate(lst):
        what  = ys if s[0] in goalp else xs
        what += [n]
    yield [lst[n] for n in xs], [lst[n] for n in ys]
