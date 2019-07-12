"""
# ok.py: a simple unit test engine

This unit test engine is strongly inspired by Kent Beck's most
excellent [making making](https://www.youtube.com/watch?v=nIonZ6-4nuU)
video.

## Example usage

Here a demo file that tests the test engine.  Any function wrapped
in `@ok` gets added to a test list.  Then, finally, in `ok()` is
called, all those tests run. And if any crash, then the test engine
just jumps to the next test function.


```python
from ok import ok

@ok
def ok1():
  "This will always fail."
  assert 2==1, "oops"

@ok
def ok2():
  "This will always pass."
  assert 10 == sum([1,2,3,4]), "should not fail"

if __name__ == "__main__": ok()

```

## Useful Features


If a test function contains a documentation string, then that
is printed as part of the test process.

Calling `python3 ok.py` will make this code run all the tests
  in all the  `okXX.py` files in the current directory.

## The Code

"""
import re,traceback,glob

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

if __name__ == "__main__":
  for f in glob.glob("ok*.py"):
    if not "-" in f:
      m   = re.sub(r'.py',"",f)
      com = "from %s import *" % m
      print("# " + com)
      exec(com)
  ok()  


"""

## Comprehension Exercises

Skim over all the `okXX.py` files to get a sense of how to use this
code/ Write a file `okMyTest.py` that checks if 1+1 equals two.

"""
