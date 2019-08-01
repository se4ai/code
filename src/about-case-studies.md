# Case Studies

There are three things to note about the following exmapels:

- They combine data minigna nd optimization and (in the case of Chen's work), theorem proving
- They all show that ethical goals can be achieved using AI tools.
- In the case of some of them, the trick was there are many possible models that fit that data,
  and many ways for those models to achieve many goals. By carefully selecting how the models
  are generated, we can select better models that achieve the goals we desire.

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

