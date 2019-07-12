from ok import ok

@ok
def ok1(): 
  "This will always fail."
  assert 2==1, "oops"

@ok
def ok2(): 
  "This will always pass."
  n = sum([1,2,3,4])
  assert n==10, "should not fail"

if __name__ == "__main__": ok()
