cat - | sed 's/,/ ,/g' | column -t -s, | sed 's/ [0-9]/,&/g' | sed 's/^[ ]*//'
