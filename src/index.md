# Preface


## Questions (that need Answers)

![](img/questions.png){: .imgright}

What do AI developers need to know about software engineering? And what do SE need to know about AI?

Looking at recent high-impact industrial and  research results, 
three 
technologies 
that ready
for widespread use by more engineers are:

- data miners;
- optimizers; and 
- theorem provers 

When used together, these three technologies can greatly benefit each other.
Data miners can simplify optimizers. Optimizers can make theorem provers run faster.
And theorem provers can become generators for data mining.

The book introduces these technologies, from a programming perspective.
Our goal is to give you enough information so you can build, refactor, and improve  your own versions of these tools.

But more than than,
this book asks what is missing from most other textbooks on AI and SE.
To fill that gap,  we will cover:

- Software processes:
Software process is how large teams divide tasks such that more people can deliver more functionality, faster.
Software processes are vital to the scalability and maintainability of AI tools.
- Ethically-aligned design:
This is how match up high-level ethical goals (e.g. fairness, reliability, transparency, etc)  with
lower-level functionality (e.g. rule generation, anomaly detection, clustering, etc). 
As AI tools get used more and more,
such an ethical perspective on AI tools is becoming increasingly  important.

We assert that it is the ethical duty of anyone building
software   to produce software that conforms to accepted ethical standards.
This book discusses how that might be done
It turns out that many different can be fitted to data.
Each such model represents a trade between what we want and what we want to avoid.
As shown in this book,
using data miners and optimizers and theorem prover, we can select the kinds of models we want.
Hence we say that

- _Ethics_ are a choice;
- And
_not choosing is unethical_
since we are not
controlling 
what goals are not satisfied by that model.  

## Why Read This Book?

You should read this book, if you do not know how to build ethical AI software.
More specifically, if you do not know how to design AI tools
that can address the following, then this is the book for you:


2. How stable is the performance of your AI tool ?
1. Have you compared the effectiveness of your AI tools against other options?
3. Can you report the dx/dy of your AI tool (i.e. if we change inputs _X_,
   how does that effect the outputs _Y_)?
3. Using that dx/dy knowledge, can you optimize your software to ensure most effectiveness?
4. Using that optimizer, can your AI tools chase a wide range of business goals?
4. Do you have a continuous monitoring process in place to ensure AI tool effectiveness?
5. Do you have a continuous repair process in place to mitigate for poor performance?
6. Does your AI tools  run
  fast enough, not use excessive minimal system resources, to enable such comparisons, stability
tests, optimization
  monitoring, and repair?
7. Do your AI tools ship with a "certification envelope" (so that its users
   know when not to trust it)?
8. Are you testing if your AI tools are  being unfair to different social groups?
9. Is your AI tool transparent enough to allow detection of misue??
10. Are your AI tools  accountable (transparent, reliable, and safe)?
11. Do your AI tools  support inclusiveness for its user population?
12. Are your AI  your tools private and secure?


A score of 12 is perfect, 11 is tolerable, but 10 or lower and you
have got serious problems. The truth is that most software organizations 
are running with a score of 2 or 3, and they need serious help.
So if you AI tools can't or won't answer "yes"
to the most of the above then:

- Industrial practitioners should use different tools; and 
- Researchers should accept  a new  research challenge (how how to enable that kinds of ethics in that kind of AI tool).
   

[^foot]: These questions are inspired by Joel Spolsky's 12 step test for the quality of a software team.  His test has 12 questions: (1) Do you use source control?; (2) Can you make a build in one step?; (3) Do you make daily builds?; (4) Do you have a bug database?; (5) Do you fix bugs before writing new code?; (6) Do you have an up-to-date schedule?; (7) Do you have a spec?; (8) Do programmers have quiet working conditions?; (9)  Do you use the best tools money can buy?; (10) Do you have testers?; (11_ Do new candidates write code during their interview?; (12) Do you do hallway usability testing?

## Notes
