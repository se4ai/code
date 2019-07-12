---
layout: abc
title: About Data Miners
---

https://link-springer-com.prox.lib.ncsu.edu/chapter/10.1007/978-3-642-45135-5\_3

## Summary

- Supervised learners  seek combiantions of indepdnent features that predict for depednent features.
- Classifiers  predict for a single symbolic goal called the class.
- Regression predict for a single numeric  goal.
- Assoication rule learners called the class.


## About Data Miners

Many data miners learn models of the form

$$
Y = f(X)
$$

where $$X$$ are the indepedent variabes and $$Y$$ are the depedent variables.



When all the data is numeric and conforms to a simple distribution, then simple 
mathematcs is enough to learn $$f$$. 
But when data is a mixture of symbols and numbers, then we need to beyond standard
maths. This is particularly true foridata extracted from software
since every `if` statement divides 
a program  into a different region needing its own $$f$$.


### Tree learning

Many data mining methods generating trees. For example, decision trees are those
These are trees
where:

- leaves are classifications (some decision about a 
  symbolic goal)
- and whose branches are conjunctions of features that lead to those classifications. 

_Regression trees_  are similar but their leaves 
make a prediction about some numeric goal.

One way to learn a tree is to:

- split the example set into
subsets based on some attribute value test. 
- The process then repeats
recursively on the subsets, with each splitter value becoming a
subtree root.  
- Splitting stops when a subset gets so small that
further splitting is superfluous or a subset contains examples with
a very clear single outcome.

#### "_argbest&nbsp;goal_"

One scheme for finding good splits is
to find splits to select for 
best values of the goal variables. For example:

-  a _best or rest_
strategy is to divide the depedent  values into (say) the 10%
best and the 90% rest
-  then find  indendent ranges that select
for that best range.

#### "_argmin&nbsp;diversity_"

Another scheme for finding good splits is 
$$\underset{\mathcal{diversity}}{\operatorname{argmax}} $$:

- A good split decreases the percentage of different symbols
  or different numbers
  in a subset, ensuring that subsequent learning generates smaller
  subtrees by requiring less further splitting to sort out the subsets.
- The diversity of the examples within each split can be measured 
  via standard deviation, or entropy.
- Given examples with numeric goals $$x_1, x_2,..$$, 
  their standard devation is  
  $$\sigma=\sqrt{\frac{1}{N-1} \sum_{i=1}^N (x_i - \overline{x})^2}$$
  where $$\overline{x}$$ is the mean of these values;
  i.e. $$\overline{x} = \frac{\sum_ix_i}{n}$$.
- Given $$n$$ examples with symbolic goals at frequency $$n_1, n_2,...$$,
  the probability of those symbols are $$p_i=\frac{n_i}{n}$$ and
  their entropy is $$e=-\sum_ip_ilog_2(p_i)$$.

Sometimes standard deviation is described as _variance_.
These two quanitites are related as follows: standard deviation
is the square root of the variance.
Note that all these values (entropy, standard deviation, and variance)
are minimal when there is least diversity in the sample.

To illustrate this kind of splitting, suppose we were considering
spliting the data on _lines of code_. If we split at _loc&lt;100_
then that would produce two splits of very similar _efforts_: 

- _(10,10,9,15)_ which has a standard deviation of $$\sigma_1=2.3$$
- and _(88,92,98)_ which has a standard deviation of $$\sigma_2=4.1$$
- The expected value of these two values is sum of these numbers
  divided by their frequency; i.e. 
  $$\frac{n_1}{n}\sigma_1 + \frac{n_2}{n}\sigma_2$$ 
  which equals
  $$\frac{4}{7}{\times}2.3 + \frac{3}{7}{\times}4.1=3.1$$. 
- 3.1 is  much less than the
  than the
  $$\sigma_0$$ of all the effort numbers of 40.5; i.e. _loc&lt;100_
  is a very good split.

$$
\begin{array}{rr}
\mathcal{lines~of~code}& \mathcal{effort} \\\hline
       10              & 10 \\
       11              & 10 \\
       13              & 9 \\
       20              & 15 \\
      100              & 88\\
      110              & 92\\
      130              & 98\\\hline
      \mathcal{stdev}=\sigma_0 = & 40.5
\end{array}
$$

### Clustering

