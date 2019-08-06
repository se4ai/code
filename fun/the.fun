#!/usr/bin/env ./fun
# vim: nospell filetype=awk ts=2 sw=2 sts=2  et :
#--------- --------- --------- --------- --------- ---------

@include "funny"

function Config(i) {
   i.row.doms=64
}

BEGIN {Config(THE)}
