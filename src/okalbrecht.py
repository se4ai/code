from ok import ok
from albrecht import albrecht


@ok
def _albrecht():
  a = albrecht()
  nums0 = set(['$File', '<Effort', '$In', '$Out', 
               '$Query','$RawFPcounts', '$FpAdj'])
  nums  = set([col.txt for col in a.nums])
  syms0 = set()
  syms  = set([col.txt for col in a.syms])
  less0 = set(['<Effort'])
  less  = set([col.txt for col in a.less])
  more0 = set()
  more  = set([col.txt for col in a.more])
  print(100, set([1,2]) == set([1,2]))
  assert (nums0 & nums) == nums
  assert (syms0 & syms) == syms
  assert (less0 & less) == less
  assert (more0 & more) == more

if __name__ == "__main__": ok()
