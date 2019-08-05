#!/usr/bin/env ./auk
# vim: nospell filetype=awk ts=2 sw=2 sts=2  et :

@include "lauk"

#--------- --------- --------- --------- --------- ---------
BEGIN  {
  SKIPCOL = "\\?"
  IGNORE  = SKIPCOL
  NUMCOL  = "\\$"
}
BEGIN { _demo("weather" DOT "csv") }
function _demo(f,  i,j,t) { 
  Num(i,"c","v")
  for(j=1;j<=100;j++) Num1(i,j)
  Tbl(t)
  lines(t,"Tbl1",f) 
  #oo(k,"t")
}
#------------------------------------------------------------
function Row(i,t,lst,     c) {
  Object(i)
  i.dom = 0
  for(c in t.cols) 
    i.cells[c] = Col1(t.cols[c], lst[c]) 
}
#------------------------------------------------------------
function Tbl(i) { 
  Object(i)
  has(i,"nums")
  has(i,"syms")
  has(i,"cols")
  has(i,"rows") 
}
function Tbl1(i,r,lst) {
  if (r==1)  {
    for(c in lst)
      if (lst[c] !~ SKIPCOL) 
        TblCols(i, c, lst[c])
  } else  
    has2(i.rows,r,"Row",i,lst)  
}
function TblCols(i,c,v) {
  if (v ~ NUMCOL) { i.nums[c]; has2(i.cols,c,"Num",c,v) }
  else            { i.syms[c]; has2(i.cols,c,"Sym",c,v) }
}
#------------------------------------------------------------
function Col(i,c,v) { 
  Object(i)   
  i.n=0
  i.col=c
  i.txt=v 
} 
function Col1(i,c,v,   add) {
  if (v ~ IGNORE) return v
  i.n++
  add = i.add
  return @add(i,c,v)
} 
#------------------------------------------------------------
function Sym(i,c,v) { 
  Col(i,c,v)
  i.mode=""
  i.most=0
  has(i,"cnt") 
  i.add ="Sym1" 
}
function Sym1(i,c,v) {
  tmp = ++i.cnt[v]
  if (tmp > i.most) {
    i.most = tmp
    i.mode = v }
  return v
}
#------------------------------------------------------------
function Num(i,c,v) {
  Col(i,c,v)
  i.n  = i.mu = i.m2 = i.sd = 0
  i.lo = 10^32 
  i.hi = -1*i.lo
  i.add ="Num1" 
}
function Num1(i,v,    d) {
  v += 0
  i.lo  = v < i.lo ? v : i.lo
  i.hi  = v > i.hi ? v : i.hi
  d     = v - i.mu
  i.mu += d/i.n
  i.m2 += d*(v - i.mu)
  i.sd  = i.n < 2 ? 0 : (i.m2/(i.n - 1))^0.5
  return v
}
