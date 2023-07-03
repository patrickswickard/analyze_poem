import numpy
import re
import json
import poemstruct

for i in range(98,232):
  if i <=99:
    filename = 'baudhtml/0' + str(i)
  else:
    filename = 'baudhtml/' + str(i)
  with open(filename) as fd:
    rawlines = fd.read().splitlines()
  incontent = False
  inpoem = False
  print(i)
  if i <= 99:
    outfilename = 'baudtxt/0' + str(i) + '.txt'
  else:
    outfilename = 'baudtxt/' + str(i) + '.txt'
  f = open(outfilename,'w')
  poemlist = []
  for thisline in rawlines:
    if incontent:
      if re.match(r"^\s*(?:<p>\s*)?&mdash;[^<]*<i>",thisline):
        inpoem = False
        print("Done with poem!")
        poemlist.append(thispoem)
    if re.match(r"^\s*<!--\s*Content\s*-->\s*$",thisline):
      incontent = True
      print("We're in business!")
    if incontent:
      if re.match(r"^\s*<b>\s*(.*?)\s*</b>\s*(?:<br>\s*)?$",thisline):
        inpoem = True
        print("Starting poem!")
        thispoem = []
    if inpoem:
      if not re.match(r"^\s*(?:<p>|</p>)\s*$",thisline):
        thislinefixed = re.sub(r"(<b>|</b>|<br>)\s*","",thisline)
        thispoem.append(thislinefixed)
    poem_count = 0
    for foundpoem in poemlist:
      poem_count += 1
      if i <= 99:
        outfilename = 'baudtxt/0' + str(i) + "_" + str(poem_count) + '.txt'
      else:
        outfilename = 'baudtxt/' + str(i) + "_" + str(poem_count) + '.txt'
      f = open(outfilename,'w')
      for thisline in foundpoem:
        f.write(thisline + '\n')
      f.close()
