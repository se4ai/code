---
title: Model Requirements
layout: dm 
---

## Summary for this Chapter

- Consider givig up before you start
- Oceans, fish, fisherfol, hooks, markets: five rules of thumbs for assessing the viability of a machine learning project.
- The best metrics takes weeeks to uncover, and are obvious (in retrospect).
- Accuracy isn't accurate (sometimes)
- Precision isn't precise (sometimes)

## The Big Ideas

### Domain Familiarization

Consider stopping

- Oceans: is this area worthy?
- Fish: is there data?
- Fisherfolk: is the team skilled?
- Hooks: are their tools ready?
- Markets: if we catch anything, will anyone buy it?  In the current environment is anyone spending money on changing “it”?  Case study: test case prioritization. save millions of dollans a year. and the oroganization didn't care.


### Before Starting

Talk a little : surveys/ card sorts, double labelling


### Coordination Plan

what other teams need to know about what you are doing?

what are you talking to? Who do you need to talk to? why would they want to talk to you? The case of the displaced expert

### Goal enginering

How many goals? How many compete?
Is this even a data mining problem? (use optimizers?)
Some goals are impossible (e.g. pi=3)
Your data laughs at your goals
After “what is” comes “what to change”. Need a planner
Reference: David Lo, ICSME’17


### Goals

my goals aren'y your goals.

profit per meeter per day. critical success emtrics. weeks to find. obvious in retrospect.

horses for courses: goals change everything

reality

goals-ish

Transparency
AI systems should be understandable
See above. Fast and frugal trees, designed for readability.
Privacy & Security
AI systems should be secure and respect privacy
See above. Privacy =  Feature+row reduction + mutation.
Accountability
AI systems should have algorithmic accountability
See above. Accountability = hyperparameter optimization= can defend design choices
Fairness
AI systems should treat all people fairly
ASE’19 (submitted):  can optimize for fairness, if we can run a learner, many times
Inclusiveness
AI systems should empower everyone and engage people
EMSE’19: FASTEAD Incremental active learning: humans critique, improve last conclusion
https://arxiv.org/abs/1612.03224
Reliability & Safety
AI systems should perform reliably and safely
Incremental active learners can guesstimate remaining inferences

Some goals are unlreaiable'

### Goals change everythong

If goal = transparency, then select model wisely
Chen et al. ASE’19?.  Predicting  Breakdowns in Cloud Services (with SPIKE). https://arxiv.org/pdf/1905.06390.pdf 

If goal is insight then that effects chocie of learners

Our goals are business-dependent.
No “best” goal


### Funding

### Staffing Tips

Match goals to staff.

2 data engieners per one data scientist (the xbox example)

### Diverse Staff

[Mirying Kim and others](/refs#Kim17) have explored, we haveTom's Menergaie of pe


### Ethics

#### Human Rights

- The right to say no
- The right to be forgotten
- The roght to privacy
- The right of access

#### Privacy


#### Security

#### Fairness


## The Details


ABCD,
maths

whe the goal is predicting some symbolic concept: acc, pre, pd, pd, popt20

mre mmre medre pred(30)


Accuracy isn't accurate (sometomes)

Precision isn't precise (sometimes)

Pareto frontier
- boolean domination
- continuous domination

V.fast Literature Reviews
