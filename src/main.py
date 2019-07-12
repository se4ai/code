"""

# About this code. 

## How to Install

- Move all the code to a new directory. 
- Every file knows its dependencies and so can 
  be executed directly using `python3 xx.py`.
- Look at the _okX.py_ files for samples of how to use this code.

## How to Configure

This file is loaded by everything else. It creates a global `my`
holding system-wide settings.

Also controlled here is the random number seed[^seed]. The idiom
`my =Defaults().reset()` will reset everything back to the defaults,
including the seed.  If that is not desired, just use `my=Defaults()`.

Note that, often, this code  read rows of data where the first row
contains the names of the columns. Those names can contain magic
symbols denoting special properties of the columns. For a list of
those properties, see `ignore, less, more, klass`, below.

"""
import random

class Defaults:
  def __init__(i):
    ## system settings (do not change)
    # misc
    i.inf     = 10**32
    i.tiny    = 1/i.inf
    i.private = "_"
    # characters in data,header
    i.ignore = "?"   # column to ignore
    i.less   = "<"   # a numeric goal, to be minimized
    i.more   = ">"   # a numeric goal, to goal to maximize
    i.klass  = "!"   # a symbolic class, to be predicted for

    # other stuff
    i.seed = 235324971  # from random.org
    # hyper parameter settings
    # sampling
    i.keep   = 128
    # chops
    i.cohen  = 0.3 # 0.5 0.4 0.3 0.2
    i.ncohen = 1/7 # 2/9 2/8 1/7 1/6
    i.bins   = 16
    i.simplerBy = 0.01
    # read data in 'eras' of size i.era
    i.era    = 512
  def reset(i,seed=None):
    random.seed(seed or i.seed)
    return i

my= Defaults().reset()

"""


## How to Test

Each file can be loaded and tested independently .
To enable that,  each file begins with a set of `import` statements that describe all its dependencies.

Some files `X.py` have demo/test code in `okX.py` 

- The demo/test code uses the unit test engine in `ok.py`. This test engine was strongly inspired by 
  Kent Beck's most excellent [making making](https://www.youtube.com/watch?v=nIonZ6-4nuU)  video.
- To test the whole system, run `python3 ok.py`. When loaded as a top-level module,
  this code loads all the "okX.py" files, then runs the `ok()` functions.

## How to Follow this Code's Conventions

All these classes start with an uppercase letters.

All this  code is laid out to be read on mobile devices; hence:

- All code is 60 characters wide.
- This code  does not use `self` but rather `i` to point back to the current instance..
- All tabs are expanded to two spaces.

Any sub-class of `Pretty` (defined in the `lib` module) will print itself as key=value
pairs inside curly braces.

If a class has derived properties, call the method that derives the property (say)
`xxx0` then wrap the class in `@memos`. This will automatically make `xxx` a property
of instances of that class. Further, that method will be memo-ed such that if
the property is requested 100 times, it will get computed once and cached (inside `i._memo`)
and returned 100 times from the cache. If a method makes some change that makes
the memos stale, wrap that method in `@fresh`.

## How to Document

To document this code, add in Markdown comments within multi-line Python quotes.

- All the files get converted into Markdown and rendered by Jekyll. 
- To avoid clashes between documentation and code files, 
  the former have a dash in their name (e.g. _about-book.md_).
- So to extend this code, do not write code files with dashes in the name.

[^seed]: Computers don’t generate truly random numbers—they are deterministic, which means that they operate by a set of rules. You can mimic randomness by specifying a set of rules. For example, “take a number x, add 900 +x, then subtract 52.” In order for the process to start, you have to specify a starting number, x (the seed).

## Comprehension Questions:

```
     1	@relation weather
     2	
     3	@attribute outlook {sunny, overcast, rainy}
     4	@attribute temperature real
     5	@attribute humidity real
     6	@attribute windy {TRUE, FALSE}
     7	@attribute play {yes, no}
     8	
     9	@data
    10	sunny, 85, 85, false, no
    11	sunny, 72, 95, false, no
    12	sunny, 80, 90, true,  no
    13	rainy, 65, 70, true,  no
    14	rainy, 71, 91, true,  no
    15	overcast, 83, 86, false, yes
    16	rainy, 70, 96, false, yes
    17	rainy, 68, 80, false, yes
    18	overcast, 64, 65, true, yes
    19	sunny, 69, 70, false, yes
    20	rainy, 75, 80, false, yes
    21	sunny, 75, 70, true, yes
    22	overcast, 72, 90, true, yes
    23	overcast, 81, 75, false, yes
```

0. For the above data, rewrite it using our magic headers `ignore,less,more,klass`
   (hint: replace likes 1 to 9 with one row with the column names). See if you can
   ignore the _humidity_ column. And try to minimize _temperature_.
1. For all the hyperparamaters listed above, search the code for (e.g.) `my.bins`. 
     - Try to work out what the parameter does.
     - Try to work out what  would happen if the hyperparameter doubled or halved
2. All the above hyperparamaters were set via ``engineering judgment''; i.e. We guessed.
   If the results of AI tools is controlled by so many guesses, what does that say
   about the trustworthiness of these tools.
3. Read section 3 in the [DUO paper](https://arxiv.org/pdf/1812.01550.pdf). 
   Answer the following questions.
     - What is hyperparameter optimization?
     - What are its benefits and weaknesses?
     - The hyperparameter optimizers themselves are controlled  
       by their own magic parameters.
       How slow/fast might hyper-hyperparameter optimization be?
        
"""
