import numpy
import re
import json
import poemstruct

for i in range(98,232):
  if i <=99:
    filename = 'baudhtml/0' + str(i) + '.txt'
  else:
    filename = 'baudhtml/' + str(i) + '.txt'
  with open(filename) as fd:
    rawlines = fd.read().splitlines()

with open(filename) as fd:
    rawlines = fd.read().splitlines()
    print(rawlines)
