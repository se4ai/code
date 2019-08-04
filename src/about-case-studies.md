# 4. Ethics : how

The premise of this book is that
AI tools offer a rich tapestry
of choices 
that
software engineers can weave
through to a variety of goals (and which can include ethical goals). 
This chapter offers specific examples of that process.

Our point will be that,
in the 21st century, the wise software engineering
knows how  different AI tools offer different services, and how some of those services
can achieve certain ethical goals.

The following algorithms will be mentioned briefly (and for
more details, see later in this book):

- Data pre-processors like feature selection;
- Classifiers like Naive Bayes and KNN (kth-nearest neighbor);
- Neural net methods like deep learning;
- Theorem provers like picoSAT; XXX
- Meta-learning schemes like active learning.
- Optimizers like sequential model-based optimization (a kind of active learning);
- Hyperparameter optimizers (again, like sequential model-based optimization);
- Explanation algorithms like LIME or FFtrees;
- Certification envelope technology such as prototype discovery and anomaly detection
- Repair algorithms, which can include contrast set learners;
- Clustering algorithms, and hierarchical clustering using recurisve random projections;
- Incremental learning that updates its models after seeing each new example.

For the reader uninterested  in ethics, this list will be very dull indeed.
Such readers will (most probably) return to using a single learner/optimizer/whatever over all their future AI
applications.

For the industrial practitioner who wishes to distinguish themselves within the currently
crowded AI market, the above list might be a marketting opportunity. Spefically,
by augmenting their current toolkit with some of the above, they might be able
to offer services that is absent amongst their  rivals.

For the researcher who is an advocated of a particular AI tool,
the above list might inspire a research challenge.
First, they might seek ways  to extend their preferred AI tool
such that it covers the more of the above services.
Secondly, they might scoff at this list, saying "I can do better than that". If they then went on
to implement and evaluate their alternative, then that would be a very good thing
(since that would give us more material for version two of this book).

## Current Ethical Concerns

