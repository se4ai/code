# About Learners

Learners divide old data  into (say):

- things that are similar or different (this is called
  clustering)
- things you care about 
- things you don't 
- things you want to avoid.

They then can look at new data to learn if
what kind of thing it is.


Optimizers change things. That is, once you have learned
that you like X and do not like Y, then an optimizer
could suggest "do X - Y". Optimizers are discussed later.

The goal of this chapter is to offer certain core intuitions, common features,
about learners. It is not a comprehensive guide (for that, see [the excellent Ian Witten book]
on data mining](REFS#witten-2016)
 but it does introduce much of the learning technology used
later in this book.

----

## Columns and Rows

Learners process examples  (also called rows)
of the form
$$(X,Y)$$ were:

- $$X$$ are one or more independent variables (a.k.a. inputs)
- $$Y$$ are the dependent variables we want to achieve
  (a.k.a. outputs).

Note that variables are also called features, attributes,
or columns.
The outputs
can be:

- one  class that may be symbolic
  (e.g. defective=True or False) or numeric (e.g. development
  effort).
- one or more numeric goals that divide into things
  we love/hate that we want to minimize/maximize (respectively);
  e.g. amount of reused code or number of bugs.

A set of rows is sometimes called a table, or a relation. In such sets, we
often keep statistics on each column. 
If `n,s` are instances of class `Num,Sym` then `n+x, s+x`
are methods that add `x` to the summary. For example

```python
n = Num()
for x in [1,2,3,4]: n+x
print(n, n.sd)

# ==> {'n': 4, 'mu': 2.5, 'lo': 1, 'hi': 4}
# ==> sd = 1.29

#-----------
s = Sym()
for x in 'abbcccc': s+x
print(s,s.mode, s.ent)

==> Sym{bag={'a': 1, 'b': 2, 'c': 4}, n=7} c 1.38
==> mode = 'c'
==> ent = 1.38
```
In the `Num`eric summaries, we see counts of how many `n` numbers seen, their minimum and maximum values (denoted `lo,hi`), 
and their standard deviation `sd` which is a measure of the diversity of a set of numbers.
The standard deviation of  a set of $$n$$ numbers is
$$\sigma(Y,n) = \sqrt\frac{\sum_i (Y_i-Y')^2}{n-1}$$ where $$Y'$$ is the mean value for $Y$. Standard deviation is minimal (zero)
when all the numbers are the same.

In the `Sym`bolic summary, we see counts of how many `n` numbers were seen, their most common value (denoted`mode`),
and their entropy `ent` (which is a measure of the diversity of a set of symbols.
The entropy of $n$ symbols occuring at frequency $$f_1,f_2,..$$ etc
is $$=\sum_i p_i\log_2p_i$$ where $$p_i=f_i/n$$.
Entropy  is minimal (zero)
when all the symbols  are the same.

Supervised learners learn a model $$f$$ of the form $$Y=f(X)$$.
Unsupervised learners ignore the dependent variable
and group together  similar rows, based on their $$X$$ values.
For that grouping, some distance function is required. A
standard distance function between rows $$a,b$$ with $$f$$ 
features

$$
\mathcal{dist}(a,b,f,r,p=2) = \left(\frac{1}{\sqrt{|f|}}\right)\left(\sum_{i\in f} \mathcal{diff}(r,i,a_i,b_i)^p\right)^{1/p}
$$

where:

- $$r$$ is the set of all rows;
- $$f$$ are the features we are considering  (usually the independent variables[^trick1])
- $$p=2$$ makes this the Euclidean distance (but it is worthy exploring other values); 
- dividing by the root of the number of features makes this range from 0 to 1

[^trick1]: Sometimes $f$ can be the dependent variables. In two-tiered
clustering you might cluster first by the dependent variables, and
then by the independent variables.  Since the number of dependents
is typically much less than the independents, this can run very
fast.

In the _dist_ equation, the _diff_ function for symbolic and numberic columns. For numbers, a usual _diff_ has the range $$0..1$$ and
is calulated as follows:

$$\mathcal{diff}(r,i,a_i,b_i) = (r.col[i].norm(a_i) = r.col[i].b_i)^p$$

where $$r.col.norm(x)$$ is a function that normalises $$x$$ to the range $$0..1$$ using $$\frac{x-lo}{hi - lo + 0.0000001}$$
(i.e. using the smallest and largest value seen in column $$i$$) and                                          $$0.0000001$$
is a small constant added to the denominator to avoid divide-by-zero errors. 

For symbols, a usual $$diff$$ is 

$$\mathcal{diff}(r,i,a_i,b_i) = 0\; \mathcal{if}\;a_i==b_i\;\mathcall{else} 1$$

If either of $$a_i,b_i$$ are unknown values then _diff_ returns the maximal possible difference. 

- For symbols, that maximum value is 1
- For numbers, if one value $x$ is known then it is normalized to $x'$ and the distance is set to the maximum possible value; i.e.

$$ (1-x')\; \mathcal{if}\; x'> 0.5\; \mathcal{else}\; x'$$

- And, for numbers if both values are unknwon, then _diff_ returns 1.
 
### Clustering

The simplest (and sometimes slowest) learner is a clusterer.
Clustering ignores any class or goal variables and group together similar rows using some distance function.
Clustering can be slow since, if implemented naively, it requires multiple $$O(N^2)$$ comparison between all rows.
The famous K-means algorithm reduces that to $$O(kN)$$ as follows:

1. Declare that  $$K$$ rows (picked at random) are the _centroids_;
2. Marks each example with the id of its nearest centroid;
3. Finds the central point of all the rows marked with the same centroid.
4. Declares those new central points to be the new centroids
5. Goto 1

It is insightful to think of K-means as an example of _expectiation minimization_ algorithms.
Such algorithms make guesses, then change something to minimize the errors associated with those gusess (in this case, move the centroids).

[Mini-batch K-means](REFS#sculley-2015) is a more memory efficient  version of K-means.
This variant never loads all the examples into main memory. Instead, it only loads _batches_ of rows of size  $$B$$. 
The first $$k$$ rows seen become the first $$k$$ centroids. Rows arrive after that (in the same batch) add themselves to a cluster assocated with the nearest
centroid. When the batch is done, each cluster adjust its centroids by reflecting over each row in the centroid:

- For the first row, the centroid moves itself half way towards the row; 
- For the second row, the centroid moves itself one-third of the way  towards the row; 
- And so on such that for the nth row, the centroid moves itself $$1/(n+1)$$th  the way  towards the row; 

The next batch of $$B$$ rows is read and the process repeats.

An even more effecient clustering algorithm uses random projections. The above clustering algorithms 
are very sensitive to quirks in the distance function. One way to mitigate for those quirks
is sort out the rows using multiple, randomly generated distance measures. Sure, a few may be less-than-perfect
but the more often a random project says two rows are similar, then the more likely they are actually are similar.

Here is FASTTREE random projection clustering.

1. Let $$M,P=32,10$$ (say)
2. Read the data. While  you have less  than $2M$ rows, add the rows into a local data cache.
3. If you have more than  $2M$$ rows, then divide:
    - $$P$$ times; pick any two rows $$x,y$$ in the batch and find the distance between them.
    - Pick the pair $$x,y$$ with maximum distance. This will be the projection used to divide the data.
    - Divide the according to whether or not they are closer to $$x$$ or $$y$$.
    - For each division, goto 2

There are many  interesting ways to modify  FASTREE. An _anomaly detector_ could report if the newly
arriving data is anything like what has been seend before (if so, we can ignore it since it does not add anything
to the model). For example,  in step2, as new data arrives, its distance could be compared to (say) $M$ other things already in the cluster.
If that is less than the $$Y$$ times the median value of all the distances previously seen in the cluster, the new example is boring and might be ignore
(For this approach, [Fayola Peters](REFS#peters-2015) suggests $Y=1$).
In step2, once $$M$$ examples have been read  a classifier/regression algorithm could be executed on the examples in that cluster and executed on any newly arriving examples.


Of all the above algorithms, standard K-means might produce the best clusters (since it is always reasoning over all the data). On the other hand,
the other variants might scale to larger data sets. 

There any many other ways to cluster data. For a more complete survey, see any textbook on data mining or [some of the excellent on-line tutorials](https://scikit-learn.org/stable/modules/clustering.html).


- range cuts, column cutts (feature selection)
contrast sets (avoding dullr egions)

### naive bayes group and the class and loomfor dfferente ebween theing
XXX decision trees cut on the class
cover and differentiate make a decision the spin hthru the rest

## Divide nums (discreitzation)


## Quiz

# u dont nroamlize what happens?
# given standard deviation forumla, derive sd
# given entropy  forumla, derive e
# distance between two rows
# derive the cosine rule
