"""One-off script to grab all captions from graffiti book index"""
import re

def grablines():
  """Grab and clean lines from graffiti captions book"""
  file = 'everything.tex'
  with open(file,'r',encoding='utf-8') as myinfile:
    lines = myinfile.read().splitlines()

  # find and report
  for thisline in lines:
    if re.search(r"\\\\$",thisline):
      newline = re.sub(r"\\\\$","",thisline)
      print(newline)

grablines()
