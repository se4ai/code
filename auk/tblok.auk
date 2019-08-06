#!/usr/bin/env ./auk
# vim: nospell filetype=awk ts=2 sw=2 sts=2  et :
#--------- --------- --------- --------- --------- ---------

@include "lauk"
@include "tbl"

BEGIN { tests("tblok","_auto") }

function _weather(f,  t,com) { 
  Tbl(t)
  lines(t,"Tbl1","weather" DOT "csv")
  oo(t,"t")
}
function _auto(f,  t,r,n) { 
  srand(1)
  Tbl(t)
  lines(t, "Tbl1", "auto" DOT "csv")
  for(r in t.rows) 
    RowDoms(t.rows[r], t.rows, t)
  ksort(t.rows,"dom")
  n = length(t.rows)
  for(r=1;r<=5;r++)
    print(t.rows[r].oid "\t" flat(t.rows[r].cells, t.my.goals)) 
  print ""
  for(r=n-5;r<=n;r++)
    print(t.rows[r].oid "\t" flat(t.rows[r].cells, t.my.goals)) 
}
