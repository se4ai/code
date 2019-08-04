#!/usr/bin/env zzz

# -----------------------------------
# macros: camel case

define(Col,`name,n')
define(Num,`hi,lo,mu,m2,sd')
define(Sym,`mode,most,cnt')
define(Row,`cells,dom')
define(All,`Col,Num,Sym,Row')

# -----------------------------------
# Constants: all uppercase

BEGIN  {
  SEP=","
  SKIPCOLUMN= "\\?"
  IGNORE = SKIP
  NUMCOLUMN = "\\$"
print 1
}
# -----------------------------------
# Main

function main(  c,line,r,lst, All) {
  while(getline line > 0) {
    r++
    split(line,vs,SEP)
    for(c in lst)
      if (r==1)
        create(c,lst[c], All)
      else
        cells[r][c] = update(c,vs[c],All)
}} 
function create(c,v, All) {
  if (v ~ SKIPCOLUMN) continue
  colCreate(c,v,Col)
  v  ~ NUMCOLUMN ? numCreate(v,c,Num) : symCreate(v,c,Sym)
} 
function update(c,v, All) {
  if(ignored(c,Col)  continue
  if (v ~ IGNORE) continue
  colUpdate(c,v,Col)
  return nump(c,Col) ? numUpdate(c,v+0,Col,Num) : symUpdate(c,v,Sym)
} 

# -----------------------------------
# predicates

function ignored(c,Col)  {return ! (c in name)}
function nump(c,Num)    {return c in mu}

# -----------------------------------
# columns

function colCreate(c,v,Col) {
  n[c] = 0
  name[c] = v
}
function colUpdate(c,v,Num) {
  n[c]++
  return v
}

# -----------------------------------
# Symbolic columns

function symCreate(c,v,Sym) {
  most[c] = mode[c] = 0 
}
function symUpdate(c,v,Sym) {
  tmp = ++cnt[c][v]
  if (tmp > most[c]) {
    most[c] = tmp
    mode[c] = v }
  return v
}

# -----------------------------------
# Numeric columns

function numCreate(c,v,Num) {
  mu[c] = n2[c] = sd[c] = 0
  lo[c] = 10^32; 
  hi[c] = -1*lo[c]
}
function numUpdate(c,v,Col,Num, d) {
  lo[c]  = v < lo[c] ? v : lo[c]
  hi[c]  = v > hi[c] ? v : hi[c]
  d      = v - mu[c]
  mu[c] += d/n[c]
  m2[c] += d*(v - mu[c])
  sd[c]  = n[c] < 2 ? 0 : (m2[c]/(n[c] - 1))^0.5
  return v
}
