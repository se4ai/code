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
and their standard deviation `sd` (which is a measure of the diversity of a set of numbers[^sddef])


[^sddef]: $$\sigma(Y,n) = \sqrt\frac{\sum_i (Y_i-Y')^2}{n-1}$$ where $$Y'$$ is the mean value for $Y$. Standard deviation is minimal (zero)
when all the numbers are the same.

In the `Sym`bolic summary, we see counts of how many `n` numbers were seen, their most common value (denoted`mode`),
and theor entropy `ent` (which is a measure of the diversity of a set of symbols[^entdef])

[^sddef]: The entropy of $n$ symbols occuring at frequency $$f_1,f_2,..$$ etc
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
- $$p=2$$ makes this the Euclidean distance; 
- dividing by the root of the number of features makes this range from 0 to 1

[^trick1]: Sometimes $f$ can be the dependent variables. In two-tiered
clustering you might cluster first by the dependent variables, and
then by the independent variables.  Since the number of dependents
is typically much less than the independents, this can run very
fast.

 or independent 
In the latter case, we also have 
   <X,Y>

wererun over data of the form


The simplest (and sometimes slowest) learner is a cluster.
Clsuters ignore any class or goal variables

curritng is implortant:

- range cuts, column cutts (feature selection)
contrast sets (avoding dullr egions)

### naive bayes group and the class and loomfor dfferente ebween theing
XXX decision trees cut on the class
cover and differentiate make a decision the spin hthru the rest
## Quiz

# given standard deviation forumla, derive sd
# given entropy  forumla, derive e
# distance between two rows
# derive the cosine rule
