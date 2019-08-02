# Manifesto

## Issues of Ethics

![](img/questions.png){: .imgright}

It is the ethical duty of anyone building
AI software   to produce tools  that conform to accepted ethical standards.
This book discusses how that might be done.

It is important, and timely, to take more time to talk about ethics.
The more society uses software to mediate its activities, and the more it uses 
artificial intelligence
to control that software, the more we need to consider the ethical implications 
 of those systems.

Happily, AI can help with ethics. 
Ethics is all about choice. Ethical principles guide the choices we make
and how we evaluate each choice.
When applying AI tools (such as data miners,
optimizers, or theorem provers), developers can make many choices:

- what goals are required;
- how to represent and apply domain knowledge
- what data to use 
- how to best weight  different examples or different attributes, 
- what algorithms  to apply for the learning;
- what optimizers to apply to better (e.g.) tune the learners;

To understand that, consider one view
of how AI converts data into conclusions:

```
data -> AI tool -> conclusion
```

This view is very misleading since it ignores all the choices inside AI tools
(and how those choices effect the resulting conclusions).
There are many ways that  AI can combine data and data miners and optimizers and theorem provers.
Each of these methods produces its own model,
only some of
which do we choose to apply[^choice]:

```
data -> AI tool --> |--> model1  \
        (control    |--> model2   \
       settings)    |--> model3    |--> choice --> model --> conclusion
                    |--> model4   /
                    |--> etc     /
```

[^choice]: This is not to say that AI just makes things up. While data may lead to multiple models, there are many models not supported by any data.  So one way to look at AI is a method to  quickly rule out was is definitely wrong (and then help us faster explore what is left).  As [Karl Popper](REFS#popper-1963) said, the ideas that we most believe are the ones that have survived the most attempts at refutation.  This view of science-as-refutation has a  long history.  Wolfgang Pauli was a prominent physics in the first half of the 20th century.  When reading a  paper of another physicist, he famously remarked "Das ist nicht nur nicht richtig; es ist nicht einmal falsch!" ( That's not just not right; it is not even wrong!).  


Each  model generated  by AI represents a trade between
what we want;
and what we want to avoid.
The key to ethical AI software is controlling what  choices are made during the software construction process. AI
technologies are unique in that, for the first time in human history, we can use AI to help us make those choices.
As shown in this book,
using data miners and optimizers and theorem provers, we can select the kinds of models we want.
Hence we say that

- _Ethics_ are a choice;
- And
_not choosing is unethical_
since we are not
controlling 
what goals are not satisfied by our AI tools.


To understand those choices, we need to understand more about the technologies used with AI tools.
When used together, 
data miners,
optimizers, and 
theorem provers
can greatly benefit each other.
Data miners can simplify optimizers. Optimizers can make theorem provers run faster.
Theorem provers can become generators for data mining.
But more importantly, each can be used to control the choices made by the other.
Also, when properly controlled, those choices can be made to achieve ethical goals.

The book introduces these technologies, from a programming perspective.
Our goal is to give you enough information so you can build, refactor, and improve  your own versions of these tools.

This book also asks what is missing from most other textbooks on AI and SE.
To fill that gap,  we will cover:

- Software processes:
Software process is how large teams divide tasks such that more people can deliver more functionality, faster.
Software processes are vital to the scalability and maintainability of AI tools.
- Ethically-aligned design:
This is how match up high-level ethical goals (e.g. fairness, reliability, transparency, etc)  with
lower-level functionality (e.g. rule generation, anomaly detection, clustering, etc). 

As we said before,
when you start a new AI project,
your  first question should not be  be  "what data miners should I apply to this data?".
Rather, it should be  "what are the ethical requirements of this development? And how can we best support those requirements?".


More and more, AI tools  are making decisions that affect people’s
lives in such high-stakes applications such as mortgage lending,
hiring, and prison sentencing. Many high-stake applications such
as finance, hiring, admissions, criminal justice use AI
decision-making
frequently[^ladd-1998],[^burrell-2016],[^corbett-2018],[^galindo-2000],[^yan-2013],[^chalfin-2016],[^ajit-2016],[^berk-2015],[^berk-2016].
Unfortunately, some of  AI tools are  known to exhibit “group
discrimination”; i.e. their decisions are inappropriately affected
attributes like race, gender, age, etc:

[^ladd-1998]:    [Ladd'98](/REFS#ladd-1998)
[^burrell-2016]: [Burrell'16](/REFS#burrell-2016)
[^corbett-2018]: [Corbett'18](/REFS#corbett-2018)
[^galindo-2000]: [Galindo'00](/REFS#galindo-2000)
[^yan-2013]:     [Yan'13](/REFS#yan-2013)
[^chalfin-2016]: [Chalfin'16](/REFS#chalfin-2016)
[^ajit-2016]:    [Ajit'16](/REFS#ajit-2016)
[^berk-2015]:    [Berk'15](/REFS#berk-2015)
[^berk-2016]:    [Berk'16](/REFS#berk-2016)


- One older version of a [sentiment analyzer from Google](/REFS.md#Google-2017) gave negative (and wildly
inappropriate) scores to sentences like 
"I am a Jew" and "I am homosexual".
- A popular photo tagging app assigned [animal category labels](/REFS.md#Google_Photo) to dark skinned people.
- Recidivism assessment models predict who might commit crimes, in the future. Some such models used by the criminal justice system are more likely to
[falsely label black defendants as future criminals](/REFS.md#Machine_Bias) (at twice the rate as white defendants).
- Facial recognition software which predicts characteristics such as gender, age from images has been found to have a
[much higher error rate](/REFS.md#skin-bias-2018) for dark-skinned women compared to light-skinned men
- Amazon.com stopped using automated recruiting tools after finding [anti-women bias](/REFS.md#Amazon_Bias).



We say that, to some degree, the ethical impact of AI tools can be controlled by the developers
building that software. We stress "to some degree" since the best ethical intentions
of any developer can be defeated by  malevolent forces, or even by just dumb luck.
So it is wrong to say that if our guileless are followed that the result AI tool will always adhere to 
socially-accepted ethical standards.

But it also wrong to say that just because some ethical goals are not always reached, that we should not strive towards
those goals.
Developers will always try to adhere to ethical standards.
Or, at the very least, they should monitor their AI tools and report unethical usage or consequences.

Many industrial practitioners and researchers agree that
we need
more
ethically-aligned design.
Not only that, buy they note that ethical issues are  something software engineers encounter on a daily basis.
For example,
at the recent
Fairware 2018 workshop, Fatma Aydemir and Fabiano Dalpiaz
[listed numerous ethical issues](/REFS.md#aydemir-2018) listed ethical concerns faced by
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

When discussing this work with colleagues, we are still sometimes
asked if ethical issues _should_
or _can_ be solved by 
software engineers. We reply that:

- It _should_ be the goal of  software developers to ensure
that software conforms to  its
required ethical standards.
- Further, even if we think that  ethics is not our
problem, our users may disagree.
When users discover problems with software, it is the job of
the person maintaining that software (i.e.  a software engineer) to fix that problem.
- Lastly, we also think that this problem _can_ be solved by software engineers. 
For example _Hyperparameter  optimization_ 
is now widely applied in SE (see [Xia'18](/REFS#xia-2018) and [Osman'17](/REFS#osman-2017)),
That kind of optimizers
selects the model we want from the large space of possible models.
That is, methods that have matured within the SE community (by SE researchers and practitioners),
can now be applied to other problems (e.g.  as discussed later in this book, how to  mitigate unfair software).


## Notes