Before doing anything else, we need a list of potential ethical goals for AI
tiools.  The  [Institute for Electronics and Electrical
Engineers](/REFS#IEEEethics-2019) (IEEE) has   discussed general principles for
implementing autonomous and intelligent systems (A/IS).  They propose that the
design of such A/IS systems satisfy certain criteria:

1. _Human Rights:_ A/IS shall be created and operated to respect, promote, and protect internationally recognized human rights.
2. _Well-being:_ A/IS creators shall adopt increased human well-being as a primary success criterion for development.
3. _Data Agency:_ A/IS creators shall empower individuals with the ability to access
   and securely share their data, to maintain people’s capacity to have control over their identity.
4. _Effectiveness:_ A/IS creators and operators shall provide evidence of the effectiveness and fitness for purpose of A/IS.
5. _Transparency:_ The basis of a particular A/IS decision should always be discoverable.
6. _Accountability:_ A/IS shall be created and operated to provide
   an unambiguous rationale for all decisions made.
7. _Awareness of Misuse:_ A/IS creators shall guard against all potential misuses and risks of A/IS in operation.

Other  organizations, like [Microsoft](/REFS.md#microai-2019)
offer their own principles for AI:

- _Transparency_ AI systems should be understandable
- _Fairness_: AI systems should treat all people fairly
- _Inclusiveness_  AI systems should empower everyone and engage people
- _Reliability &amp; Safety_ AI systems should perform reliably and safely
- _Privacy & Security_: AI systems should be secure and respect privacy
- _Accountability_: AI systems should have algorithmic accountability

Ethics is a
rapidly evolving concept so it hardly surprising to say that mapping
the stated ethical concerns of one organization (Microsoft) into
another (IEEE) is not easy.  
Nevertheless,
the following table shows one way we might map together these two
sets of ethical concerns. Note that:

- "accountability" and "transparency"  appear in both the IEEE and Microsoft lists. Clearly these
  are concerns shared by many people.
- Also missing from the Microsoft list is "effectiveness" but
  we would argue that what IEEE calls "effectiveness" can be expressed
  in terms of other Microsoft terms (see below).
- Assessed in terms of the Microsoft terminology, the IEEE goals or "well-being" and "awareness of misuse"
  are synonyms since they both reply on "fairness and "reliability and safely".


|                | Accountable|Transparent|Fairness |Rely+Safe|Inclusive|Private+Secure|
|Accountability  |  &#10004;  |           |         |         |         |              |
|Transparency    |            |  &#10004; |         |         |         |              |
|Well-being<br>+ aware of misuse||        | &#10004;| &#10004;|         |              |
|Human-rights    |            |           | &#10004;|&#10004; |&#10004; |              |
|Data agency     |            |           |         |         |&#10004; |   &#10004;   |
|Effectiveness   |   &#10004; |           |         |&#10004; |         |   &#10004;   |
{: border="1px" align=center }

The reader might dispute 
this  mapping, perhaps saying  that 
we have missed,
or missed out, or misrepresented, some vital ethical concern.  This  would be 
a good thing since that would mean you are now engaging in discussions about
software and ethics.
In
fact, the best thing that could happen below is that you say "that
is wrong; a better way to do that would be..."
As  George Box said,  all models
are wrong; but some are useful.  

In any case, what the above table does demonstrate is that:

- Large organizations are now very concerned with ethics. 
- When they talk about ethics, there is much overlap in what they say.
- This is a pressing need to extend our current design thinking for AI tools. Hence, this book.
 
## From Ethics to Algorithms

The above table maps between ethical concerns  from different organizations.
The rest of this chapter discusses how different algorithm choices enable these
ethical goals.  
### Effectiveness


It is unethical to deliver an AI tool that is performing poorly,
particularly when there are so many ways to make an AI tool perform
better.  As discussed in our chapter on [Baselines](about-basleines),
no AI tool works best for all problems. Hence, we exploring new
problems, there must be a _commissioning_ process where different
AI tools are explored and/or adjusted to the local problem:

- AI tools come with defaults from their control settings. Those defaults may
be wildly  inappropriate for new problem.  For examples of this of this, see
Section 2 of [Nair et al.](REFS#nair-2018).  Hyperparameter optimizers are
tools for automatically finding tunings that can greatly improve effectiveness.
For examples of this, see [Fu et al.](REFS#fu-2016) and [Agrawal et
al.](REFS#agrawal-2018a). One way to implement such hyperparameter optimization
is via active learning (see below). 

The faster the algorithm,
the easier it is to fiddle with. So measured in terms of
_commissioning effort_,
 we prefer linear time methods (e.g.  Naive Bayes)
to very slow algorithms (e.g. KNN,  that scale very poorly to large 
data sets).

- Naive Bayes classifiers keep different statistics on rows of different
classes. When new data arrives, such a classier can be quickly updated, just by
adding to the stats of the class of that new row.  
- On the other hand, KNN algorithms make conclusions by interpolating between
the k nearest neighbors.  In practice, this is very slow since finding the
Kth-nearest neighbors requires a full pass over all the training data for each
new test instance.
- KNN can be made faster via clustering algorithms that group together similar examples.
  Once grouped, KNN only needs to within a group. 
- Just as an aside, clustering can be made very fast using tricks
like 
recursive random projections (RRP).
After a few random samples, it is possible to find two moderately distant points "_east,west_"
Data closest to "_east_" or "_west_" can clustered into two groups.
Repeating this recursively "_N"_ times generates a tree of clusters of depth "_N_",
the leaves of which holds
data that is 
similar according  to "_N_" random projections  over "_east,west_" pairs.

It is important to stress that the  commissioning   effort cannot be the only way we assess
an AI tool.  For high dimensional image data, deep learning] has
proved to be very effective.

- Deep learners are n-layered neural networks were layer "i" find
new features hat layer "i+1" uses to make new conclusions.

Training such learners can be a very slow process, so tuning and
comparing with other learners may be impractical.  In this book we
made no case that deep learning (or any other AI tool) is inherently
better or worse. Rather, our goal is to  map the trade-offs associated
with  AI tool such that the best one can be selected from the next
problem.

### Inclusiveness

Inclusiveness is helped
by AI tools that generate succinct human-readable models 
since  
humans can read and understand  such models.
Rule-based learners like  FFTrees are useful in the regard:

![](/img/fft.png){: .imgright}

-   [FFtreess](REFS#phillips-2017) are a heuristic methods  to test  different learning biases using  problem-specific goals.
    FFtrees ranks different divisions of data columns according the goal of the learning (e.g. for each division, how
   many positive/negative examples does in cover).
   At every level of its tree building, FFtrees fork two sub-trees for
   two different biases (the subsets of the data that do/do not match the worst/best division). 
    In this way, dividing "_N_" levels produces $$2^N$$ different
   trees. The tree that performs best (on the training data) is then selected to apply to the test data. 
- In practice, FFTrees generate very small binary trees of depth four or less. Humans can quickly glance at such
  trees, [then critique or apply them](REFS#gigerenzer-2008). Desipte their small size, they can be [remarkably effective](REFS#chen-2018).

AI tools that enable human-in-the-loop reasoning abllow 
ee Hu'18 and anything that does human-in-the-loop reaasoning
During commissioning, there is usually an audit process where some "ground truth" is established against which we 
(a) train the AI tool(s) or (b) evaluate the performance of  the tool(s). In many domains, creating that
ground truth requires an incremental exploration of many examples. For that process, active learning is very useful.

- Active learners  incrementally build models using the minimum number of queries
  to some oracle (e.g. some human). 
     1. For example, if some as-yet-unlabelled examples fall near the decision
  boundary between two classes, then  the label for that example is _uncertain_. 
     2. One active learning stratefy is to
  ask the oracle about the next most uncertain example, the  update the model using that new information.
     3. Such learning strategies often dramatically descreses the number of examples
       need to build a ground truth or comission a model.
- Active learning is simpler when models can quickly update themselves.
    - Examples of such fast incremental update algorithms include Naive Bayes and RRP and many others besides.
- Sequential model-based optimization (SMBO) is an active learner that assumes it is fast to guess
  a value for a new example (if we have a model) but slow to confirm that guess (by running some oracle).
     - For example, when optimizing a data miner,
  SMBO might explore random settings to the control parameters of that learner. 
     - As it evaluates different
  settings, it builds  a model predicting the effect of a particular setting.
     -  The next setting it tries
  might be the one that is guessed to [achieve the highest predicted  score](REFS#nair-2018).


see explanation work [Feather'02]  [Menzies'07] [Gay'12] [Matheer'16]

active learning

### Fairness

- See [Charaborty, 2019](REFS#chakrabory-2019).

### Privacy and Security

privacy.centralized. target fr hackers. ditsibuted with transitions: dat tehft during transitions. why send alld ata
prorotype generation.

### Reliability  and Safety
One an AI tools survives the commissioning process, it must be  monitored. Once again, as we stream
across newly arrived data, it is useful to deploy incremental learners that can quickly react to new data.

- One useful tool for monitoring is an anomaly detector that can report when new data is far and away removed
from the data seen so far.  Detecting such anomalies is important since we cannot trust an AI tool that encounters
something far removed from its previous experience. 
- One way to build an anomaly detector is to use RRP. As a side-effect of computing distance to each "_east,west_"
  pair in any cluster, we can collect the mean and standard deviation of all the distances seen in that cluster.
  With that information, we can declare something to be anomalous if its distance is   
  [more than "_N_" standard deviations away from the mean](REFS#peters-2019).
- Another way to build an anomaly detector is to continuing active learning (including SBMO) after the comissioning process.
  Anomalies can be reported when the predictions from active learning/SMBO do not
  match the newly incoming data.

    - via multi-goal reasoning (so you known how reliabilty you are satisfying the goals of different users of the ssytems),
    - see [Sayyad'13](REFS#sayyad-2013)
    - via certification envelope (see Peters13]

### Transparency

Transparencey: 

    -transparent makes users of a  system aware ot the use and misue of that ssytem
    - see explanation work [Feather'02]  [Menzies'07] [Gay'12] [Matheer'16]


### Accountability

- enabled by trasnparency and relaiblity abd safety


### Well-being and Awareness of Misuse
Well being & Awareness of Misue    
- Fairness : 
- Relaibility & safety: 
- Also helped by transparency


Human rights
- enabled y Fairness
- enabled by relaibir & Safey
- enabled by inclusiveness
   - a system is inclusiveness if it allows people toudenradnand change it see 
   - see Hu'18 and anything that does human-in-the-loop reaasoning

Data agency: 
- inclusiveness
- privacy and sharing

Effectiveness
- accountability (so you can see what is going on)
- priavy and safety (so you can share what is going on, and when not to use)
- reliabilty and safey
- testability : need testing not tbe resource isntancesve (otherwise we are discoruaged to do it)
     - optimziation
     - prototype selection
     - incremental learning
       
[Charaborty, 2019](REFS#chakrabory-2019).
- Models are unfair when the eprformance ofa mdoel isvery differnt for social groups
  with tranditioanlly different degrees of  privleidge (e.g. groups identified by race, gender, sex, age) 


EFFEVECTIVENES, ACCOUNTABILITY, TRANSPARENCY Milton, Gay: Contrast set learning

- Assess ranges via their 
- repair

SECURITY (while sharing)- Papakroni (master, 2019)
- prototype generation.
- Inclusiveness

PRIVACY & SECURITY (while sharing): Peters: 
- privacy and sharing, cmompression (prootoype detection), streaming, sharing (transfer learning)
- discretization to convert columns into bins
- importantance ranking for bins 
     - better bins better select for the target class
- column pruning 
     - to prune the dull columns
- row purning (to prune rows without important bins)
- clustering (to group the rows)
- anomaly detection (to report when enw data is unlike what is already in the clsuter)
- sharing via "keep the anaomalies" (only sharedata that extends an existing cache; i.e. only your anomalies)
- privacy via row + column pruing, then mutation of the surivors up to, but not over the boudnary between this class and that


EFFECTIVENESS Krall: 
- active learning, optimization, compression (prototype detection)
- optimziation via recurisve bi-clsutering
     - repeat for N generations
         - find two distant points, rank them 
         -   if cluster small: mutate all data towards top ranked point
         - else,
              split data by distance to those points, cull the worst half, recurse

[Feather'02]:
requireemetns ptimziaiton via rulebased programming. instead of demanding action on 90 items, the rule-based methods seen in theese studies
found one-thrid of attributes that ost materredamd proposed controlelrs just for those.
- accoring to aharmon, this was one of the first example sof automated multi-obejctive reasoning  in requiremetns engineering.

[Menzies'07]: kike Featuer'02. but this time, for general mdoels of SE (not some very domain-specific mdoels for NASA).

[Gay'12]: kYES2: liek Feather'02 but now much faser and applied to very complex NASA models (controlling sacrecreaft re-entry).

[Mathew'17]: like [Featyer'02], recongizing of a very small (12%) of the factors that mattered the most. all those factors
were ranked so users could see what mas msot to elast improtant.  Here, the models being explored were some of the alrgers models yet 
processed automatically in requirements engineering.

[Sayyad'13](REFS#sayyad-2013)
-  mutli-goal reasoning and  optimization
- support exploratin of trade-off between miltiple competing goals

EFFECTIVENESS Chen (Ph.D. 2019) 

INCLUSION, EFFECTIVENESS Nair (Ph.D. 2019): 
- sequantial model-based optimizaion, icnremntal reair, streaming
- Do all the above using  very small samples of the data 
- Faster reasoning, with a place for humans to peek in and guide the reasoing 

EFFECTIVENESS Fu (ph.D. 2018): Effectiveness
- Hyperparamter optimization


EFFECTIVENESS, RELIABILTIY, Krishna (Ph.D. 2019?): 
- planning. repair, sharing (transfer learning)

TRSANSPARECENY, Chen (Masters, 2018): 
- explanation, 
- FFTs

EFFECTIVENESS Amrit (Ph.D. 2019): 
- very fast hyperpamater optimziation
- jsut a few dozens samples

EFFECTIVENESS Yu (Ph.D. 2019?): Inclusiveness
- active learning, incrementa repair, streaming
- data labelling via very small samples
- infer laeblling trends (so you know when to stop)
- labelling error mitation (by sometomes relabelling old examples_

FAIRNESS Chakraborty (Ph.D. 2022?)
- hyperparamter optimzation and fairness

