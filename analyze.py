import numpy
import re
import json
import poemstruct

#with open('dict.json') as fd:
#  syllable_dict = json.loads(fd.read())

def analyze_poem(thispoem):
  #thispoem.get_stanzas()
  #get_letter_frequencies(thispoem)
  #thispoem.get_letter_frequencies()
  #get_word_frequencies(thispoem)
  #thispoem.get_word_frequencies()
  #get_syllable_data(thispoem)
  thispoem.get_syllable_data()

def read_poem(poem_file):
  with open(poem_file) as fd:
    lines = fd.read().splitlines()
    if lines[0] and not lines[1] and lines[2]:
      title = lines[0]
      dedicatee = ''
      firstline = 2
    elif lines[0] and lines[1] and not lines[2] and lines[3]:
      title = lines[0]
      dedicatee = lines[1]
      firstline = 3
    else:
      raise 'This does not fit the format'
    thispoem = poemstruct.Poem(title,dedicatee,lines)
    return thispoem

values = range(40)
for i in values:
  poem_file = '/home/swickape/projects/github/plathagrams/spsidebyside' + str(i+1) + '.txt'
  this_poem = read_poem(poem_file)
  print('HOOHAH' + str(this_poem.length()))
  analyze_poem(this_poem)
for i in values:
  poem_file = '/home/swickape/projects/github/plathagrams/anagram_' + str(i+1) + '.txt'
  this_poem = read_poem(poem_file)
  analyze_poem(this_poem)

print()
