#!/usr/bin/env ./auk
# vim: nospell filetype=awk ts=2 sw=2 sts=2  et :
#--------- --------- --------- --------- --------- ---------

@include "lauk"

function Config(i) {
   i.row.doms=100
}

BEGIN {Config(THE)}
