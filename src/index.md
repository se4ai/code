# 1.Preface

![](/img/discuss.jpg){: .imgright}


This book is about using better software engineering to build better AI software. 
 AI is a very broad topic, discussed in
 [so](REFS.md#norvig-2009) 
 [very](REFS.md#grus--2019)
 [many](REFS.md#duda-2000)
 [other](REFS.md#witten-2016)
 books. So what makes this book so different?

Firstly,   by "better" AI software, 
we mean "ethically-aligned".
We assert that the design goals for SE-for-AI must be 
prioritize for human well-being.

- It is ethical to improve
the profits of your company since that money becomes wages which
becomes groceries which becomes dinner so everyone and their kids
can sleep better at night.
- It is also ethical to change the design
of AI software in order to ensure   that (say) the software is not
unduly discriminatory towards a particular social group (e.g. some
groups characterized by age, race, or gender). 

Secondly, the authors of this book have spent decades applying many
AI tools ( mostly  for software engineering applications). We share
some of that case study experience in this book.

Thirdly,  we look
 at AI tools which,  recently, have had a major   impact on software
 engineering. Specifically, we will talk much about data mining
 algorithms; some about optimizers; and a little about theorem
 provers.
These technologies are tightly connected. For example:

- Theorem provers can be data generators for data miners or optimizers
    - When models come with many constraints, we can use theorem provers to [generate valid examples](REFS#chen-2018a);
- Optimizers can  improve theorem provers: 
    - Theorem provers deliver solutions in an order dictated  by their internal design. This means, when
     there are very many ways to solve constraints, theorem provers can take a while  to generate solutions that we prefer. In
  this case, a useful trick is to first , run theorem provers (a little) to get a sample of solutions; then  second
      run mutators and optimizers to [combine that sample in interesting ways](REFS#chen-2019).
- Data miners and optimizers can be mashed up to (say) explore complex problems where one
  defines interesting regions where the other can reason faster, and better:
    - In this approach, data miners and optimizers can be seen as separate executables. 
    - For example, [Abdessalem et al.](REFS:abdollahi-2016) generate test cases for autonomous cars via a cyclic approach where an optimizer reflects on the output of data miners that reflect on the output of an optimizer (and so on).
- Data miners can act as optimizers: 
    - In this approach, there is no separation between the data miner and optimizer. 
    - For example, [Chen et al.](REFS#chen-2018a)
show that their recursive descent bi-clustering algorithm (which is a data mining technique) out-performs traditional evolutionary algorithms for the purposes of optimizing SE models.
- Optimizers can better control the data  miners: 
    - In this approach,the data miner is a sub-routine called by the optimizer. 
    - For example, several research has  improved data mining performance via optimizers that tune the control parameters of the data miner (See [Agrawal 2018a](REFS:agrawal-2018a), 
   [Fu'18](REFS:fu-206), and [Tantithamthavorn et al.](Tan-2016a)).
- Data miners can better control the optimizers:
    -  In this approach, the optimizer is a sub-routine called by the data miner. 
    - For example, 
[Majumder et al.](majumder-2018) used k-means clustering to divide up a complex text mining problem, then apply optimizers within each cluster. They report that this method speeds up their processing by up to three orders of magnitude.

Our point is this,  AI tools
offer a rich tapestry of tools that software engineers can weave
 together to achieve a variety of goals. That means
that our
our tools can offer us more
choices. Which means, in turn, that  they are also offer us more ethical choices.
So we suggest to you that when you start a new AI project:

- Your  first question should **not** be (e.g.) "what data miners should I apply to this data?".
- Rather, it should be  "what are the ethical requirements of this development? And how can we best support those requirements?".

Please enjoy this book. If you are teaching this material at
 the graduate level, note that in our table of
contents (shown at top-of-page) there is an _exercises_ section listing some weekly homeworks
and some idea for month-long  projects.

Have fun! Be more ethical!

![](/img/timm.png){:width="50px" } ![](/img/zimm.png){:width="50px" }  

Tim Menzies  (timm)  
Tom Zimmermann (zimm)     
August, 2019    
