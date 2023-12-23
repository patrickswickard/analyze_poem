"""Code to read in raw baud html"""
def readbaud():
  """Read baud txt files which probably no longer exist"""
  for i in range(98,232):
    if i <=99:
      filename = 'baudtxt/0' + str(i) + '.txt'
    else:
      filename = 'baudtxt/' + str(i) + '.txt'
    with open(filename,'r',encoding='utf-8') as myinfile:
      rawlines = myinfile.read().splitlines()

  with open(filename,'r',encoding='utf=8') as myinfile:
    rawlines = myinfile.read().splitlines()
    print(rawlines)

readbaud()
