---
title: Definitions
layout: default
---


Before going any further, we'll need some preliminaries. For example,
what do we mean  by SE? By AI?


### What is SE?



Software is everyware and does everything.
We once challenged a class of students to come
up with one thing that is _not_ mediated, organized,
controlled by software. One student waved a shoe
in the air and said "look! no software!". But when
pressed, the student confessed the shoe was bought on-line
using a digital credit card transaction after they saw
someone else wearing the same shoes on a social media
platform. So in a very real sense, software created
the shoes on her feet.

Software engineering is the creation/ maintenance of some software
product of an acceptable standard, given the available resources (time,
people, tools, etc)[^0].




Software engineering should be (and often isn't) a process of looking
at current software so we can make it better.  
We want to make software better since if we ever we do it again,
we want to do it easier. Also, if we want to scale up the use
of a software solution, then we want  to know how to run
that software faster, with fewer resources.

Sometimes making software better  means
adjusting it and sometimes that means burning it down and starting afresh.
According to W. Edwards Deming[^2] (a prominent writer on quality control),
this process is called _Plan, Do, Study, Act_.
SE needs AI since,
currently, software engineering is very, very good at _Do_ and _Act_ but not _Plan,Study_

-  Many software teams use practice continuous integration. Such CI-teams can
   build and deploy new versions of complex systems, several times per day.
   Any number of other texts explore _Doing_ and _Acting_.  

- But here, we explore _Plan_ and _Study_. Currently, this is mostly a manual
  task done in the heads of human software engineers.
  Which is a problem since humans are talented, but flawed, people.
  When they get
  it right, they can really think up some 
  amazing things [^7] [^8] [^9] [^10] [^11] [^12] [^13] [^14] [^15] [^16] [^17] [^18] [^19] [^20].
  Nevertheless there are so many ways humans routinely get it
   wrong wrong wrong wrong wrong
  (e.g. see the list of [over 100 cognitive biases](cognitivebias)). 

![](https://i.ytimg.com/vi/E46LYc4JpYM/maxresdefault.jpg){: align="right" width="350px"}

Enter artificial intelligence. AI
is the designing and building of intelligent agents
that receive precepts from the environment and take actions that affect
that environment[^1].  More specifically, this is the process of:

- collecting and analyzing the data that lets us understand:
     - what the users want (the objectives);
     - what are the current options;
     - what are the constraints around those options.
- then making choices that:
     - reach as many objectives as we can;
     - as easily as possible;
     - while satisfying most of the constraints.

This means that SE in the age of AI
can use some combination of data mining and optimization:

- _Optimizers_ are algorithms
that take some model (or something)
and then try to learn inputs that lead to better results.
Sometimes (often) there is no model in which
case they can be built via _data mining_.
- Whereas data miners usually explore a fixed
set of data, optimizers can generate more data by re-running the model 
many times,
using different inputs.
Data miners, on the other hand,
reflect over data to return a
summary of that data.

One informal way to characterize the difference between data miners and optimizers is _slice_ versus _zoom_.

- Data miners _slice_  data such that similar patterns  are found within each division.
- Optimizers  _zoom_ into interesting regions of the data,
then then use a model to fill  in any missing details
about those regions. 

Having spent two decades building optimizers and data miners,
we assert that, internal to the code,
 data mining and optimizers are very similar.
Because of this underlying similarity, it is easy
to mix-and-match the services of data miners and optimizers,
in useful ways.
For example:

- When the optimizer is running too slowly, we might apply data mining
  to divide up and simply the problem, then run optimizers on 
  the simplified bits.
- Data miners are configured by many magic parameters. When we do not know
  what choices to apply, we ask optimizers to automatically
  explore those choices.


### "No, no, that isn't SE"

The next page offers examples from software engineering where
data miners and optimizers have been mixed-and-matched in order
to better manage _Plan_ and _Study_.

But before going on, we make the obvious comment that 
the above is just an opinion. And its an opinion that some people might dispute saying (e.g.)

"That's not SE. I know since I am a software engineer and the above says very little about my day to day work." 

To which we reply, that it might not characterize your day to day work... yet. But it will soon. 

We say this SE keeps
redefining itself. There is a long history of people saying "X is not about" and yet, a decade later,
SE is all about X. Consider:


- SE is not about  users (Dijkstra, 79)[^3]
- SE is not about testing (Mills, 1985)[^4]
- SE is not about requirements (Paulk, 1993)[^5]
- SE is not about deployment (before the advent of continuous integration)
- SE is not about AI... yet

Our point here is that even though AI is not a standard tool 
used and studied by 
software engineers, it will soon be. 

If you agree, then read on.

Otherwise, send along your email and we'll check back in with you in 2020.

## Notes

[^0]: Not sure who said this first. But we first heard it from Bojan Cukic.
[^1]: S. Russll and P. Norvig (2009) [Artificial Intelligence: A Modern Approach](https://dl.acm.org/citation.cfm?id=1671238),  Prentice Hall.
[^2]: Aguayo, Rafael (1990). Dr. Deming: the American who taught the Japanese about quality. A Lyle Stuart book. Secaucus, NJ: Carol Pub. Group. p. 76. ISBN 978-0818405198. OCLC 22347078. Also published by Simon & Schuster, 1991.
[^13]: e.g. [UNIX](https://en.wikipedia.org/wiki/History_of_Unix)
[^14]: e.g. [GCC](https://en.wikipedia.org/wiki/GNU_Compiler_Collection)
[^15]: e.g. The [open source community](https://en.wikipedia.org/wiki/Open-source_software) where, on a daily basis, millions of people who have meet collaborate to build, share, and maintain software of unprecedented complexity.
[^7]: e.g. The [green revolution](https://en.wikipedia.org/wiki/Green_Revolution) that feed billions.
[^9]: e.g. [Walking on the moon](https://en.wikipedia.org/wiki/List_of_missions_to_the_Moon)
[^17]: e.g. [Abstraction](https://en.wikipedia.org/wiki/Abstraction)
[^20]: e.g. [Mathematics](https://en.wikipedia.org/wiki/Mathematics), which invented all manner of usefil ideas sich as zero.
[^19]: e.g. Newton's  realization that certain physical laws hold on earth, and in stars.
[^21]: e.g. [Conservation Laws](https://en.wikipedia.org/wiki/Conservation_law#Exact_laws)
[^18]: e.g. The unification of fundamental forces in the universe [light, eclectic, magnetic](https://en.wikipedia.org/wiki/Electromagnetic_radiation)
[^16]: e.g. [Crispr](https://en.wikipedia.org/wiki/CRISPR)
[^8]: e.g. [Invention of perspective in art](https://en.wikipedia.org/wiki/Perspectivity)
[^10]: e.g. The work of [Isamu Noguchi](https://www.noguchi.org/noguchi/timeline)
[^12]: e.g. The work of [Frank Lloyd Wright](https://franklloydwright.org)
[^11]: e.g. The work of [Dieter Rams](https://readymag.com/shuffle/dieter-rams/)
[^3]: B. Boehm (2004) [Keynote address to the ASE'04 conference](http://ase-conferences.org/ase/past/ase2004/download/KeynoteBoehm.pdf), Boehm reports that at ICSE'4 (1979), Edsger Dijkstra commented that "The notion of ‘user’ cannot be precisely defined, and therefore has no place in CS or SE."
[^4]: H. Mills et al. (1987) [A cleanroom approach to software development](https://en.wikipedia.org/wiki/Cleanroom_software_engineering).  Here, the task of programmers was to  delivered probably correct code to a separate testing team.
[^5]: M. Paulk at al. (1993)  SEI Software CMM\* manual (v.1.1). "Analysis and allocation of the system requirements is not the responsibility of the SE group but is a prerequisite for their work."


