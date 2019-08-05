#!/usr/bin/env ./auk
# vim: nospell filetype=awk ts=2 sw=2 sts=2  et :
#--------- --------- --------- --------- --------- ---------

@include "lauk"
@include "col"

BEGIN  {
  SKIPCOL = "\\?"
  NUMCOL = "[<>\\$]"
  GOALCOL= "[<>!]"
}
#------------------------------------------------------------
function Row(i,t,lst,     c) {
  Object(i)
  has(i,"cells")
  i.dom = 0
  for(c in t.cols) 
    i.cells[c] = Col1(t.cols[c],  lst[c]) 
}
#------------------------------------------------------------
function Tbl(i) { 
  Object(i)
  has(i,"my")
  has(i,"cols")
  has(i,"rows") 
}
function Tbl1(i,r,lst,    c) {
  if (r==1)  {
    for(c in lst)
      if (lst[c] !~ SKIPCOL) 
        TblCols(i, c, lst[c])
  } else  
    has2(i.rows,r,"Row",i,lst)  
}
function TblCols(i,c,v) {
  if (v ~ CLASSCOL) i.my.class = c
  v ~ GOALCOL ? i.my.goals[c]: i.my.xs[c]
  v ~ NUMCOL  ? i.my.nums[c] : i.my.syms[c]
  has2(i.cols,c,
       v ~NUMCOL ? "Num" : "Sym",
       c,v) 
}

