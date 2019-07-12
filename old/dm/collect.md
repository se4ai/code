---
title: Data Collection
layout: dm
---

## Cheats gude to data (from the recommendaation book)

## Suspect your data


## Live with the data yu have


## REspect Priacy during colelction

111

ounce of knowldge ugudies colelction the spike example of how to focust ehe data colelction  



https://link-springer-com.prox.lib.ncsu.edu/chapter/10.1007/978-3-642-55035-5_18

This chapter argues that modeling is simple—if we prune away superfluous details. It turns out that this is a very old idea (even though, until very recently, there was little tool support for this approach). William of Ockham (c. 1287–1347) proposed Occam’s Razor, which is a principle of parsimony for problem-solving. It states that among competing hypotheses the one with the fewest assumptions should be selected. To put that another way: (1) Prune the unnecessary and (2) focus on what remains.

It turns out that Occam’s Razor is a core principle of cognitive psychology. In the early 1980s, Jill Larkin and her colleagues explained human expertise in terms of a long-term memory of possibilities and a short-term memory for the things we are currently considering (Larkin et al. 1980):
Novices confuse themselves by overloading their short-term memory. They run so many “what-if” queries that their short-term memory chokes and dies.
Experts, on the other hand, only reason about the things that matter so their short-term memories have space for conclusions.
The exact details of how this is done are quite technical, but the main lesson is clear: Experts are experts since they know what to ignore. Larkin et al. offered numerous examples of this effect. Novices performed badly when they confused themselves with too many options. Also, experts performed better since they could clear their short-term memory of all but essential features (Larkin et al. 1980).

Occam’s Razor has obvious business implications. For one thing, we can build very simple decision-support systems:
In 1916, Henri said that managers plan, organize, coordinate, and control. In that view, managers systematically assess all relevant factors to generate some optimum plan (Fayol 1916)
Then in the 1960s, computers were used to automatically and routinely generate the information needed for the Fayol model. This was the era of the management information system (MIS), where thick wads of paper were routinely filed in the trash can (Ackoff 1967)
In 1975, Mintzberg’s classic empirical fly-on-the-wall tracking of managers in the day-to-day work demonstrated that the Fayol model was normative, rather than descriptive. For example, Mintzberg found 56 US foreman who averaged 583 activities in an 8-h shift (one every 48 s). Another study of 160 British middle and top managers found that they worked for half an hour or more without interruption only once every 2 days (Mintzberg 1975)
The lesson of MIS is that management decision-making is not inhibited by a lack of information. Rather, according to Ackoff, it is confused by an excess of irrelevant information (Ackoff 1967). This was true in the 1960s and now, in the age of the Internet, this problem has become particularly acute. As Mitch Kapor said in his famous quote, “Getting information off the Internet is like taking a drink from a fire hydrant.”

Further, the lesson of Mintzberg’s study is that it is vitally important to give managers succinct summaries of their available actions since, given their work pressures, they just cannot digest long and overly complex ideas. Too much data can overload a decision maker with too many irrelevancies. Data must be condensed before it is useful for supporting decisions. Modern decision-support systems evolved to filter useless information to deliver small amounts of relevant information (a subset of all information) to the manager. Hence, Occam’s Razor.


As mentioned above, one lesson from the 1960s obsession with management information system (MIS) was that project managers can be overloaded with too much information (Ackoff 1967). Therefore, the wise decision analyst seeks the smallest amount of the most important information. The lesson of this chapter is that, using some data mining tools, this smallest amount may be very small indeed (Chang 1974; Olvera-López et al. 2010; Kohavi and John 1997; Hall and Holmes 2003; Menzies and Hu 2003, 2007; Geletko and Menzies 2003; Menzies et al. 2012; Gay et al. 2010).

Consider a table of data with rows and columns where each row is one example instance about something (e.g., a software project) and each column is one thing we can measure about that instance. A repeated result is that:
After instance selection, most of the rows can be ignored: If a model can be learned from rows of data, it follows that those rows are multiple copies of some underlying effect. Hence, rows of data can usually be reduced to just a few prototypes that most exemplify the underlying model. Such row selection algorithms also serve to remove very similar (or repeated) rows, or noisy rows that can confuse model generation (Chang 1974; Olvera-López et al. 2010; Menzies et al. 2012). Experiments on the reduced row set show that predictive performance can be just as good as with the full set [especially when row pruning avoids outliers and other noisy examples (Menzies et al. 2012)].
After column selection, most of the columns can be ignored: Feature subset selection algorithms test what columns can be removed without damaging the signal in the data. In the usual case, dozens of columns can be reduced to just a few. This process removes (a) noisy columns; or (b) columns that are irrelevant to the prediction task at hand; or (c) columns that are redundant (since they are similar to other columns in the data) (Kohavi and John 1997; Hall and Holmes 2003).
After range selection, most variable ranges can be ignored: A “contrast set” is the delta between two populations. Minimal contrast sets can be formed by listing the ranges that are more common in some preferred population. Such minimal contrast sets can be very small, even between complex concepts. For example, it may require gigabytes of gene sequencing to list all the properties of human and ape DNA. But one of those two species can talk and the other cannot. Hence, a contrast set between these two complex entities might be one simple test (e.g., can they say their name?). Any variable range not in a contrast set is not something that can select one population over another; hence, in terms of offering actionable analytics, they can be ignored (Menzies and Hu 2003, 2007; Geletko and Menzies 2003; Gay et al. 2010).
These three pruning rules can dramatically simplify a model.

As an example of the impact of range pruning, previously we have discussed how contrast sets can simplify seemingly very complex models. In one case, we explored a data set that had generated a 6,000-node decision tree. The same data yielded four contrast sets with 2–5 attributes—which were small enough to show on one-eighth of a page (whereas the original decision tree filled 100 pages) (Menzies and Sinsel 2000).
As an example of the impact of column and row pruning, with Kocaguenli, we have explored tables of software effort data. In experiments with 681 projects from 19 different data sets, we found that in each data set, we could ignore most of that data (Kocaguneli et al. 2013a, b). Specifically, within the rows, 36–84 % of them can be pruned and within the columns, 17–83 % of them can be pruned. After pruning we were usually left with just 11 % of the cells in the original data tables. Further, when we used all of the pruned data, there was very little difference in our ability to predict the effort required to build software (Kocaguneli et al. 2013a, b).
An interesting feature of the second result is that it did not need all the data to do its pruning. Kocaguenli’s method understands the cost curve associated with collecting different features. To exploit that knowledge, they first run queries on the cheaper features. Next, for the more expensive features, they only ask for least number of values that are most informative. For example:
