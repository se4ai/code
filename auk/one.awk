function List(i)         { split("",i,"") }
function zap(i,k)        { i[k][0]; split("",i[k],"")}
function has( i,k,f)     { f=f?f:"List"; zap(i,k); @f(i[k]) }
BEGIN { a["as"]; a["as"]["p"]=2; for(i in a) print a[i] }

