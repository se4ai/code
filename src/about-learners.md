# About Learners

Learners divide old data  into (say):

- things that are similar or different (this is sometimes called clustering)
- things you can recognize, or score (this is called classification or regression)
- things you want to avoid or use (this is called optimization)

Then, when new data arrives, we can:

- work where to put it (which cluster)
- or what it is (using classification or regression) 
- or how to change it (using optimization)

For now, we focus on clustering, data mining, and regression. Later we will talk about optimization (but as we shall see, data mining and optimization are connected in that either one can help the other).

The goal of this chapter is to offer certain core intuitions, common features,
about learners. It is not a comprehensive guide (for that, see [the excellent Ian Witten book]
on data mining](REFS#witten-2016)
 but it does introduce much of the learning technology used
later in this book.

## But which learner is best?

## Data Miners work on Data

1. Tables have rows and columns of data. 
      - When data does not come in a nice neat table[^usually], then the
  first task of the data scientist is to wrangle the data into such a format. 
      - Later in this book, we devote three chapters to that wrangling (when we talk about data collection, data cleaning, and data labelling).
1. Columns are also sometimes called features, attributes, or variables.
1. Columns can be numeric or symbolic. 
     - Numbers can be added together. 
     - Symbols can only be compared using _equals_ and _not equals_.
1. Some columns might be _goals_ (things we want to minimize or maximize) 
   or _classes_ (which we want to predict).  
     - Goals and classes are sometimes called the _dependent_ variables. 
     - Goals are always numeric columns and the others can be symbolic or numeric.
     - Classifiers predict for symbolic goals (e.g _car=ford_ or _disease=measles_).
     - Regression algorithms predict for numeric goals (e.g. the time to failure of a hard drive).
- Columns that are not dependent are _independent_.

[^usually]: Which is, in fact, the usual case.

## Operations on data

### Discretization

Columns of numbers can be divided into a few ranges using _discretization_. 
For example, here's a number ranges divided into 12 bins:

![](https://www.cradle-cfd.com/images/tec/column01/fig5.1.jpg)


- Discretization converts a (potentially) infinite range of numbers to into a small set of systems. 

Discretization is usually applied just to one column, or a pair of columns. 
     -  In _supervised discretization_, we break up one column according to how much those breaks divide some goal column.
     -  For example, consider a table of data about
every Australian born since 1788. If that table has independent and dependent  columns _age_ and _alive?_,
then it is
tempting to split _age_ at least at 120 since above that point, everyone is _alive?=no_.


- As we shall see, we can also "discretize" more that just columns (and multi-dimensional "discretization" is called _clustering_).


### Clustering

Clusters  divide the table  into groups of similar rows (and each group is a cluster). Usually, 
  clustering  ignores the goal/class columns (but it is possible and sometimes useful to cluster on the  goals/class).


If  new thing is not similar to any existing cluster, then it is _anomaly_. 

- Once we have enough data in a cluster, we can can save space/time by  ignoring anything that isn't an anomaly (since we have already seen it before).
- Once we have too many new anomalies, it is time to recurs and form sub-clusters (so that we can work out the structure of the anomalies).
- In this way, one way to track anomalies is to track when  new clusters start forming.

Note that Recursive clustering lets us divide large problems into smaller ones.

If we only build models for the smaller clusters, then [model construction is much faster](https://arxiv.org/pdf/1802.05319.pdf).


### Model Building


There are many ways to build models, most of which involve [dividing the data](https://i.stack.imgur.com/v4IfD.png).

- Usually the divisions are pre-computed and cached (and those divisions are called the _model_). 
- But _lazy learners_
        work out the divisions at runtime on a case-by-case basis (e.g. nearest neighbor methods that use a division
        consisting of $$k$$ nearest neighbors). Note that lazy learners can be much slower than otherwise since nothing is
        pre-computed and cached from training time (so all the 
        work hapens at test time).

Different learners divide the data in different ways. For example: 

- Some learners divide the data using straight lines, parallel to the data axis (e.g. Decision trees)
      - E.g. continuing the above example, if the features are _age_ and _weight_ and _alive?_
        then the region _age &lt; 120_ has a border that is a line orthogonal to the _age_ axis and
        parrallel to the _weight_ access.
- While others
       allow curved boundaries  (_neural networks, support vector machines_).
- _Naive Bayes_ classifiers divide the data on the class value, then keeps summaries on the values seen in each division.
       When new data arrives, we check how similar it is to the summaries fron each class (and the new data is assigned the
       class that it is most similar).
    - For example, if all elephants are big and all snails are small, then if a new thing arrives that is big,
      we will guess that it is an elephant.
- <img align=right width=300 src="https://en.wikipedia.org/wiki/Logistic_regression#/media/File:Exam_pass_logistic_curve.jpeg">Logistic regression sorts data according to [an S-shaped curve](https://www.wolframalpha.com/input/?i=1%2F(1%2Be%5E(-x))+from+-10+to+10) ranging from $$0 \le y \le 1$$.  On that slope, we strongly
       believe in $$\neg x$$ or $$x$$ at $$y=0,1$$ (respectively)
     - For example, suppose we have learned that students pass exams at the range of _x=1.5\*hoursStudies-4_
     - The curve $$y=1/(1+e^{-x}$$ is shown at right.
 - Support vector machines invent new dimensions that let us  [better separate the data](https://pubs.rsc.org/image/article/2018/MO/c8mo00111a/c8mo00111a-f5_hi-res.gif). To do this, they use a _kernel function_ and different kernels invent
       different dimensions (e.g. here's [one that uses](http://omega.albany.edu:8008/machine-learning-dir/notes-dir/ker1/phiplot.gif)  $$\sqrt{2}x_1x_2}$$). Note that  some kernels are
       are [most suited to the current data](https://images.squarespace-cdn.com/content/54856bade4b0c4cdfb17e3c0/1418555379610-JJN6XJ9SG8TEABIB55R1/?content-type=image%2Fpng).
- Tree learners divide the data using a _split_ most reduces the _variety_ of stuff in each split. As discussed below, variety can be measured using _entropy_ (for discrete values) or _standard deviation_ (for numeric values);
- Random forests build (say) 100 decision trees, each time  using (say) $$\log_2$$ of the
  attributes (picked at random) and some random subset of the rows (i.e. not more than can fit  into main memory).
 - Ensemble learners randomly divide the data, build one model per division, then make conclusions by voting across
  the ensemble.

### Uncertainty

The less things divide, or the more than fall into the gaps between the divisions, the more we doubt those conclusions.
  For example:

- In a random forest, if all the trees offer the same conclusion, then might strongly believe that conclusion.
     - But if half the forest says _X_ and the other half says _Y_, then we are less certain of the conclusion. 

- In logistic regression, when the output is around $$y=0,5$$ then we should be a little skeptical of the conclusions.
    - Continuing the example from above, after studying for three hours, it is nearly a 50-50 proposition
      whether or not the student will pass the exam.
- In a two-class Bayes classifier, of the probability of $$a,b$$ is $$0.9,0.1$$ then we strong believe in $$a$$. 
    - But
        when those probabilities are $$0.55,0.45$$, we are less certain of our conclusions.

The other place we need to doubt conclusions is when they fall outside of everything that has been seen before. 

- One way to handle anomalies at model construction times is  as described above) to divide the anomalies into similar groups and process each group separately; i.e. fork sub-clusters
- One way to handle models at testing time is that if a new example
      arrives, and it is anomalous, then we should doubt that our AI tool can cope with that data 


## Operations and Ethics


Explanation and transparent:

- Discretization divides many values into just a few, which makes explanation and  transparency easier  (since there is less to explain).

Privacy:

- If clusters only keep samples, not all, of the data, then the non-sampled data is 100\% private.

Inclusiveness:

- If a human has to check the conclusions of an AI tool that uses clustering,  then they 
      need only show them representative samples of the data (i.e. just some
       per cluster). 

Reliability

-  Once data is divided into small clusters, we can quickly check for stability and  (and here reliability)
- Incremental clustering lets us stream over the data and recognize when new data is outside the _certification envelope_
      of what has been seen before.     This also informs reliability.

Effectiveness

- In the happy case where anomalies are localized to particular clusters, then this simplifies repair or pollution marking[^pollute]  (since it
      localizes the regions we need to fix, or avoid). 

[^pollute]: Pollution marking is adding a flag to some regions of a model saying "keep away! Don't use me!". In a hiearchical clustering of data,
we can decide about new examples by descending the hierarchy looking for the smallest cluster nearest the example that is _not_ marked as polluted.


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
and their standard deviation `sd`.

In the `Sym`bolic summary, we see counts of how many `n` numbers were seen, their most common value (denoted`mode`),
and their entropy `ent`.

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
(i.e. using the smallest and largest value seen in column $$i$$) and                  $$0.0000001$$
is a small constant added to the denominator to avoid divide-by-zero errors. 

For symbols, a usual $$diff$$ is 

$$\mathcal{diff}(r,i,a_i,b_i) = 0\; \mathcal{if}\;a_i==b_i\;\mathcall{else} 1$$

If either of $$a_i,b_i$$ are unknown values then _diff_ returns the maximal possible difference. 

- For symbols, that maximum value is 1
- For numbers, if one value $x$ is known then it is normalized to $x'$ and the distance is set to the maximum possible value; i.e.

$$ (1-x')\; \mathcal{if}\; x'> 0.5\; \mathcal{else}\; x'$$

- And, for numbers if both values are unknwon, then _diff_ returns 1.
 
### Clustering (Unsupervised Learning)

The simplest (and sometimes slowest) learner is a clusterer.
Clustering ignores any class or goal variables and group together similar rows using some distance function.
Clustering can be slow since, if implemented naively, it requires multiple $$O(N^2)$$ comparison between all rows.
The famous K-means algorithm reduces that to $$O(kN)$$ as follows:

1. Declare that  $$K$$ rows (picked at random) are the _centroids_;
2. Marks each example with the id of its nearest centroid;
3. Finds the central point of all the rows marked with the same centroid.
h

4. Declares those new central points to be the new centroids
5. Goto 1

K-means terminates when the next set of centroids are similar to the last ones. There are several heuristics for determinging a good value for $$k$$:

- One way is to always us $$k=$$; i.e. recursively apply $$k=$$ k-means to divide the data into 2, then 4, then 8.. clusters (stopping when you hit, say, $$\sqrt{N}$$ of the original data set size;
- Another way is the _elbow_ test. 
    - Define some measure of "goodness" for a cluster (e.g. median distance of members to the centroid). 
    - Increase $$k$$ [looking for the "knee" in the curve](https://bl.ocks.org/rpgove/0060ff3b656618e9136b) after which more $$k$$ does not produce "good clusters" (e.g. those with lower distance members to the centroid)
    - Use the $$k$$ at the "knee".

Once you know your $$k$$, you've got to select $$k$$ centroids
One way is to do it randomly (see the mini-batch k-means algorithm shown below), 
Another way is to use k-means++, which always tries to select centroids that are far away from the existing centroids:


- For $$z$$ in 1 to $$k$$ do
    - Pick any row $$r_0$$ and make  set $$\mathit{center[z] = r_0$$.
    - For every other row, $$r_i$$ (a) find the nearest center made so far; (b) find the distance $$d_i$$ between $$r_i$$ and that center
    - Pick $$r_i$$ as the  next center at probability $$d_i^2$$  [^pick]

[^picl]: to pick $$x_i\in X$$ at probability  $$p_i$$,  find  $$P=\sum p_i$$.  Sort $$x_i \in X$$ in descending order by $$p_i$$.
Pick a random number $$0\le r \le 1$$ and run over sorted $X$. At each step, set $$r=r-  p_i/P$$. When $$r \le 0$$, return $$x_i$$.

It is insightful to think of K-means as an example of _expectiation minimization_ algorithms.
Such algorithms make guesses, then change something to minimize the errors associated with those gusess (in this case, move the centroids).

[Mini-batch K-means](REFS#sculley-2015) is a more memory efficient  version of K-means.
This variant never loads all the examples into main memory. Instead, it only loads _batches_ of rows of size  $$B$$. 
The first $$k$$ rows (picked at raond) become the first $$k$$ centroids. Rows arrive after that (in the same batch) add themselves to a cluster assocated with the nearest
centroid. When the batch is done, each cluster adjust its centroids by reflecting over each row in the centroid:

- For the first row, the centroid moves itself half way towards the row; 
- For the second row, the centroid moves itself one-third of the way  towards the row; 
- And so on such that for the nth row, the centroid moves itself $$1/(n+1)$$th  the way  towards the row; 

The next batch of $$B$$ rows is read and the process repeats. Note that for this to work, we must have a way of moving some cluster $$c$$ towards
row $$r$$. When processing the $$z$$-th item in a cluster:

- For numeric column $$i$$, $$c_i = (1 - 1/z)*c_i + 1/z*r_i$$
- For symbolic columns, at probablity $$1/z$$, $$c_i = r_i$$

An even more effecient clustering algorithm uses random projections. The above clustering algorithms 
are very sensitive to quirks in the distance function. One way to mitigate for those quirks
is sort out the rows using multiple, randomly generated distance measures. Sure, a few may be less-than-perfect
but the more often a random project says two rows are similar, then the more likely they are actually are similar.

Here is the RP0 random projection clustering (there are many others, but this one is pretty simple):

1. Let $$M,P=32,10$$ (say)
2. Read the data. While  you have less  than $2M$ rows, add the rows into a local data cache.
3. If you have more than  $2M$$ rows, then divide:
    - $$P$$ times; pick any two _poles_ (the rows $$x,y$$) in the batch and find the distance between them.
    - Pick the pair of poles with maximum distance.
    - Divide the according to whether or not they are closer to one pole or the other.
    - For each division, goto 2

Note that RP0 is like a faster version of the recursive $$k=2$$-means algorithm described above.

There are many  interesting ways to modify  RP0:
- Do not sub-cluster all data. E.g. only divide on (say) X=50% of data selected (a) at random or (b) spread out between the poles.
This way ensures that sub-trees get smaller and smaller.
- If you only build intra-cluster models, only do that on non-root clusters. Then you can use statistics collected in the parent to inform your decisions in the child.
  Also, the top 2-3 clusters in RP0 are   good to avoid- (since that will be most approxaimate, most error prone).
- Ignore (some) newly arrived data. In this aproach,   an _anomaly detector_ could report if the newly
arriving data is anything like what has been seend before (if so, we can ignore it since it does not add anything
to the model). For example,  in step2, as new data arrives, its distance could be compared to (say) $M$ other things already in the cluster.
If that is less than the $$Y$$ times the median value of all the distances previously seen in the cluster, the new example is boring and might be ignored
(For this approach, [Fayola Peters](REFS#peters-2015) suggests $Y=1$).
In step2, once $$M$$ examples have been read  a classifier/regression algorithm could be executed on the examples in that cluster and executed on any newly arriving examples.


## From Unsupervised to Supervised Learning

Clustering is a knowledge acquisition technique. In short, rather than asking everyone about everything, first cluster the data
then only check a sample of rows from each cluster.

For example, clustering is one way to help _active learning_.
Often we have more rows than labels (a.k.a. classes) for that data (that is, most of our data is suitable only for unsupervised learning). This is a common situation.
For example:

- Suppose it takes 15 seconds to read a four line Github issue before you can say if that issue is 
  "about a bug" or "otherwise".
- Suppose further you have 10,000 such issues to read. Assume you can stand doing that for 20 hours in a standard 35 hour work week (which is actually a  bit of a stretch), and suppose that
  you label issues ina  group of two (so that when labels disagree, you go ask the other person). That labelling task will take two people, four weeks to complete[^mt]-- and you many just
  not have time for that.

[^mt]: Some might comment that this four weeks could be done in an hour, via
[crowdsourcing](https://www.youtube.com/watch?v=Pjm1uYbuyk4),  That's true BUT consider- when comissioning a crowdsourcing rig, you have to first certify the efficacy of that rig. That means
you need some "ground truth" to check the conclusions. So now you are back to labelling some significant percentage of the data. 

For another example:

- Suppose you are doing effort estimation for software projects. It is relatively much harder to access financial details about a project (e.g. the salaries of the workers) than
  the product details about that software.
- This means that your data has many independent rows (the product details) but little or no dependent information.


Given some oracle that can label data (e.g. a human being), and assuming that oracle takes time $$t$$ or costs $$x$$  everytime you ask it a question,
then _active learning_ is the process of learning an adequate model after asking the oracle using minimum time and/or cost.

(Aside: Another way to handle label-shortage is  _semi-supervised_ learning that finds things similar to the labelled examples,
then propagates the labels to the unlabelled space. For example, if you cluster data, then (a) each cluster will have a few labels and (b) the unlabelled
examples in each cluster can be given that cluster's majority label.  Of course, you still have to check if the resulting new labels are correct.
If you want to do that check effeciently (i.e. not check everything) then you'll need some smart way to check a sub-sample of the new labels.
At which point you are back to active learning-- but perhaps with fewer overall queries to the oracle).

An _aquisition function_ is one way to guide an active learner:

- Given a model built from the $$L$$ labels seen to date, go forth and make guesses; i.e. use the tiny model built so far to guess labels for the remaining data.
- Apply the aqusition function to select the most interesting guess
     - e.g. select the guess with the highest/lowest score (if you are truing to maximimze/ minimize something).
     - e.g. select the guess with the highest uncertainty
     - e.g. or select the guess with higest score plus uncertainty
- Give that most interesting guess  to an oracle. Ask them to label it
- Build a new model from  the $$L+1$$ labels.

Here are some important details about the above process:

- When building a new model using the new label, it is useful if the new model can be incrementally 
    - If the number of labelled examples is very small, then anything will do. 
    - But as the labelled space grows, consider using learners that incrementally update very quickly (e.g. fast nearest-neighbors; Naive Bayes).
- The uncertainty of a guess can be determines in different ways, depending on the learner:
    - Within [NaiveBayes](img/boundary.png), the most uncertain guess is the one that with nearly equal probabilities of being in multiple classes. 
    - Within [Logistic regression](https://en.wikipedia.org/wiki/Logistic_regression#/media/File:Exam_pass_logistic_curve.jpeg), the most uncertain guess is the one closest to 0.5.
    - Within [Support Vector Machines](https://quantdare.com/wp-content/uploads/2016/09/svm2.png), the most uncertain row is the one that falls mid-way between the support vectors
    - In an [ensemble learning](https://miro.medium.com/max/590/1*DUaQoSKHX09hLG0QcGApTg.png), an uncertain guess is the one made by the smallest majoirity. For example consider an ensemble of
      built from (say) ten 90% samples of the current data. That ensemble offers a label when 6,7,8,9 or 10 ensemble members vote the same way.
      In that case, the most uncertain guess would be from a majoroty of only 6.
    - [Gaussian process models](https://miro.medium.com/max/700/1*PF8XTtgVm1UYTuRc3U2ePQ.jpeg) offer a mean and standard deviation for each prediction.


## Supervised Learning


Dont traing on  examples , use some sunset (selected at random, or selected froma  cluserr)
move the elarning into the clsuterr so  icnremetnaly do top-down recrsive clsutering and build one mdoel per elaf clsuter)


maths methods highly optimized. For example, SVM with a lienar kernel runs very fast over a large text corpus. 

XXX active:
 and suppose there are

Divide the data,a t random, into 10 buckets.
   - Build one model  rows have class/goal values:
   - Also, when  humans are checking the class columns:
   - Within each cluster, ten times, select 90\% of the data. Find the oddest item (the o

g. Since the learner chooses the examples, the number of examples to learn a concept can often be much lower than the number required in normal supervised learning. 

Of all the above algorithms, standard K-means might produce the best clusters (since it is always reasoning over all the data). On the other hand,
the other variants might scale to larger data sets. 

There any many other ways to cluster data. For a more complete survey, see any textbook on data mining or [some of the excellent on-line tutorials](https://scikit-learn.org/stable/modules/clustering.html).


- range cuts, column cutts (feature selection)
contrast sets (avoding dullr egions)

### naive bayes group and the class and loomfor dfferente ebween theing
XXX decision trees cut on the class
cover and differentiate make a decision the spin hthru the rest

neural ents

## Divide nums (discreitzation)


## Quiz

# u dont nroamlize what happens?
# given standard deviation forumla, derive sd
# given entropy  forumla, derive e
# distance between two rows
# derive the cosine rule
