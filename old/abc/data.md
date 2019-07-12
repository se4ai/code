---
layout: abc
title: About Data
---


## Summary

- Data can be _stuctured_ or _unstructured_;
- _Tables_ are one way to structure data. Tables have  _columns_ (also called  _features_ or _attributes_ or _variables_);
+ The columns may be _numeric_ (has numbers) or _symbolic_ (contain symbols).
- Features can be _independent_ or _dependnet_
- Dependent features (also called _goals_)  can be _classes_ or _objectives_
- Learners are often used to explore problems with only one dependent variable.
- Multi-objective optimizers are often used to explore problems with many dependent variables.

## About Data

Lets start at the very beginning-- its a very good place to start.
When we read we begin with a-b-c. When we mine we begin with... data.

## Unstructured Data

Reader beware: Most data does not arrive in a well-structured form (like that discussed below).
For example, when mining text we have to handle
spelling mistakes,
tables in inconstist formats,  the same words taking on different meanings, etc etc.
In fact, in text mining, it is not even clear where one cencept ends  and another begins.
For those reasons, text mining is so much fun.

In any case, when  data does not come in an unstructured form (and it usually does not) it is the task of the data scientist
to uncover that strucutre. This book has sevearl chapters on exactly that
process (see [data collection](/dm/collect), [data cleaning](/dm/clear),
[data labelling](dm/label) and [feature engineering](/dm/feature)).
For now, we'll assume some magician has waved a magic wand over the data to produce stuctured data.

## Structured Data

Different kinds of data miners work best of different kinds
of data. For structured data, that  data may be views as _tables_ of examples:

+ Tables have _columns_, also know as features or attributes or variables.
+ The columns may be _numeric_ (has numbers) or _symbolic_ (contain symbols).
+ Columns may contain missing values.
+ Tables have one _column_ per feature and one _row_ per example. 
+ Also, some columns are goals (things we want to predict using the
  other columns).
    - Goals are often called _dependent_ variables and the other columns ar called _independent_.
    -  Data mining algorithms seek combinations of the independent
       values that predict for the dependent values. 
    - Optimizing algirthms seek changes to the independent values
      that predict for _changes_ in the dependent values.

For example, in _text mining_, where there is one column per
word and one row per document, the columns contain many missing values
(since not all words appear in all documents) and there may be
hundreds of thousands of columns.

Text mining applications can have many columns. 
Big Data
applications can have any number of columns and millions to billion
of rows.  For such very large data sets, a complete analysis may be
impossible.  Hence, the data must be sub-sampled or treated
 probabilistically.
  
On the other hand, when there are very few rows, data mining may fail
since there are too few examples to support summarization. For such
sparse tables, nearest neighbors may be best. Such methods make
conclusions about new examples by looking at their neighborhood in the
space of old examples. Hence, they may only needs a few (or even only one)
similar examples to make conclusions.

If a table has many goals, then some may be competing; e.g. it may not
be possible to find a car with the twin goals of low cost and low
miles per gallon.  Such competing multi-goal problems can be studied
using a _multi-objective optimizer_.

If a table has no goal columns, then this is an _unsupervised_
learning problem that might be addressed by (say) finding clusters of
similar rows.
An alternate approach
is an 
association rule learner that  assumes ever column
is a goal (then it to looks for what combinations of any values predict for
any combination of any other).

If a table has one goal, the this is a _supervised_ learning problem
where the task is to find combinations of values from the other
columns that predict for the goal values.

+ Note that for data sets with one discrete goal feature,
  it is common to call that goal the _class_ of the data set.
  
The following table shows a _simple data mining_ problem. Such problems
are characterized by tables with just a
few columns and not many rows (say, dozens to thousands).
The early machine learners all worked on the
these simple data mining problem
(and note that with some clever sampling of the data, it is
possible to scale these traditional learners to Big Data problems.  

In this table, we are trying to predict for the goal of
`play?` (and note that `temp` and `humidity` are numeric columns and
there are no missing values).

 outlook |   temp |  &nbsp;humidity&nbsp; |  windy |   play?
-------- |   ---- |  --------             |  ----- |  -----
overcast |     54 |        65             |   TRUE |    yes
rainy    |     58 |        70             |   TRUE |     no
rainy    |     59 |        80             |  FALSE |    yes
sunny    |     59 |        70             |  FALSE |    yes
rainy    |     68 |        96             |  FALSE |    yes
rainy    |     70 |        91             |   TRUE |     no
overcast |     70 |        90             |   TRUE |    yes
sunny    |     70 |        95             |  FALSE |     no
rainy    |     71 |        80             |  FALSE |    yes
sunny    |     72 |        70             |   TRUE |    yes
sunny    |     81 |        90             |   TRUE |     no
overcast |     83 |        75             |  FALSE |    yes
overcast |     85 |        86             |  FALSE |    yes
sunny    |     85 |        85             |  FALSE |     no
{:class="table table-bordered table-striped"}

## Ranges

An important concept in a column are _ranges_ of values.

- Symbolic column have one range per symbolic value; eg.. for _outlook_,
its ranges are _overcast_, _rainy_, and _sunny_.
- For numeric columns, ranges can be inferred. For example,
  the `temp` column shown above is charted below. Note that
  this sequence can be approximated by the three ranges
    - _temp &lt; 68_
    - _temp &lt; 81_
    - _temp &ge; 81_


![](/img/abcdatatemp.png)


The process of converting the numbers into a column into
a small number of ranges is called _discretization_ (and we will
disucss it later).
