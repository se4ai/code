# Manifesto

## Issues of Ethics

![](img/questions.png){: .imgright}

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


- One older version of a [sentiment analyzer from Google](/REFS.md#Google-2017) gave negative score to sentences like I am a Jew and I am homosexual.
- A popular photo tagging app assigned [animal category labels](/REFS.md#Google_Photo) to dark skinned people.
- Recidivism assessment models predict who might commit crimes, in the future. Some such models used by the criminal justice system are more likely to
[falsely label black defendants as future criminals](/REFS.md#Machine_Bias) (at twice the rate as white defendants).
- Facial recognition software which predicts characteristics such as gender, age from images has been found to have a
[much higher error rate](/REFS.md#skin-bias-2018) for dark-skinned women compared to light-skinned men
- Amazon.com stopped using automated recruiting tools after finding [anti-women bias](/REFS.md#Amazon_Bias).



We say that, to some degree, the ethical impact of AI tools can be controlled by the developers
building that software. We stress "to some degree" since the best intentions
of any developer can be defeated by  malevolent forces, or even by just dumb luck.
So it is wrong to say that if our guileless are followed that the result AI tool will always adhere to 
socially-accepted ethical standards.

But it also wrong to say that just because some ethical goals are not always reached, that we should not strive towards
those goals.
Developers will always try to adhere to ethicals standards.
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


## Testing For "Ethical" Software

Once upon a time, back in the year 2000, Joel Spolsky proofed 12 tests for
the quality of a software team[^foot].  This test was widely influential in the agile community. 

[^foot]: (1) Do you use source control?; (2) Can you make a build in one step?; (3) Do you make daily builds?; (4) Do you have a bug database?; (5) Do you fix bugs before writing new code?; (6) Do you have an up-to-date schedule?; (7) Do you have a spec?; (8) Do programmers have quiet working conditions?; (9)  Do you use the best tools money can buy?; (10) Do you have testers?; (11) Do new candidates write code during their interview?; (12) Do you do hallway usability testing?

Now, two decades later, we demand more of our software (particularly of our AI software). Here are some other questions
we now want to ask about our software.  Include below are some methods could be used to address these questions
(and it is an open research issue if there are other, better, ways to address these concerns). 
If you AI tools can't or won't answer "yes"
to the most of the above then:

- Industrial practitioners should use different tools; and 
- Researchers should accept  a new  research challenge (how how to enable that kinds of ethics in that kind of AI tool).


<em>1. How stable are the  conclusions from  your AI tool ?</em>

- The conclusions from an AI tools should be succinct enough to inspect and understand. Stability should
be tested across multiple random samples of the training data as well as over time (as new data arrives).

<em>2. Have you compared the effectiveness of your AI tools against other options?</em>

- When commissioning an AI tool for   a new domain, some experimentation is required to match the right tool to the current data.

<em>3. Can you report the dx/dy of your AI tool (i.e. if we change inputs _X_,
   how does that effect the outputs _Y_)?</em>

- We need to know the envelope within which important conclusions stay the same.
- We also need to know how to change things that are undesirable.

<em>4. Using that dx/dy knowledge, can you optimize your software to ensure most effectiveness?</em>

- AI tools include an optimizer that can intelligently explore the state space of your AI tool?

<em>5. Using that optimizer, can your AI tools chase a wide range of business goals?</em>

- Optimizers/data miners should not be hard-wired to specific goals. Rather, they should accept as input
  the specific goals that the local business people want to achieve.

<em>6. Do you have a continuous monitoring process in place to ensure AI tool effectiveness?</em>

- We need to know when AI tools are going off the rails (performing poorly).

<em>7. Do you have a continuous repair process in place to mitigate for poor performance?</em>

- We need some kind of mitigation strategy that can manage less-than-desired AI tool performance.

<em>8. Does your AI tools  run
  fast enough, not use excessive minimal system resources, to enable such comparisons, stability
tests, optimization
  monitoring, and repair?</em>

- All the above should be achievable within the system constraints of the local environment.

<em>9. Do your AI tools ship with a "certification envelope" (so that its users
   know when not to trust it)?</em>

- AI tools should broadcast when they can be trusted, and when they should be suspected.

<em>10. Are you testing if your AI tools are  being unfair to different social groups?</em>

- Fairness can be seen in the different  responses of your AI tools to
social groups
  marked by protected attributes (e.g. age, race , gender).
  Sometimes, it is required to use these protected attributes in a
 model (e.g. certain genders are a very good predictor for "not
  pregnant"). But at other times, it is optional to use 
  protected  attributes,
as apposed to some other parts of the data. At those times, 
  it is at least polite (and at most illegal) to report models that places special emphasis  on these protected attributes.


<em>11. Is your AI tool transparent enough to allow detection of misue?</em>

- One way to increase the odds of misuse of any system is it make it harder for someone to audit that system.

<em>12. Are your AI tools  accountable (transparent, reliable, and safe)?</em>

- Unsafe and unreliable software can fail, hurting people as it does so.

<em>13. Do your AI tools  support inclusiveness for its user population?</em>

- For users that want to lean in and participate in the creation and maintenance of an AI tool, can that tool
  report itself succinctly enough to allows humans to watch, understand, and change that system?

<em>14. Are your AI  your tools private and secure?</em>

- The less private and the less secure the system, the greater the odds of misuse.


## Notes
