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
- Tools that help here are rule-based learners and well as any AI tool that can quickly and easily and incrementally modify its knowledge
  (where "easy" means using only limited system resources and without complex pipelines).

<em>2. Have you compared the effectiveness of your AI tools against other options?</em>

- When commissioning an AI tool for   a new domain, some experimentation is required to match the right tool to the current data.
- Tools that help here are kits containing many algorithms, each of which is easy to install, fast to configure, and fast to run.
- Some statistical tools are required here as well (to simplify the statistical analysis and to produce succinct reports; e.g
  Scott-Knot).

<em>3. Can you report the dx/dy of your AI tool (i.e. if we change inputs _X_,
   how does that effect the outputs _Y_)?</em>

- We need to know the envelope within which important conclusions stay the same.
- We also need to know how to change things that are undesirable.
- Tools that help here are Monte Carlo rigs that can perturb  inputs across known ranges (or theorem provers
  that can generate a wide range of valid inputs). Also useful here  are data miners
  that can summarize how different independent variables (the inputs) lead to what dependent variables (the outputs).

<em>4. Using that dx/dy knowledge, can you optimize your software to ensure most effectiveness?</em>

- Tools that help here are optimizers that intelligently probe the _dx_ space to learn how to change _dy_
  (and which do so without exorbitantly  long run times).

<em>5. Using that optimizer, can your AI tools chase a wide range of business goals?</em>

- Optimizers/data miners should not be hard-wired to specific goals. Rather, they should accept as input
  the specific goals that the local business people want to achieve.
- Tools that help here are optimizers that can accept a wide range of goals (as part of their inputs). Also useful
  are multi-objective optimizers that can explore trade offs between multiple goals.

<em>6. Do you have a continuous monitoring process in place to ensure AI tool effectiveness?</em>

- We need to know when AI tools are going off the rails (performing poorly).
- Tools that are useful here are streaming AI tools (that incrementally modify themselves as new data arrives).

<em>7. Do you have a continuous repair process in place to mitigate for poor performance?</em>

- We need some kind of mitigation strategy that can manage less-than-desired AI tool performance.
- Tools that help here are multi-objective optimizers or contrast set learners that can report
  what differences in the independent variables  change the dependent variables.

<em>8. Does your AI tools  run
  fast enough, not use excessive minimal system resources, to enable such comparisons, stability
tests, optimization
  monitoring, and repair?</em>

- All the above should be achievable within the system constraints of the local environment.
- Tools that help here are fast clustering algorithms (that divide large problems into many smaller ones)
  and stochastic sampling methods that look at general patterns in subsets of the data.

<em>9. Do your AI tools ship with a "certification envelope" (so that its users
   know when not to trust it)?</em>

- AI tools should broadcast when they can be trusted, and when they should be suspected.
- Tools that help here are prototype learners  (so we only have to share representative examples of all the data),
  and data mutators (that help to  anonymize the shared data).

  co
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



