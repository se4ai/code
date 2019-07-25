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
  On the other hand:

- Explanations based over a   few bins is much simpler explain (since they contain fewer values);
- A search over a few bins can run much faster than a search over a large number of numbers;
- Discretized columns are easier to index

Note only is explanation over ranges, it also is more general (in the sense that it covers more examples).
That is, before discretization, users can expect rows
with point values like _loc=50_ and _experience=2years_. While that is interesting, it does not
tell the user how much they can safely change things without changing effects inside the data.
If the data is discretized, then they can inspect rows with bins like $$\mathcal{30\le loc \le 70}$$
and $$\mathcal{ 1 \le experience \le 3}$$. When reasoning about models
 built from such discretized ranges, it is easier to work out how much things can safely change, without
effecting  the overall results.


Hence, discretization is very useful. For example,
having discretized a time series, [NASA would watch its rockets](https://www.cs.ucr.edu/~eamonn/HOT%20SAX%20%20long-ver.pdf) looking for unusual sequences
of time steps. To that end they build a n-gram model that used the last n letters to predict
the n+1 letter. This can be displayed in a simple tree where the width of each branch shows how
often it is used (so fat branches are most frequent). Note that in the following, if ever we see _bcb_
then we can relax (cause that is normal operations) but if we see 
_aaa_ then we might get worried
(since that is something new and rare).


It is surprising how few discretized ranges are enough to capture domain semantics.

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
When finding the median, if sorting all the numbers is inconvenient, just keep a small random sample
of the numbers.

## Unsupervised Discretiztion

Discretization can be _unsupervised_ or _supervised_.
Unsupervised discretization
  just looks at each column by itself. 
Simple unsupervised clustering strategies include:

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

Another way to divide up numbers is to split column1 according to how much that changes column2. In this approach,
column2 is said to _supervise_ the splitting of columns1.

Traditionally, discretization is applied recursively just to divide a single
column of numbers. Here, we note that if the discretizer is allowed to swich attributes
at each level of dividing the data, then the "discretizer" becomes a tree learners.
The lesson here is that by the time you have a discretizer working, you are more than half
way to having a fully fledged learner.

One  discretization method, which we might call _ARGBEST_ 
finds split that most include some desired dependent variables. For example, 
suppose the we  want to find ways to maximize
some numeric class variable
 $$y_i$$. Consider a  split $$x_i$$  that divides a 
column into $n_1,n_2,n_3$ rows with mean $$y_i$$ scores of $$mu_1, mu_2, mu_3$$.
Let us say that $$n_0$$ denotes the split with worst $$mu$$$ value (which we will call $$\mu_0$$).
The best split would be the one with the most number of values greater than those in $$n_0$$. That is,
we would seek to maximize:
we would seek splits that maximize
$$n_1*\mu_1/\mu_0$$.


Another method, 
that we might call 
_ARGMIN, divides the data using the split that most reduces the _variety_
of the dependent column. Next, we add sub-trees by
recursing  into each division. That is, one way to build a model is just recursively apply discretization.
To implment _ARGMIN_ we need someway to measure variability variety
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
- However we measure variety, if a column splits $n$ rows into $$n_1,n_2,n_3..$$ rows, each of which
  has variety  $$V_1,V_2,V_3...$$ (where $$V_i$$ is either entropy or standard deviation),
  the expected value of  
  of the variety after the split is $$E[V]= \sum_i \frac{n_i}{n}V_i$$. 
     - For example, if a split on __age>100_ divides our data into 50 and 100 and 200 rows with standard
       deviations of 0.3 and 0.2 and 0.1 respectively, the $$E[V]]= \frac{50}{350}*0.3 + \frac{100}{350}*0.2 + \frac{200}{350}*0.1=0.18$$. 
- For _ARGMIN_  to work, it has to explore all possible splits of all numeric attributes. 
  To speed that up:
       - Implement some $$V$$ collector class that can incremetnally add (or subtract) values
         from the  standard deviation or entropy of a set of numbers..
       - To divide the column $$X$$ using some class column $$Y$$, then create pairs
         of $$(x1,y1),(x2,y2), etc)$$. 
       - Sort on $$x_i$$ then create two collectors $$V_0$$ and $$V_1$$.
         Initialize $$V_0$$ to be empty and $$V_1$$ to hold the variety of all $$y_i$$ values.
       - Working from min to max along that sorted list:  (a)take each $$y_i$$ and (b)add it to $$V_0$$ and
         (c) remove it from $$V_1$$. Now $$E[V]$$ for a split at the current position can be computed
         straight away from $$V_0,V_1$$. 
       - This approach requires only one sort and two pass of the data.

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


