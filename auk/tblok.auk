#!/usr/bin/env ./auk
# vim: nospell filetype=awk ts=2 sw=2 sts=2  et :
#--------- --------- --------- --------- --------- ---------

@include "lauk"
@include "tbl"

BEGIN { tests("tblok","_weather") }

function _weather(f,  t) { 
  Tbl(t)
  lines(t,"Tbl1","weather" DOT "csv")
  oo(t,"t")
}
