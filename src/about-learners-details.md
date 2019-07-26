# More About Learners

In the last two chapters, building models using data miners was characterized 
as
a _division_ process that breaks the whole data into sub-regions.
Also 
that process can be initialized via discretization that divides sets of numbers.

This chapter expands on that characterization. First, we discuss model building
as iterative  discretization. Next, we discuss other kinds of learners that use
of other ways to divide the data.

## Iterative Discretization

If descretizers  divide a whole space into interesting parts, why not build
models by just iterating  the same process within each part?

For example, STAR is a rule learner where most of the work is in the dsicretization
(followed by a little greedy search).
STAR
uses some unsupervised discretization to divide all the independent numeric columns into bins.
After  sorting the bins according to some domain specific criteria, it tests
the effect of a rule built from just the top sorted bin, then the top sorted bins, then the top
three,  etc.
STAR stops when the effect of the first $$i$$ bins is not better than the first $$i-1$$
(at which points it recommends all the bins 
$$1 to i-1$$).
In practice, STAR often [stops very early](REFS#menzies-2007); i.e. after  just  a few steps.
For domains where this is true, this makes STAR a useful method for generating tiny rules.

More specifically, STAR divides a numeric dependent column into (say), 20\% best values and 80\% rest. 

- Let the number of rows in best and rest be $$n_b,n_r$$, respectively.
- Each bins $$X$$ in the independent columns appears at some frequency $$f_b,f_r$$ in best and rest.
- The preferred bins are those that (a) occur frequently in best and (b) occur more frequently in
  best than rest. 
     - That is, the rank of bin $$b_i$$ is $$R(b_i)=p^2/(p+q)$$ where $$p=f_b/n_b$$ and $$q=f_r/n_r$$.
- Using $$R$$, STAR sorts all the bins $b_i$ into the list
  `$$b_1,b_2,b_3,...$$` in descending order of rank (so  `$$R(b_i) \le R(b_{j>i})$$`).


If you want to implement STAR, here are some important details:

- To score a set of bins:
     - find all the rows that match those bins
     -  then compute the mean of the dependent variable in those rows.
- To fast find rows that a set of bins:
     -  Build a data structure that stores a bin, plus a set of rows that have that bin.
     - Note that this data structure can be populated in the initial unsupervised discretization process.
- To fast find rows that satisfy the first $$i$$ bins:
     - Use set operations.
     - If ranges are stored in sets (as per the last tip), then  take the $$i$$ bins are divide them
       according to what attributes they use.
     - First run over all the attributes and combine their sets using a set union operator
       (e.g.  when combining the rows using _age=low_ and _age=high_, you want to find the rows
       with  _age=(low or high)_, which can be done via set union).
     - Second,  run over the rows from different attributes and combine those sets with a set intersection operator
       (e.g. if 20 rows have _age=hi_ and 10 rows have _car=ford_ then a set interesction will find the
        subset of the 20 rows having _age=hi_ and _car=ford_).
- As STAR a large number of $$i$$ bins, then usually most of the improvement happens with the first few bins
  (after which, it is a case of diminishing returns). Greg Gay recommends, therefore, to add it more and more
  bins at each step[^keys2]. That is:
     - At first, try jsut the top ranked $$i=1$$ bin.
     - Next , try add in two more bins (so now we are looking at bins $$i_1,i_2,i_3$$;
     - More generally,  at step $$j$$, always add $$j$$ more bins.
- If the rows have multiple numeric goals (some of which are to be minimized and some are to be maximized),
  use some _aggregation_ function to combine these into on dependent variable (which STAR can divide
   into 20\% best and 80% rest). 

[^keys2]: See his [KEYS2 algorithm](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.650.3238&rep=rep1&type=pdf).

Further to the last point, for aggregating multiple goals, we recommend
[Zitler's indicator method](REFS:zitler-2004)
since this known to [better aggregate  multiple-goals](REFS:sayyad-2013).
This method reports what loses least: moving from _here_ to _there_
or _there_ to _here_
(and the row _here_  is preferred if moving to _here_ results
In the following code:

- In the weights array,  -1,1 means "minimize, maximize" respectively.
- Objective scores are normalized 0..1 since, otherwise,
the exponential calculation might explode.

```python
def x_better_than_y( 
            x,y,     # two rows
            weights, # dictionary of objective weights,
            goals,   # list of goal indexes
            lo, hi): # lists of low,high values of goals  
    xloss, yloss, n = 0, 0, len(w)
    for g in goals:
        a      = normalize( x[g], lo[g], hi[g] ) 
        b      = normalize( y[g], lo[g], hi[g] )
        w      = weights[g]
        xloss -= 10**( w * (a-b)/n )
        yloss -= 10**( w * (b-a)/n )
    end
    return xloss/n < yloss/n

def normalize(z,lo,hi): return  (z  - lo) / (hi - lo + 0.00001)  
```









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