$$(\sum_i(x_i - y_i)^p)^{1/p}$$

### Association rule learning

Association rule learners such as [Apriori](/refs#Agrawal93) find
attributes commonly occurring together in a training set. 
Rules have the form

$$
\mathcal{LHS} \Rightarrow \mathcal{RHS}
$$

where $$\mathcal{LHS}$$ and


No attribute
can appear on both sides of the association LHS × RHS—that is, LHS
× RHS = ∅.  The rule LHS × RHS holds in the exam- ple set with
confidence c if c percent of the examples containing LHS also contain
RHS: c = |LHS ∪ RHS| × 100/|LHS|. The rule LHS × RHS has support s
in the exam- ple set if s percent of the examples contain LHS ∪
RHS: s = |LHS ∪ RHS| × 100/|D|, where |D| is the number of examples.
Associ- ation rule learners return rules with high confidence (for
example, c > 90 percent).  Rejecting associations with low sup-
port first can cull the search for associations. We can view
association rule learners as generalizations of decision tree
learning: Decision tree learners restrict the RHS of rules to one
class attribute whereas association rule learners can add any number
of attributes to the RHS.

e examples have 

This part introduces some terminology that we'll need as we go along.

no way s the following a complete list of methods. kust those we can review quicikly


some dvision tactic:

use the class

use mxitures 


use intra-independtn dimension space (Calustering)

aprior grows small to big


incude here the dm survey from duo

and the survey from data mining for bisy people'


Clustering groups together related data

```python
### meta data about rows
def indep(row) : return row's' independent columns 
def isNum(col) : return true if col holds numerics
def hi(n)      : returns max number in column n
def lo(n)      : returns min number in column n

### routines
def any(lst,n=1): return any n items in lst. repeats are allwoed. 
```

```python
def dist(row1,row2,,P=2):
  "distance between rows one and two"
  n=0
  for col in indep():
    n  += 1
    x,y = row1[col], row2[col]
    d  += dist1(x,y,col)^P
  return (d/n)^(1/P)

def dist1(x,y,col)
  if x=="?" and y=="?": return 1
  elif isNum(col): return numDist(x,y) 
  else           : return symDist(x,y)

def symDist(x,y, n):
  "identical symbols have distance 0"
  return 0 if x==y else 1

def numDist(x,y,n):
  "if x,y unknown, make a guess that maximizes distance"
  if x=="?":
     y = norm(y,n)
     x = 0 if y > 0.5 else 1
  elif y=="?":
     x = norm(x,n)
     y = 0 if x > 0.5 else 1
  else:
     x,y = norm(x), norm(y)  
  return x-y

def norm(z,n) : return (z - lo(n)) / (hi(n) - lo(n) + 10^-32)
```
```python
def lt(x,y): return x < y
def gt(x,y): return x > y

def closest(row1,rows, best=1, better=lt):
  for row2 in rows:
    if id(row2) != id(row1):
      tmp = dist(row1,row2)
      if better(tmp,best):
         best, out = tmp,row2
  return out

def furthest(row1,rows):
  return closest(row1,rows,best=0, better=gt)
```

```python
class item:
  def __add__(i,x):
    if x != "?": i.add(x)
    return x

class sym(item):
  def __init__(i,c): i.col,i.most,i.mode,i.bag = c,0,nil,{}
  def expect(i)    : return i.mode
  def add(i,x)     :
     n = i.bag[x] = i.bag.get(x,0) + 1
     if n > most:
       most,mode=n,x

class num(item):
  def __init__(i,col): 
    i.n,i.mu,i.sd,i.m2, i.col = 0,0,0,0,col
    i.lo,i.hi = math.inf, -1*math.inf
  def expect(i): return i.mu
  def add(i,x): 
    d = x - i.mu
    i.mu += d/i.n
    i.m2 += d*(x - i.mu)
    i.sd  = (i.m2/(i.n - 1 + 10^-32))^0.5
    if x < i.lo: i.lo = x
    if x > i.hi: i.hi = x

class cluster:
  def __init__(i,row):
    i.has, i.items, i.centroid = [],[], copy(row)
    i.reset(i.centroid)
  def __add__(i,row):
    i.has += [row]
    for item,x in zip(i.items,row): 
      item + x
  def centralize(i):
    for item in i.items: 
      i.centroid[item.col] = item.expect()
    i.reset()
  def reset(i,row):
    i.has = [row]
    i.items = [(num(col) if isNum(col) else sym(col)) 
              for col in len(row)]

class rows:
    named = {}
  now   = None

  @staticmethod
  def switch(x):
    assert x in names, '%s not named' % x
    now = data.names[x]
    return now

  def __init__(i, name=None, indeps=[], nums=[], headers=[],
                  klass=None, less=[],more=[]):
     i.name= name
     if name: 
        data.named[name]= i
     i.indeps,i.nums,i.names = indeps,nums,names
     i.klass, i.less,i.more  = klass, less,more
     i.syms,i.items,i.dep = [],[],[]
     i.all=[]
   def clone(i):
     return data(indeps=i.indeps,   nums=i.nums, 
                 headers=i.headers, klass=i.klass, 
		 less=i.less,       more=i.more)
   def __add__(i,row):
     if not i.all
       decideThingsAboutData(row.i.headers)
       i.items = i.items0()
     i.all  += [row]
     for item,val in zip(i.items,row):
       item + val
   def items0(i):
     item = lambda j: num(j) if j in i.nums else sym(j)
     lst  = [item(j) for j in i.dep]
     lst += [item(j) for j in i.indep]
     return sorted(lst, key=lambda z: z.col)

def decideThingsAboutData(i,row,headers=None):
  less  = "<"
  more  = ">"
  klass = "!"
  num   = "$"
  intfloat = lambda j: isinstance(row[j],(int,float))
   n = len(row)
   if headers:
      lessp    = lambda j: headers[j][0]== less
      morep    = lambda j: headers[j][0]== more
      klassp   = lambda j: headers[j][0]= klass
      depp     = lambda j: lessp(j) or morep(j) or klassp(j)
      nump     = lambda j: headers[j][0]= num
      i.nums = i.nums or [j for j in range(n) if nump(txt)]
      i.less = i.less or [j for j in range(n) if lessp(txt)]
      i.more = i.more or [j for j in range(n) if morep(txt)]
      for j in range(n): 
        if klassp(j): i.klass=j
   i.klass = i.klass or n-1
   i.nums  = i.nums  or [j for j in range(n) if intFloat(j)] 
   i.syms  = i.syms  or [j for j in range(n) if not j in i.nums]
   i.dep   = i.dep   or [j for j in range(n-1) if depp(j) ]
   i.indep = i.indep or [j for j in range(n-1) if j not in i.dep]
 
 def kmeans(rows,K=10,P=2):
  clusters  = [cluster(row) for row in any(rows,K)]
  centroids = [cluster.centroid for cluster in clusters]  
  for row in rows:
    k = closest(row,centroids)
    clusters[k] + [row]
  

```python
# data is some source that returns rows in random order
def mioniBatchKMeans(data,K=10,T=100,M=1000):
  v={}
  n={}
  for k in range(K): 
     centroids[k] = data.next()
     n[k] = 0 
  for _ in range(T)
    cache={}
    some = []
    for _ in range(M):
      one = rows.next() or return centroids
      some += one
    for row in some:
      cache[ id(row) ] = closest(row, centroids)
    for row in some:
      range(M):
      

      row:
    k = closest(row, centroids)
    n[k]++
    
    for c in centroid 

  c[i] = row
k clusters C = {c1, c2, c3, ......ck}

initialize k cluster centers O = {o1, o2, .......ok}
# _initialize each cluster
Ci = Φ (1=< i =< k)
# _initialize no. of data in each cluster
Nci = 0 (1=< i =< k)

for j=1 to t do:
    # M is the batch dataset and xm
    # is the sample randomly chosen from D
    M = {xm | 1 =< m =< b}

    # catch cluster center for each
    # sample in the batch data set
    for m=1 to b do:
        oi(xm) = sum(xm)/|c|i (xm ε M and xm ε ci)
    end for
    # update the cluster center with each batch set

     for m=1 to b do:
        # get the cluster center for xm
        oi = oi(xm)
        # update number of data for each cluster center
        Nci = Nci + 1
        #calculate learning rate for each cluster center
        lr=1/Nci
        # take gradient step to update cluster center
        oi = (1-lr)oi + lr*xm
     end for
end for