## Other Applications of Discretization

We said above that once a discretizer works, then we are more than
halfway to have a learning system.  Four  illustrations of this are
[STAR](REFS#menzies-2007), [FFTtrees](REFS#chen-2018),
[CART](REFS#brieman-1994) and [C4.5](REFS#quinlan-1996) discussed
in the next chapter.

Another applciation of "discretizaton" is actually a statistical
clustering method called the _Scott-Knot_ procedure. In this methods,
various _treatments_ are applied to collect a bag of score values
for each treatment. For example, a standard evalatuon rig in data
mining is an M-times-N cross validation where:

- $$M$$ times, the data is sorted randomly. This is top _order effects_ where the scores are
  artificially low or high due to some fortuitous (but unlikely) ordering of the input data[^example]
- Then, for each ordering, the data is divided into $$N$$ bins. Each bin $$1 \le b \le N$$
  is then set aside as a test set while a model is learned on the remaining $$N-1$$ bins.
- Assuming $$M=N=5$$ [^crossval],  then this will generate 25 scores per treatment.

The Scott-Knot procedure "discretizes" these treatments into sets of similar values as follows.
The thing to note here is that, with very few changes, this procedure is the same _ARGMIN_
discussed above.


[^example]: E.g. Consider a data set from a hospital where all the female patients are listed last.
In such a data set, attempting to learn risk factors for pregnancy using the first part of
the data will fail (since that part contains no female examples).

[^crossval]: The standard values are $$M=N=10$$ but the empirical evidence for the need for
so many cross-validations is not strong. Using $$M=N=5$$ reduces the over all number
of trainings by a factor of four (from 10\*10=100 to 5\*5=25) while still returning
a large enough sample to be statistically interesting.


Scott-Knot
sorts a list of $$l$$ treatments with $$ls$$ measurements by their median
score. It then
splits $$l$$ into sub-lists $$m,n$$ in order to maximize the expected value of
 differences  in the observed performances
before and after the splits. For example, we could sort $$\mathit{ls}=4$$ 
methods based on their median score,
then splits them into three sub-lists of of size $$\mathit{ms},\mathit{ns} \in \{(1,3), (2,2), (3,1)\}$$.
Scott-Knot would declare one of these divisions
to be _best_,  as follows.
For lists $$l,m,n$$ of size $$\mathit{ls},\mathit{ms},\mathit{ns}$$ where $$l=m\cup n$$, the "best" division maximizes 
the difference in the expected mean value
before and after the split: 

$$
E(\Delta)=\frac{ms}{ls}abs(m.\mu - l.\mu)^2 + \frac{ns}{ls}abs(n.\mu - l.\mu)^2
$$

Scott-Knot then checks if that
_best_ division is actually useful (using some statistical procedure[^stats].
To implement that check, Scott-Knot would
apply some statistical hypothesis test $H$ to check
if $$m,n$$ are significantly different. If so, Scott-Knot then recurs on each half of the ``best'' division.

[^stats]: Statistics are discussed later in this book.

For example, consider
$$l=5$$ treatments:

```python
        rx1 = [0.34, 0.49, 0.51, 0.6]
        rx2 = [0.6,  0.7,  0.8,  0.9]
        rx3 = [0.15, 0.25, 0.4,  0.35]
        rx4=  [0.6,  0.7,  0.8,  0.9]
        rx5=  [0.1,  0.2,  0.3,  0.4]
```
After sorting and splitting, Scott-Knott declares:

- Ranked #1 is rx5 with median= 0.25
- Ranked #1 is rx3 with median= 0.3
- Ranked #2 is rx1 with median= 0.5
- Ranked #3 is rx2 with median= 0.75
- Ranked #3 is rx4 with median= 0.75

Note that Scott-Knott found  little
difference between rx5 and rx3. Hence,
they have the same rank, even though their medians differ. This is to say that there is no
real difference in the performance of rx3 and rx5 (and, indeed, rx2 and rx4).
This is the essence of discretization-- ignoring trivial differerences and grouping together similar 
values into a few, easy to browser, sets.

