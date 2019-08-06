#!/usr/bin/env ./auk
# vim: nospell filetype=awk ts=2 sw=2 sts=2  et :
#--------- --------- --------- --------- --------- ---------

@include "lauk"
@include "tbl"

BEGIN { tests("tblok","_auto") }

function _weather(f,  t) { 
  Tbl(t)
  lines(t,"Tbl1","weather" DOT "csv")
  oo(t,"t")
}
function _auto(f,  t,r) { 
  srand(1)
  Tbl(t)
  lines(t, "Tbl1", "auto" DOT "csv")
  for(r in t.rows)
     print r, RowDoms(t.rows[r], t.rows, t)
}
