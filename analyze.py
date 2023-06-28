import numpy
import re
import json
import poemstruct

#with open('dict.json') as fd:
#  syllable_dict = json.loads(fd.read())

def analyze_poem(thispoem):
  print('*********************')
  print('I read a poem today!')
  thispoem.print_stanza_info()
  #thispoem.print_letter_frequencies()
  #thispoem.print_word_frequencies()
  #thispoem.print_syllable_list()
  thispoem.print_line_info()

def read_poem(poem_file):
  with open(poem_file) as fd:
    lines = fd.read().splitlines()
    thispoem = poemstruct.Poem(lines)
    return thispoem

values = range(40)
for i in values:
  poem_file = '/home/swickape/projects/github/plathagrams/spsidebyside' + str(i+1) + '.txt'
  this_poem = read_poem(poem_file)
  print(str(this_poem.length()))
  analyze_poem(this_poem)
for i in values:
  poem_file = '/home/swickape/projects/github/plathagrams/anagram_' + str(i+1) + '.txt'
  this_poem = read_poem(poem_file)
  print(str(this_poem.length()))
  analyze_poem(this_poem)

print('*********************')
