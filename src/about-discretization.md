# About Discretization


Recall that columns of numbers can be divided into a few _bins_ (a.k.a _ranges_) using _discretization_. 
Discretization converts a (potentially) infinite range of numbers to into a small set of systems. 
For example, here's a number ranges divided into 12 bins:

![](https://www.cradle-cfd.com/images/tec/column01/fig5.1.jpg)

Clustering can be along the x-axis (as above)
or (for time-series data) on the y-axis.

![](https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/5e810061f5bd8449e35fdd0b05a805a0e90a7b68/5-Figure2-1.png)

<img align=right width=400 src="img/ngram.png">
Discretizaton can lose some numeric nuances.
  On the other hand,  discretized columns are easier to index
as well as explain (since they contain fewer values)
Hence, discretization is very useful for reducing the complexity of the reasoning. For example,
having discretized a time series, [NASA would watch its rockets](https://www.cs.ucr.edu/~eamonn/HOT%20SAX%20%20long-ver.pdf) looking for unusual sequences
of time steps. To that end they build a n-gram model that used the last n letters to predict
the n+1 letter. This can be displayed in a simple tree where the width of each branch shows how
often it is used (so fat branches are most frequent). Note that in the following, if ever we see _bcb_
then we can relax (cause that is normal operations) but if we see 
_aaa_ then we might get worried
(since that is something new and rare).


Another good thing about discretized numerics is that they let us report our models
in terms of ranges, not point values. That is, before discretization, users can expect rows
with values like _loc=50_ and _experience=2years_. While that is interesting, it does not
tell the user how much they can safely change things without changing effects inside the data.
If the data is discretized, then they can inspect rows with values like $$\mathcal{30\le loc \le 70}$$
and $$\mathcal{ 1 \le experience \le 3}$$. When reasoning about models
 built from such discretized ranges, it is easier to work out how much things can safely change, without
effecting  the overall results.

Its surprising how few discretized ranges are enough to capture domain semantics.
- In software engineering, [Jaechang Nam and Sunghun Kim](REFS#nam-2015)
report that they can predict software defects
using data 
where all the numerics are divided into just two bins (above and below
the median value[^med]). While one such attribute may not be informative, when (say)
24 attributes are all above their median value, then you start being pretty sure 
that a defect is present.
- Another example of using just a few bins comes from _random projections_.
     - This is a clustering method that picks two points _X,Y_ at random, then computes the distances
from everything else to these two. 
     - Those distances are then discretized into 
into two bins: those nearest _X_  or those nearest _Y_. 
     - The data is then divided into
those two bins and the algorithm recurs into those divisions. 
     - Like in the  defect prediction
example, splitting on one random projection is not particularly informative.
But once you get a few levels deep in the tree of clusters, it become highly likely
that the things found together are actually very close together.
     - Random projections are hence a very useful way to very rapidly cluster a lot data.

[^med]: In statistics, the median,mean, and mode value of a distribution is the central,
average and most frequent common value, respectively. The mean of $$n$ numbers is $$i(\sum_in_i)/n$$.
To find the median, sort the numbers then find the middle value (or, if the list is
en even number of items long, report the average between the two middle values).
When finding the median, if sorting the numbers is inconvenient, just keep a small random sample
of the numbers.

## Unsupervised Discretiztion

Discretization can be _unsupervised_ or _supervised_.
Unsupervised discretization
  just looks at each column by itself. 
Simple simplest unsupervised clustering strategies include:

- When dividing, first sort the rows on the column you want to divide on. Then...
   - Divide on (say) $$\mathcal{(max-min)/10$$.
   - Or divide into bins of size $$\sqrt{N}$$ of the number of columns.
- When consider a division of a column into some range $$a .. b$$, ensure that $$b > a+ \epsilon$$
  where $$\epsilon$$ is some measure of ``too small to be interesting''. $$\epsilon$$ can be
  set via domain knowledge or using some simple heuristics like 
     - Find the 50-th and 64-th percentile in the sorted
       columns of numbers and let  $$\espilon=p_{64}-p_{50}$$ (this is a range equal to 1/7th of the
       numbers).
     - If you are happy to assume your numbers have a  bell-shaped curve[^warn]
       distribution,  then use Cohen's rule
        i.e. $$\epsilon=30\%*\sigma$$ where $$\sigma$$ is the standard deviation (defined below).
       The standard deviation of  a set of $$n$$ numbers is
$$\sigma(Y,n) = \sqrt\frac{\sum_i (Y_i-Y')^2}{n-1}$$ where $$Y'$$ is the mean value for $Y$. Standard deviation is minimal (zero)
when all the numbers are the same.
Cohen's rule has the advantage that it can be calcuated without sorting (via incremental
       calculation of the standard deviation)[^incsd]. 

[^warn]: Warning: many distributions do not conform to this shape.
[^incsd]: To incremental compute mean and standard deviation $$\mu,\sigma$$,
start with $$n=\mu=m=\sigma=0$$. As every new number $x$ arrives, $$n++$$ and $$d=x-\mu$$ and $$\mu += d/n$$
and m+=d*(x-\mu)$$ and, if $$n>1$$,  $$\sqrt{sigma=(m/(n - 1))}$.

## Supervised Discretization

Another way to divide up numbers is to consider how those divisions select for the goals or classes.
After dividing the data on that split, we can learn trees, where each level of the tree shows
the effect of one division.


Technical aside: traditionally, discretization is applied recursively just to divide a single
column of numbers. Here, we note that if the discretizer is allowed to swich attributes
at each level of dividing the data, then the "discretizer" becomes a tree learners.
The lesson here is that by the time you ahve a discretizer working, you are more than half
way to having a fully fledged learner.

A widely used method to learn a tree is,
that we will call 
_MIN_, divides the data using the split that most reduces the _variety_
of the dependent column. This split becomes a new node in the tree. Next, we add sub-trees by
recursing  into each division. That is, one way to build a model is just recursively apply discretization.
To implment _MIN_ we need someway to measure variability variety
(since  that is what we want
to minimize).


- If the dependent column is numeric, we measure _vareity_ using _standard deviation_ (defined above)
When the [CART](REFS#brieman-1984) learner is building a regression tree, it uses standard deviation.
(and a regression tree is a tree whose leaves predict for numeric variables).
- If the dependent column is symbolic, we measure _variety_  using _entropy_[^ent].
The entropy of $n$ symbols occuring at frequency $$f_1,f_2,..$$ etc
is $$=\sum_i p_i\log_2p_i$$ where $$p_i=f_i/n$$.
Entropy  is minimal (zero)
when all the symbols  are the same.
When CART or [C4.5](REFS#quinlan-1986) (also known as J48) is building a classification tree, it uses entropy.
- However we measure variability, if a column generates splits $n$ rows into $$n_1,n_2,n_3..$$ rows, each of which
  has variety  $$V_1,V_2,V_3...$$ (where $$V_i$$ is either entropy or standard deviation),
  the expected value of  
  of thevariety after the split is $$E[V]= \sum_i \frac{n_i}{n}V_i$$. 
- For _MIN_ to work, it has to explore all possible splits of all numeric attributes. 
  To speed that up:
       - Implement some $$V$$ collector class that can incremetnally add (or subtract) values
         from a standard deviation or entropy calculation.
       - To divide the column $$X$$ using some class column $$Y$$, then create pairs
         of $$(x1,y1),(x2,y2), etc)$$. 
       - Sort on $$X$$ then create two collections $$V_0$$ and $$V_1$$.
         Initialize $$V_0$$ to be empty and $$V_1$$ to hold the variety of all $$y_i$$ values.
       - Working from min to max along that list take each $$y_i$$ and add it to $$V_0$$ and
         remove it from $$V_1$$. Now $$E[V]$$ for a split at the current position can be computed
         straight away from $$V_0,V_1$$.

[^ent]: According to [Wikiquotes](REFS#entropy-1949)
this expression was named as follows.
In 1949, Claude Shannon
visited the mathematician John von
Neumann, who asked him how he was getting on with his theory of
missing information. Shannon replied that the theory was in excellent
shape, except that he needed a good name for "missing information".
"Why don’t you call it entropy", von Neumann suggested. "In the
first place, a mathematical development very much like yours already
exists in Boltzmann’s statistical mechanics, and in the second
place, no one understands entropy very well, so in any discussion
you will be in a position of advantage."

Another  discretization method, which we call _MOST_,
is to find split that most include some desired dependent variables. For example, 
suppose we want to find ways to maximize
some numeric class variable
 $$y_i$$. Consider a  split $$x_i$$ 
the column into $n_1,n_2$ rows hold all rows with values larger that $$x_i$$ or otherwise.
Those two splits would 
hold $$Y$ scores in the two bins of $$\mu_1, \mn_2$$
The best split contains the most $y_i$ values
that are greater than in the other split. That is,
we would seek splits that maximize
$$n_1*\mu_1/\mu_2$$.

power pruning b^2/(b+r)

active elarning

goal custering

fft trees

https://en.wikipedia.org/wiki/Logistic_regression#/media/File:Exam_pass_logistic_curve.jpeg
w

Amazing how few you need. median chops

Sctott knott is a deicretizer

LSH is a discretizer

ARGMOST


For more on discretizatin, see after
applying some unsupervised discritizer, find 

, used in learners in FFtrees
 it would
be ts indepednent and depednet columns,
 
 columns
values to car about) but you can sometimes lose some of the numeric nuances.


