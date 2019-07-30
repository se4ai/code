# Preface

As AI tools get used more and more,
it is vitally important to have an ethical perspective on AI tool development.
We assert that
it is the ethical duty of anyone building
software   to produce tools  that conform to accepted ethical standards.
This book discusses how that might be done.

It turns out that many different models can be fitted to data.
Each such model represents a trade between:

- what we want;
- and what we want to avoid.

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

