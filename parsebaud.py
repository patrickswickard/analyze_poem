import re

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
        thislinefixed = re.sub(r"&mdash;","--",thislinefixed)
        thislinefixed = re.sub(r"&quot;",'"',thislinefixed)
        #if not poem_count == 1:
        if 1:
          thislinefixed = re.sub(r"&eacute;","e",thislinefixed)
          thislinefixed = re.sub(r"&egrave;","e",thislinefixed)
          thislinefixed = re.sub(r"æ","ae",thislinefixed)
          thislinefixed = re.sub(r"œ","oe",thislinefixed)
          thislinefixed = re.sub(r"Æ","Ae",thislinefixed)
          thislinefixed = re.sub(r"è","e",thislinefixed)
          thislinefixed = re.sub(r"é","e",thislinefixed)
          thislinefixed = re.sub(r"ü","u",thislinefixed)
          thislinefixed = re.sub(r"&agrave;","a",thislinefixed)
          thislinefixed = re.sub(r"&Eacute;","E",thislinefixed)
          thislinefixed = re.sub(r"&Egrave;","E",thislinefixed)
          thislinefixed = re.sub(r"&ecirc;","e",thislinefixed)
          thislinefixed = re.sub(r"&ocirc;","o",thislinefixed)
          thislinefixed = re.sub(r"&Agrave;","A",thislinefixed)
          thislinefixed = re.sub(r"_","",thislinefixed)
        thispoem.append(thislinefixed)
    poem_count = 0
    for foundpoem in poemlist:
      poem_count += 1
      if i <= 99:
        outfilename = 'baudtxt2/0' + str(i) + "_" + str(poem_count) + '.txt'
      else:
        outfilename = 'baudtxt2/' + str(i) + "_" + str(poem_count) + '.txt'
      f = open(outfilename,'w')
      for thisline in foundpoem:
        f.write(thisline + '\n')
      f.close()
