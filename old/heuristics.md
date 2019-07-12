---
title: Heuristics
layout: default
---

![](https://divergentmba.files.wordpress.com/2010/04/knowledge-funnel-762867.png){: align="right" width="350px"}


  
- Andres's law: Show me the code
   - We will seek to operationalize all the deas of theis book. 
   - RAISE0: a baseline system, deisnged to inspire, to irritate, to make you wrote better systems.

- But can you cut my code base in half?
   - yes, this is all "just reinforcement learning" and "just bayesian parameter
     optimization" and "just search-based SE" and "just optimzation"
   - but the devil is in the detail. if we lean in to how to write wokrable systems for
     all the above then 

- Beliefs are sticky things
   - hang around much longer than they should
   - need to always be revising

- George's law: all models are wrong (but some are useful)
    - In a complex system of only a modest number of variables and interconnections, any attempt to describe the system completely and measure the magnitude of all the links would be the work of many people over a lifetime ([207], p5).
    - As complexity rises, precise statements lose meaning and meaningful statements lose precision.


- Mary's law: "Insisting on (perfection) is for people who don’t have the b\lls to live in the real world.”
   - Mary Shafer, SR-71 Flying Qualities Lead Engineer, NASA Dryden
   - We don't live in a certain world. 
   - [maryrisk](There's no way to make life perfectly safe; you can't get out of it alive.)
   - Youse payz your money and youse take your choice. There's no other way, no backsies (second
     law of thermodynamics)

- Accuracy ain't, precision isn't
   - Which means, as a side-effect, that the way we look at the world can cause systematic errors in what we see
   
- Xenophane's law: for all is but a woven web of guesses
   - Despite all the maths and amchnery, all conclusions are based on their assumptions. No way to
     avoid that. Karl Popper here.
   - [Devabux ICSE'16]
   - [Cognitive biases](cognitivebias)
   - Best we can do is to state our conclusions, and those assumptions; 


- Conclusions need certification
   - a second oracle that can screams wehn you ask a question that i should not answer
     (the challenger disaster lesson)
   - whenever you find something unfair, incorrect, write a little scrtipt to check for 
     that problem in future

- Fairness is a choice and not choosing is unfair

- The technology that will most improve data science is.. science
   - Science = a cache of concepts curated by a community, doing each
     other the courtesy of (re)checking and improving each other's ideas.
   - Most data science is not science

- Ken's law: I want to read symbols. 
   - Qualitative representations—symbolic representations that carve continuous phenomena into meaningful units—are central to human cognition.
   -  They provide a foundation for expert reasoning in science and engineering by making explicit the broad categories of things that might happen and enabling causal models that help guide the application of more quantitative knowledge as needed. 

- I want to argue with you.
    - why have symbolix represnetations

- Not general models, but general methods for local models.

- Tom (Zimmermann)'s first law:  Live with the data you have
    - data has answers, for the questions you aren't asking (yet)

- Tom's second law:
   - projects mature from "many one-off" queries to a "just a few repeated"  ones

- Tim's first law: ask a lot of questions, expect a few answers

- Your configuration is wrong (probably)
   - Major area, previously under explored

- Wei's Law: It will take 3+ months.

- Wei's second law: One data scientists per two (or three) data engineers

- David (Wolpert)'s law: no such thing as a free lunch (no learner or optimzier is always best).
   - So your going to have to look around some

- A foolish consistency is the hobgoblin of little minds
   - Just because it works tehre don't mean it works here
   - SE data is different (may nit correspond to known bias/variance effects;  binkely's agrument, amrit's study)

- George's law: better learners/optimizer are rare, [so better better is even rarer rarer](http://www.cs.cmu.edu/~gmontane/pdfs/montanez-2013-bounding.pdf).
   - So you don't have to look around forever

- Fisher's Law: "Fast iteration is key"

- Timm's law: AI should be agile and often it aint

- Dave (Binkley)'s rule: Your learners ain't my learners
   - Software specific inference

- Dieter's Law: Less, But Better
   - Particularly when exploring options

- Most data is crap data PCA, 1901
   - Narrows: Amarel 1960s
   - Prototypes: Chen 1975
   - Frames: Minsky, 1975
   - Min environments: DeKleer, 1986
   - Saturation: Horgan & Mathur: 1980
   - Homogeneous propagation: Michael: 1981
   - Master variables: Crawford & Baker, 1995
   - Clumps, Druzdel, 1997
   - Feature subset section, Kohavi, 1997,
   - Back doors, Williams, 2002
   - Active learning: many people (2000+)

Vasil's Law: The best thing to do with most (SE) data is to throw it away
   - Ignore small trivial differences in numerics (discretiation).
   - Ignore dull columns (feature selection)
   - Ignore dull ranges (range selection)
   - Ignore rows with dull ranges (instance selection)

Fayola's Law: only share the interesting bits
   - What's left after vasil's stuff

Repeat all conclusions, 10 times, using 90\% of the data.

- Zach's law: start as you mean to go on

- Vivek's law:  guess is faster than knowing (surrogates)

- Jack's law: a couple of darts beats smarts

- Amrit's law : most differences, aren't

- Tim's first law: not studying theory is bad

- Tim's second law: too little theory is a very bad.
    - Talk to the users . build the hypothesis matrix

- Tim's third law: too much theory is a very very bad.
    - Just because someone else argues that it won't work, they might be wrong
    - E.g. bias/variance trade off

- Tim's fourth law: step away from the trivial
   - not tiny effects, bit ones
   - coarse grained states

- Tim's fifth law: pictures for intuitions, stats for sanity

- Tim's sixth law: localize!

- Data miners for one goal, optimizers for N

- Suvodeep's rule: If your optimizer is slow, add a data miner

- Martin's rule: if your optimizer is confusing, add a data miner.

- Jianfeng's first law: verfication is faster than repair, repair is faster than generate

- Jianfeng's second law: the deltas between valid examples are (usually) valid

- Jianfeng's third law: things that need repair are more interesting than otherwise



----

## Design Choices for Systems

- Speed of model
- Speed of constraints
