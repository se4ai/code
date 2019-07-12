import re,traceback

def ok(f=None, the=dict(all=[],tries=0,fails=0)):
  if f:
    the["all"] += [f]
  else:
    for f in the["all"]:
      print("\n-----| %s |%s" % (f.__name__,"-"*40))
      if f.__doc__:
        print("# "+ re.sub(r'\n[ \t]*',"\n# ", f.__doc__))
      the["tries"] += 1
      try: 
        f()
      except Exception:
        the["fails"] += 1
        print(traceback.format_exc())
      t,f = the["tries"], the["fails"]
      p   = (t-f)/(t+0.0001)
      print(f"# PASS= {t-f} FAIL= {f} %PASS= {p:.0%}")
