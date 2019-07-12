---
layout: abc
title: About Optimizers
---


## About Optimizers

This part introduces some terminology that we'll need as we go along.


Recall that we said above
that many data miners learn models of the form

$$
Y = f(X)
$$

where $$X$$ are the indepedent variabes and $$Y$$ are the depedent variables.

Optimiers, on the other hand
learn models the explore changes (deltas, or $$\Delta$$) to variables:

$$
{\Delta}Y = f'({\Delta}X)
$$

Sometimes $$Y$$ is not one feature, but a whole set ($$Y=y_1,y_2,...$$),
some of which might compete with each other
(e.g. improving $$y_1$$
might hurt $$y_2$$). 
Later in this book, we will spend much time
exploring trade-offs between
competing goals for such _multi-objective optimization_ problems.



