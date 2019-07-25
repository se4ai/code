# More About Learners

STAR is a rule learner that
uses some unsupervised discretization to divide all the independent numeric columns into bins.
It then divides a numeric dependent column into (say), 20\% best values and 80\% rest. 

-  Let the number of rows in best and rest be $$n_b,n_r$$, respectively.
- Each bins $$X$$ in the independet columns appears at some frequency $$f_b,f_r$$ in best and rest.
- The preferred bins are those that (a) occur frequently in best and (b) occur more frequently in
  best than rest. 
     - That is, the rank of bin $$b_i$$ is $$R(b_i)=p^2/(p+q)$$ where $$p=f_b/n_b$$ and $$q=f_r/n_r$$.
- Using $$R$$, STAR sorts all the bins $b_i$ into the list
  $$b_1,b_2,b_3,...$$ in descending order of rank (so  $$R(b_i) \le R(b_{j>i})$$).
- STAR then selects all the rows in steps:
    - The first step contains  the first bin $b_1$
    - The second step contains two bins $$b_1,b_2$$;
    - The third  step contains three bins $$b_1,b_2,b_3...$$ 
    - And so on.
- This stepping process is a greedy search that stops with the $$y_i$$ values seen in rows selected in the current  step
  are no better than those seen in the step before.
- STAR then prints  all the bins used in the steps before the last stopping step.

In practice, STAR often [stops very early](REFS#menzies-2007); i.e. after just  a few steps). 

Details:
i
step 1
- Note that at each step may encournter bins from new attributes, or attributes already used in prior
steps. In the former case, the number of rows at this step will _decrease_. But in the latter, the number
of rows at each step i _
- To speed this up, for each bin cache the set of rows that have this bin. Many programming languages
   support very fast set 

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


