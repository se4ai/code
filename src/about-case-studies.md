# 4. Ethics : how

The premise of this book is that
AI tools contain many choices and, taken all together,
those,
choices
offer a rich tapestry of tools that software engineers can weave
 together to achieve a variety of goals. The good thing about that
is that as our tools offer us more
choices, they also offer us more ethical choices.

To show examples of that, first we need a working definition of "ethics".


## Working Definitions of Ethics

The  [Institute for Electronics and Electrical Engineers](/REFS#IEEEethics-2019) (IEEE)
have   discussed general principles for implementing autonomous and intelligent systems (A/IS).
They propose that the design of such A/IS systems
satisfy certain criteria:

1. _Human Rights:_ A/IS shall be created and operated to respect, promote, and protect internationally recognized human rights.
2. _Well-being:_ A/IS creators shall adopt increased human well-being as a primary success criterion for development.
3. _Data Agency:_ A/IS creators shall empower individuals with the ability to access
   and securely share their data, to maintain people’s capacity to have control over their identity.
4. _Effectiveness:_ A/IS creators and operators shall provide evidence of the effectiveness and fitness for purpose of A/IS.
5. _Transparency:_ The basis of a particular A/IS decision should always be discoverable.
6. _Accountability:_ A/IS shall be created and operated to provide
   an unambiguous rationale for all decisions made.
7. _Awareness of Misuse:_ A/IS creators shall guard against all potential misuses and risks of A/IS in operation.
8. _Competence:_ A/IS creators shall specify and operators shall adhere to the knowledge and
   skill required for safe and effective operation.

Other  organizations, like [Microsoft](/REFS.md#microai-2019)
offer their own principles for AI:

- _Transparency_ AI systems should be understandable
- _Fairness_: AI systems should treat all people fairly
- _Inclusiveness_  AI systems should empower everyone and engage people
- _Reliability &amp; Safety_ AI systems should perform reliably and safely
- _Privacy & Security_: AI systems should be secure and respect privacy
- _Accountability_: AI systems should have algorithmic accountability

The rest of this chapter shows how different algorithm choices let us
weave together the IEEE and Microsoft concerns. Before showing that, the obvious point
to make is that ethics is a rapidly evolving concept so the following "weaving" is somewhat
subjective. But to misquote George Box, all ideas are wrong; but some are useful. 
The reader might disagree with the following. You might believe that
we have missed, or 
missed out, or misrepresented,
some vital ethical concern.
In that case, the following is still useful since
at least our ideas have gotten you thinking abut ethics. In fact,
the best thing that could happen below is that you say "that is wrong; a better way to do that
would be..."

## From Ethics to Algorithms

Well being & Awareness of Misue    
- Fairness : 
    - See [Charaborty, 2019](REFS#chakrabory-2019).
- Relaibility & safety: 
    - via multi-goal reasoning (so you known how reliabilty you are satisfying the goals of different users of the ssytems),
    - see [Sayyad'13](REFS#sayyad-2013)
    - via certification envelope (see Peters13]
- Also helped by transparency
Transparencey: 
    -transparent makes users of a  system aware ot the use and misue of that ssytem
    - see explanation work [Feather'02]  [Menzies'07] [Gay'12] [Matheer'16]

Accountability:
- enabled by trasnparency and relaiblity abd safety

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

