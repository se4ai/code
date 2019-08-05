#!/usr/bin/env ./auk
# vim: nospell filetype=awk ts=2 sw=2 sts=2  et :

# ---------------------------------
# misc

BEGIN{  DOT=sprintf("%c",46)}

function trim(s) {
  gsub(/^[ \t]*/,"",s)
  gsub(/[ \t]*$/,"",s)
  return s
}
function lines(i,update,f,sep,  r,line,lst,com) {
  f = f ? f : "/dev/stdin"
  sep=sep ? sep : "[ \t]*,[ \t]*"
  com = "#"DOT"*"
  while((getline line < f) > 0) {
    sub(com,"",line)
    line=trim(line)
    if (line) {
      split(line,lst,sep)
      @update(i,++r,lst) }
  }
  close(f)
} 
function oo(x,p,pre, i,txt) {
  txt = pre ? pre : (p DOT)
  for(i in x)  {
    if (isarray(x[i]))   {
      print(txt i"=" )
      oo(x[i],"","|  " pre)
    } else
      print(txt i (x[i]==""?"": "=(" x[i] ")"))
}}

# ---------------------------------
# testing
function rogues(    s) {
  for(s in SYMTAB) if (s ~ /^[A-Z][a-z]/) print "Global " s
  for(s in SYMTAB) if (s ~ /^[_a-z]/    ) print "Rogue: " s
}

function tests(what, all,   one,a,i,n) {
  n = split(all,a,",")
  print "\n#--- " what " -----------------------"
  for(i=1;i<=n;i++) { one = a[i]; @one(one) }
  rogues()
}

function is(f,got,want) {
  if (want == got) 
    print "#TEST:\tPASSED\t" f "\t" want "\t" got 
  else 
    print "#TEST:\tFAILED\t" f "\t" want "\t" got 
}

# ---------------------------------
# object constructors
function zap(i,k)        { i[k][0]; split("",i[k],"")} 

function List(i)         { split("",i,"") }
function Object(i)       { List(i); i["oid"]=++OID }

function has( i,k,f)     { f=f?f:"List"; zap(i,k); @f(i[k]) }
function has1(i,k,f,m)   {               zap(i,k); @f(i[k],m) }
function has2(i,k,f,m,n) {               zap(i,k); @f(i[k],m,n) }

