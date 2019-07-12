#!/usr/bin/env python3
import sys; sys.path.append(r'../s4a')

from xy import *

@ok
def stringok():
  for n,line in enumerate(string("""Four score and
    seven years ago     
    our mums baked us a cake
    and told us to stop shouting and do our homework""")):
       print(n, '['+line+']')
  assert n==3,"lines lost"

@ok
def fileok():
  for n,line in enumerate(file('libok.py')):
     print(n, '['+line+']')
  assert n>=20,"lines lost"

@ok
def rowok():
  for n,line in enumerate(rows(file('../data/weather.csv'))):
    print(n,line)@ok

@ok
def cellsok():
  for n,line in enumerate(cells(rows(file('../data/weather.csv')))):
    print(n,line)@ok

@ok
def xyok():
  for n,line in enumerate(xy(cells(rows(file('../data/weather.csv'))))):
    print(n,line)
