import re

file = 'everything.tex'
with open(file) as fd:
  lines = fd.read().splitlines()

# find and report
for thisline in lines:
  if re.search(r"\\\\$",thisline):
    newline = re.sub(r"\\\\$","",thisline)
    print(newline)

