BEGIN{  DOT=sprintf("%c",46)}
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
function List(i)         { split("",i,"") }
function Object(i)       { List(i); i["oid"]=++OID }
function has2(i,k,f,m,n) { has(i,k); @f(i[k],m,n) }
function has1(i,k,f,m)   { has(i,k); @f(i[k],m) }
function has( i,k,f) { 
  f = f ? f : "List"
  i[k][SUBSEP]
  split("",i[k],"")
  @f(i[k])
}
function oo(x,p, pre) {
  for(i in x)  {
    if (isarray(x[i]))   {
      print(pre p"["i"]=" )
      oo(x[i],p,"|  " pre)
    } else
      print(pre p"["i"]=" x[i])
}}
