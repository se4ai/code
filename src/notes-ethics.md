# Ethically-aligned Design

XXX lime. Limits. Domain goals, cluster, local rule learning.

It is the duty of anyone building software
to strive to deliver software that is ethically acceptable. 
When you start a new AI project, perhaps the 
first question should not be be "what data miners should I apply to this data?". Rather, it is better to ask:

- What are the ethical requirements of this development?
- And how can we best support those requirements?.

There is much current interest in 
[ethics and software engineering](/REFS.md#brun-2018)  exploring this issues. For example,
at the recent
Fairware 2018 workshop, Fatma Aydemir and Fabiano Dalpiaz
[listed numerous ethical issues](/REFS.md#aydemir-2018) faced by
software engineers in their day-to-day work:

- _Privacy_: Handling, storing, sharing user data only under the circumstances and for the purposes that the user sets
- _Sustainability_: Energy consumption of the software artifact, caring about energy throughout the SE process and in the documentation
- _Transparency_: Transparent decision-making procedures of intelligent systems, publicly available ethics policies by software development organizations
- _Diversity_: Gender, race, and age distribution of professionals in a development team
- _Work ethics_: Decisions on which bugs to fix and how quickly, ensuring quality of the code before release
- _Business ethics_: Informing users of a changed business model, including revenue models
- _Accountability_: Who should be held responsible for the harm caused by software?
- _Dependability_: Decision to maintain and/or keep a software product in the market
- _Common goods_: Contributing to, using, promoting open source software

If anyone doubts that ethics is an SE concern, then it be noted that:

- The authors of this book assert that it is the goal of software
  developers to ensure that software conforms to its required ethical
  standards.
- Even if you  think that (fairness is not your problem), your users
  may disagree. When users discover problems with software, it is the
  job of the person maintaining that software (i.e. a software engineer)
  to fix that problem.
- To some extent, issues of ethics can be managed by software design.
  As shown in this book, there are design patterns and algorithms
  could lead to more ethical software. That is, ethics is a design
  issue that _could be_ addressed like any other design problem

As we warned in the introduction, _could be ethical_ is very different
to _is ethical_. Even the best designed system can be maliciously
or accidentally used in an unethical way. Nevertheless, the easier
it is to build ethical systems, the more likely they will get
created. Also, even if the tools of this book do not fully address
ethical issues, it is still very valuable to demand that software
engineers think very hard about the ethics of their system.


## Why is Ethics so Important for AI Systems?

Two common uses of AI tools is the creation of autonomous agents
that:

- Show us "what is" inside data. We need such "what is" agents since
many data sources are too complex or too large for humans to fully
understand.

- Tell us "what to do"; i.e what actions we could do (or what actions
we are allowed to do). For example, privacy settings on a cloud-based
application dictate what functions and data are accessible by a
user.

When these AI tools are implemented using data miners, there is
always discrimination. By their very nature, these algorithms are
discriminatory in that they learn to discriminate one set of results
from another. This discrimination becomes objectionable when it
places certain social groups at a systematic advantage and other
unprivileged groups at a systematic disadvantage. In some situations,
such as employment (hiring and firing), discrimination is not only
objectionable, but illegal.

It is timely to reflect on the implications of such discrimination.
More and more, software is making decisions that affect people’s
lives in such high-stakes applications such as mortgage lending,
hiring, and prison sentencing. Many high-stake applications such
as finance, hiring, admissions, criminal justice use algorithmic
decision-making
frequently[^ladd-1998],[^burrell-2016],[^corbett-2018],[^galindo-2000],[^yan-2013],[^chalfin-2016],[^ajit-2016],[^berk-2015],[^berk-2016].
Unfortunately, some of that software is known to exhibit “group
discrimination”; i.e. their decisions are inappropriately affected
attributes like race, gender, age, etc:

[^ladd-1998]:    /REFS.md#ladd-1998
[^burrell-2016]: /REFS.md#burrell-2016
[^corbett-2018]: /REFS.md#corbett-2018
[^galindo-2000]: /REFS.md#galindo-2000
[^yan-2013]:     /REFS.md#yan-2013
[^chalfin-2016]: /REFS.md#chalfin-2016
[^ajit-2016]:    /REFS.md#ajit-2016
[^berk-2015]:    /REFS.md#berk-2015
[^berk-2016]:    /REFS.md#berk-2016


- One older version of a [sentiment analyzer from Google](/REFS.md#Google-2017) gave negative score to sentences like I am a Jew and I am homosexual.
- A popular photo tagging app assigned [animal category labels](/REFS.md#Google_Photo) to dark skinned people.
- Recidivism assessment models predict who might commit crimes, in the future. Some such models used by the criminal justice system are more likely to 
[falsely label black defendants as future criminals](/REFS.md#Machine_Bias) (at twice the rate as white defendants).
- Facial recognition software which predicts characteristics such as gender, age from images has been found to have a 
[much higher error rate](/REFS.md#skin-bias-2018) for dark-skinned women compared to light-skinned men
- Amazon.com stopped using automated recruiting tools after finding [anti-women bias](/REFS.md#Amazon_Bias).

## Current Definitions of "Ethics"


Recently, many organizations like [Microsoft](/REFS.md#microai-2019)
 and the  [Institute for Electronics and Electrical Engineers](/REFS#IEEEethics-2019) (IEEE)
have  discussed general principles for implementing autonomous and intelligent systems (A/IS).
The IEEE makes the following points about A/IS:

1. Human Rights: A/IS shall be created and operated to respect, promote, and protect internationally recognized human rights.
2. Well-being: A/IS creators shall adopt increased human well-being as a primary success criterion for development.
3. Data Agency: A/IS creators shall empower individuals with the ability to access 
   and securely share their data, to maintain people’s capacity to have control over their identity.
4. Effectiveness: A/IS creators and operators shall provide evidence of the effectiveness and fitness for purpose of A/IS.
5. Transparency: The basis of a particular A/IS decision should always be discoverable.
6. Accountability: A/IS shall be created and operated to provide
   an unambiguous rationale for all decisions made.  
7. Awareness of Misuse: A/IS creators shall guard against all potential misuses and risks of A/IS in operation.  
8. Competence: A/IS creators shall specify and operators shall adhere to the knowledge and 
   skill required for safe and effective operation.

All these points are important, albeit a little hard to operationalize.
For example, the last point talks more about the developers than
the developed software.  Microsoft offers its own Another list of
principles, this time from Microsoft,  is perhaps more operational:

<ol type="a">
<li z=a> Transparency: AI systems should be understandable:
<li z=b> Fairness: AI systems should treat all people fairly
<li z=c> Inclusiveness: AI systems should empower everyone and engage people
<li z=d> Reliability &amp; Safety: AI systems should perform reliably and safely
<li z=e> Privacy & Security: AI systems should be secure and respect privacy
<li z=f> Accountability:AI systems should have algorithmic accountability
</ol>

One way to map these two lists together is as follows
(where the IEEE and Microsoft principles are shown in the rows and  columns, respectively). 

|                | a=Transparency | b=Fairness | c=Inclusiveness | d=Rel/Safety | e=Priv/Secure | f=Accountability |
|----------------|----------------|------------|-----------------|--------------|---------------|------------------|
| 1=Human Rights |                |  &#10004;  |     &#10004;    |  &#10004;    | &#10004;      |                  |
| 2=Well-being   |                |  &#10004;  |                 |  &#10004;    |               |                  |
|3=Data Agency   |                |            |     &#10004;    |              | &#10004;      |                  |
|4=Effectiveness |                |            |                 |  &#10004;    | &#10004;      |  &#10004;        |
|5=Transparency  |   &#10004;     |  &#10004;  |                 |              |               |                  |
|6=Accountability|   &#10004;     |  &#10004;  |                 |  &#10004;    |               |  &#10004;        |
|7=AwareOfMisuse |                |  &#10004;  |                 |  &#10004;    |               |                  |
|8=Competence    |                |            |                 |              |               |                  |

**Table 1: Ethical principles from IEEE and Microsoft**{: style="text-align: center"}

The above table is hardly definitive since many of these concepts are being rapidly evolved.
One way to assist in the evolution of these concepts is to define them use discrete maths; i.e. using data structures
and algorithms-- which is the point of the rest of this chapter. 

## Design Details

Before committing to a particular design, it is important to make the following point. The following is
**one** way, but not **the only** way, to design for ethical AI.
The aim of the following is to get software engineers thinking about how to better design their systems.
So a  perfect reaction to the following would be:

- "Hey! there's a better way to do this!"
- or "This code does not handle ABC so I propose DEF".

### Accountability, Transparency, Competency   need Explanations

The principle of _accountability_ requires that users of software
can demand an _explanation_ of why software is doing what it does.
Consider, the situation where some new AI software is installed to
control the traffic signals along  a road in front of a set of
shops.  Suppose those signals cause a change in traffic patterns:

- Those new AI controller might may lead to gridlock. In that case, drivers should be able to ask why that is happening.
- Those signals may also lead to the cars moving so fast, that none dare slow down and turn into the shops.
  In that case, the shopkeepers should be able to understand why that is happening.

Note that one aspect of such accountability is _repair_. That is,
if you do not like the answers that an AI system is giving you,
then there needs to be some way of adjusting those answers.

Another reason to implement an explanation system  is _transparency_
and _competency_.  Consider the following  five common software
tasks: construction (of the original system); testing; fixing;
certification; and maintenance.  All these five tasks are made simpler
by software that  can explain its internal workings.  That is,
software _competency_  is greatly assisted by transparency.  For
this reason, modern software development environments come with
many transparency tools such as tracing, breakpoints, code search,
extensive test suites, code summarization tools, etc. For AI tools,
those transparency tools need to be augmented with ways to discover
and understand by decisions are being made.

Yet another reason to endorse transparency is
that
criminal behavior is more likely when criminals  think they will not get caught. Hence, the
easier it is to understand and audit a system, the less  
likely it is that there will be
fraud and malfeasance.

But does every system need an explanation system?  Perhaps not.
The obvious counter-argument is that if no human ever needs to
understand the AI tool,   then it does not need to be transparent.
For example, a neural net could control the carburetor of an internal
combustion engine since that carburetor will never dispute the model
or ask for clarification of any of its reasoning.
On the other hand, if an AI model is to be used to persuade humans
to change what they are doing, it needs to be comprehensible
so humans can debate the merits of its conclusions. Returning
to the carburetor example, if there is some debate on how best
to change the carburetor's software (e.g. during debugging or upgrading),
then engineers will need to open up the carburetor's  black box to understand how it works
(and how best it can be changed). 

More generally,
many people argue that
that AI tools models needs to be expressed in a
simple way that is easy for practitioners to
[interpret](/REFs.md#dam-2019). According to [Miryung Kthaniel D Phillipsuim and her
colleagues](/REFS.md#kim-2106), AI tools for software analytics aim to obtain
actionable insights from software artifacts that help practitioners
accomplish tasks related to software development, systems, and
users.  [Other researchers](/REFS.md#tan-2016) argue that for
software vendors, managers, developers and users, such comprehensible
insights are the core deliverable of software analytics.  [Robert
Sawyer](/REFS.md#sawyer-2103) comments that actionable insight is
the key driver for businesses to invest in data analytics initiatives.

Accordingly, much research focuses on the generation of simple
models, or making "black box" models more explainable, so that human
engineers can understand and appropriately trust the decisions made
by [software analytics models](/REFS.md#abdollahi-2016). If a model
is not comprehensible, there are some explanation algorithms that
might mitigate that problem. For example:

-  In secondary learning, the examples given
to a neural network are used to [train a rule-based learner](/REFS.md#craven-2013)
and those
learners could be said to "explain" the neural net. 
- Another secondary learner is LIME that builds a model in the local neighborhood of a particular
example in order to explain why an AI model made particular decisions about that example.
- In
contrast set learning for instance-based reasoning, data is clustered
and users are shown the difference between 
[a few exemplars selected from each cluster](/REFS.md#krishna-2015).

Such explanation facilities are post-processors
to the original learning method. An alternative simpler approach
would be to use learners that generate comprehensible models in
the first place. 
One such approach is FFtrees.

The premise of FFtrees is that if you are going to explain something to someone,
you had best do that in a  form that that easily accommodate inside their own memory.
One way to do that is offer explanations in the form of many tiny rules.
Psychological theorists note that human memory is often organized around a large number of such simple rules,
also called heuristics. Such heuristics may not be general principles. In fact, usually, they are highly
context-specific constructs. But even then, they are very useful. For example,
suppose one of the authors of this book had a heart attack. If that were to happen, we would
ask that we not be taken to the local maths department where they would try to diagnose us from first principles.
Instead, we would ask that you take us to the local hospital where dozens of medical professionals have spent
decades learning  large number of heuristics on how to treat people like us using drugs and machines like what
they have locally available[^fifth].

[^fifth]: example adapted from [Edward Feigenbaum](/REFS.md#Feigenbaum-1983).

[Jill Larkin and her colleagues](/REFS.md#larkin-1980) characterize
human expertise in terms of very small short term memory, or STM
(used as a temporary scratch pad for current observation) and a
very large long term memory, or LTM. The LTM holds separate tiny
rule fragments that explore the contents of STM to say “when you
see THIS, do THAT”. When an LTM rule triggers, its consequence can
rewrite STM contents which, in turn, can trigger other rules.  The
STM is very small (perhaps just  four to seven items[^ma]).  Novices
perform worse than experts, says Larkin, when they fill up their
STM with too many to-do’s where they plan to pause and reflect on
what to do next.  Further, experts are experts, says Larkin because
their LTM  patterns dictate what to do, without needing to pause
for reflection.  Since, experts post far fewer to-do’s in their
STMs, they complete their tasks faster because (a) they are less
encumbered by excessive reflection and (b) there is more space in
their STM to reason about new information.
For example,
[Nathaniel Phillips](/REFS.md#phillips-2017)
 and his colleagues  discuss how models containing tiny rule fragments can be quickly comprehended by
doctors in emergency rooms making rapid decisions; or by soldiers on guard making snap decisions about whether to fire or not on a potential enemy; or by stockbrokers making instant decisions about buying or selling stock. 

[^ma]: Recently, [Wei Ma and colleagues](/REFS.md#ma-1024) used
evidence from neuroscience and functional MRIs to argue that STM
capacity might be better measured using other factors than "number
of items". But even they concede that "the concept of a limited
(STM) has considerable explanatory power for behavioral data".


In summary, according to Larkin and Phillips and their colleagues, 
  humans best understand some thing:

- When they can _write_ that thing into their memory; i.e., when that thing comprises many small rule fragments;
- Further, having an expert-level comprehension of some domain means having rules that can very quickly _applied_
to reach  a decision, without clogging up memory.


There are many ways to implement 

That is, such transparency reduces the odds of criminal behavior.

Also, from an ethical 

explain:
volumes, not points
rule-based
Local models (inferring irrelevancies)

repair:
Reweight the rows, reqeughet to columns, 
Patch

XXX is this the only way yo genra an explanation? Of course note. Leake 1991 advises that explanations
are an inference process that needs to be tuned to the goals and background knowledge of the audience.
In FFtrees, we use user goals to control discretization. and if we know the contepts famialr to
the audoece,we might restrict the rule learning to jsut those attributes. e.g. rahul's just tused hte changing attributes
And other audiences like maths. and sometimes aninformative visuslaization is enough.
So all we are saying above is hat we have **one**way, not **the way** to make an exalantion.


AI systems should be understandable
E.g. models as tiny trees or the LIME instance-based explanainer
Privacy & Security


AI systems should be secure and respect privacy


E.g. using a tree model or knowledge of the hyper boundary between instances of different classes, prune most rows. THen mutate the rest so as to not cross the boundary.
Accountability
AI systems should have algorithmic accountability


Hyperparameter optimization (HO) can demonstrate that the right settings are being used for the learners. When implemented naively, HO is slow. But instance-based or tree-based methods can significantly simplify HO.
Fairness
AI systems should treat all people fairly


In our view, fairness is a hyperparameter optimization issue where the learner is tuned (using the tree-based or instance-based methods of the previous row) for multiple goals including the standard fairness measures
Inclusiveness
AI systems should empower everyone and engage people


Our tree-based or instance-based semi-supervised methods can incrementally explore data, showing users the most informative examples. In our experiments, humans need explore less than 15% of the corpus to find useful models.
Reliability & Safety
AI systems should perform reliably and  
In our view, reliability is a statement of incrementally learning from examples and reporting the growth curves in model performance. This can be done using the methods of the previous row 14


### Transparency

many ways to explain things. eg. visually

explanation needed for debugging, accoutanability, reduce ods of freadualtna tbheavior
(cause f the system's reasoning is opaque then the it is easier to hide fraud or 
malfeasance

Ethtical software must  explain how it  makes its own conclusions since, otherwise,
humans cannot check the decisions of the system against their own expecations.


XXXX note that after transparancey comes accountability. If a system explains its internal reasoning,
and you disagree with those conclusions, there has to be some way to adjust the system. Such adjustments raises
numerous interesting issues, especially when the system is being used by a group of people, each with different
hopes and goals for the system. XXX.


```
users --> [have] --> goals --> [alter] --> conclusions


```
### Fairness

<p align="center">
  <img  src="img/curve_fitting.png">
</p>

**Source: XKCD https://xkcd.com/2048/**{: style="text-align: center"}

Models built by machine learners can exhibit "group discrimination"; i.e.  their decisions can system-atically disadvantage certain social groups (e.g.  those defined by race,  gender,  age,  etc.).  We diagnosisthe  problem  as  follows:if fairness is not known to be a goal,  thenlearning may neglect to generatefair models.  To fix this we can move the fairness goal into the model generation process.  Specifically, weusehyperparameter optimizationto find tunings for learners such that find fairer models. 

One way to use that experience in order to build fairer models ishyperparameter optimization. Hyperparam-eter optimizers explore a learner’s control parameters to find settings that produce models which bettersatisfy particular goals.  As shown by experiments presented later in this proposal, it is possible for suchtuning to find fairer models (where “fair” is determined by measures like those presented in §2.2). Hencewe  sayfairness is a choicesince  data  scientists  can  choose  whether  or  not  to  utilize  hyperparameteroptimization  to  ensure  fairness.   But  we  also  say  thatnot choosing is unfairsince  (a)  hyperparameteroptimizers must reject many candidate models before they find fair ones so (b) if a data scientist stopschoosing  and  just  uses  (say)  the  off-the-shelf  defaults  of  a  learner,  then  it  is  most  likely  they  will  beselecting an unfair model

### 
## Exercises

1. Check the mapping in Table1 between the Microsoft and IEEE ethical principles? Do you agree with that mapping?
2. In your opinion, what is missing from the rows and columns of Table1? Briefly define your new rows and columns.
3. One reason to define ideas (like ethics) in terms of data structures and algorithms is that that this lets
us also define (a) computational bottlenecks with those ideas; (b) areas that need further research. What are the computational
bottlenecks, areas that need extension, in the above?


 Transparency AI systems should be understandable
See above. Fast and frugal trees, designed for readability. Privacy
& Security AI systems should be secure and respect privacy See
above. Privacy = Feature+row reduction + mutation. Accountability
AI systems should have algorithmic accountability See above.
Accountability = hyperparameter optimization= can defend design
choices Fairness AI systems should treat all people fairly ASE’19
(submitted): can optimize for fairness, if we can run a learner,
many times Inclusiveness AI systems should empower everyone and
engage people EMSE’19: FASTEAD Incremental active learning: humans
critique, improve last conclusion https://arxiv.org/abs/1612.03224
Reliability & Safety AI systems should perform reliably and safely
Incremental active learners can guesstimate remaining inferences
