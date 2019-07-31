# Tools

Before going on, we digress to offer  a few definitions,

 **Data mining algorithms** tell us "what is" in the data. Data miners extract models   from data. For example, from columns of numbers and <em>programmer experience</em>, <em>development language</em>, and   <em>number of observed defects</em>, then a data miner might learn that defects are  more dependent on the experience of the programmer than the language that they use.  
 
- Example  data mining algorithms
 are  nearest neighbor algorithms like kNN; clustering algorithms like k-Means and EM; statistical learners like Naive Bayes; equation learners like linear or logistic regression; decision tree learners like C4.5,   and CART; meta-learners like AdaBoost; and many other as well including  Apriori,, PageRank,  neural networks (and deep learners); etc.
 
**_Optimizers** tell us "what to do". Optimizers look  at models and tell us how changes in something effects something else. Ideally, optimizers also tell us the <em>least_</em>we need to do to <em>most</em> improve something. For example, an optimizer might report that defects can are most reduced   using   developers with two years of experience. They might also report that improving experience to three, four, five years (and above) offers little extra reduction in observed defects. 
 
-  Example optimizers include genetic algorithms like NSGA-II, MOEA/D and differential evolution;   sequential model-based optimization methods like FLASH and SMAC; and other approaches such as particle swam optimization, tabu search; and many more besides


**Theorem provers** are very specialized tools for finding settings to variables that satisfy the logical constraints of a model. Such a theorem prover might report that  A=true and B=false satisfies the constraint (A and not B).   For example, the constraints of the kernel of the Linux operating system can be expressed as hundreds of thousands of constraints.  When optimizing the design of some new version of Linux (e.g. to try and avoid  modules  with a track record of problems) we can use theorem provers to (a) generate a population of valid designs; and (b) check the validity of a new design. 

-  Example theorem provers include  maxWalkSat, pycoSAT, MathSAT, vZ, Z3,  and many more besides.

Note that <b>optimizers are model-based</b> and <b>data miners are data-based</b>. 

-  Data miners explore whatever data is available.
-  Models, on the other hand, can be used to build more data whenever they want, just by running the model some more. 

This means that:

-  data miners explore a fixed data space
- while optimizers explore a more fluid data set (since they can  zoom into little cracks in the data, expanding that part of the data as they go).

Note also that optimizers and data miners are tightly inter-connected:

- Data miners can learn a model which [can be used by optimizers](REFS.md#feather-2002).  
- Optimizers can [adjust the control parameters of a data miner](REFS.md#fu-2016) such that those data miners learn better models (technical note: this is called [search-based software engineering](REFS.md#harman-2012)).

