#!/usr/bin/env ./auk
# vim: nospell filetype=awk ts=2 sw=2 sts=2  et :
#--------- --------- --------- --------- --------- ---------

@include "lauk"
@include "tbl"

BEGIN { tests("colok","_weather") }

function _weather(f,  n,i) { 
  Num(n,"c","v")
  for(i=1;i<=100;i++) Num1(n,i)
  oo(n,"t")
}
