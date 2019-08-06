  /^@include/              { print "CODE "$0; next }
  /^(func|BEGIN|END).*}$/  { print "CODE "$0; next }
  /^(func|BEGIN|END)/,/^}/ { print "CODE "$0; next }
                           { print "DOC " $0}
 
