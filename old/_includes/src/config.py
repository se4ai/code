class Defaults:
  def __init__(i):
    ## system settings (do not change)
    # misc
    i.inf    = 10**32
    i.tiny   = 1/i.inf
    # characters in data,header
    i.ignore = "?"
    i.less   = "<"
    i.more   = ">"
    i.num    = "$"
    i.klass  = "!"

    # hyperparameter settings
    # sample-ing
    i.keep   = 128
    # chops
    i.tiny   = 3
    i.cohen  = 0.3 # 0.5 0.4 0.3 0.2
    i.ncohen = 1/7 # 2/9 2/8 1/7 1/6
    i.bins   = 16
    i.simplerBy = 0.01
    # read data in 'eras' of size i.era
    i.era    = 512

my= Defaults()
