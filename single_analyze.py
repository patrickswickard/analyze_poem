import numpy
import re
import json
import poemstruct

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

poem_file = 'baudtxt/160_5.txt'
this_poem = read_poem(poem_file)
analyze_poem_to_json(this_poem,'outfile.json')
