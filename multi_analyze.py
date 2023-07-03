import numpy
import re
import json
import poemstruct
import os

def analyze_poem(thispoem):
  print('*********************')
  print('I read a poem today!')
  print(thispoem.title)
  print()
  thispoem.print_poem_stanza_info()
  thispoem.print_poem_syllable_info()
  thispoem.print_line_info()
  thispoem.print_poem_word_frequencies()
  thispoem.print_poem_letter_frequencies()

def analyze_poem_to_json(thispoem,filename):
  f = open(filename,'w')
  f.write(thispoem.dump_poem_hash())
  f.close()

def read_poem(poem_file):
  with open(poem_file) as fd:
    lines = fd.read().splitlines()
    thispoem = poemstruct.Poem(lines)
    return thispoem

list_of_files = os.listdir('baudtxt2')
for thisfile in list_of_files:
  #print(thisfile)
  poem_file = 'baudtxt2/' + thisfile
  poem_outfile = 'baudjson/' + re.sub(r"\.txt",".json",thisfile)
  print(poem_file)
  print(poem_outfile)
  if re.findall(r"_1\.txt",poem_file):
    pass
  else:
    this_poem = read_poem(poem_file)
    try:
      #analyze_poem_to_json(this_poem,'outfile.json')
      analyze_poem_to_json(this_poem,poem_outfile)
    except:
      print('problem with ' + poem_file)
