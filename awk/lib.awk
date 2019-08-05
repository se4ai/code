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
function Object(i)       { split("",i,""); i["oid"]=++OID }
function has2(i,k,f,m,n) { has(i,k); @f(i[k],m,n) }
function has1(i,k,f,m)   { has(i,k); @f(i[k],m) }
function has( i,k,f) { 
  f = f ? f : "Object"
  split("",i,"")
  @f(a[k]) 
}
