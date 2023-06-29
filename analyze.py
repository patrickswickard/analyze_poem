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

corpus_word_frequency_plath = {}
corpus_word_frequency_sylph = {}

values = range(40)
for i in values:
  poem_file = '/home/swickape/projects/github/plathagrams/spsidebyside' + str(i+1) + '.txt'
  this_poem = read_poem(poem_file)
  print(str(this_poem.length()))
  analyze_poem(this_poem)
  print('word hash for ' + this_poem.title + ':')
  print(this_poem.poem_word_hash)
  for thiskey,thisvalue in this_poem.poem_word_hash.items():
    if corpus_word_frequency_plath.get(thiskey):
      corpus_word_frequency_plath[thiskey] = corpus_word_frequency_plath[thiskey] + thisvalue
    else:
      corpus_word_frequency_plath[thiskey] = thisvalue
for i in values:
  poem_file = '/home/swickape/projects/github/plathagrams/anagram_' + str(i+1) + '.txt'
  this_poem = read_poem(poem_file)
  print(str(this_poem.length()))
  analyze_poem(this_poem)
  print('word hash for ' + this_poem.title + ':')
  print(this_poem.poem_word_hash)
  for thiskey,thisvalue in this_poem.poem_word_hash.items():
    if corpus_word_frequency_sylph.get(thiskey):
      corpus_word_frequency_sylph[thiskey] = corpus_word_frequency_sylph[thiskey] + thisvalue
    else:
      corpus_word_frequency_sylph[thiskey] = thisvalue

print('*********************')
print('Plath corpus:')
#print(corpus_word_frequency_plath)
sorted_corpus_word_frequency_plath = sorted(corpus_word_frequency_plath.items(), key=lambda x:x[1],reverse=True)
print(sorted_corpus_word_frequency_plath)
print('*********************')
print('Sylph corpus:')
#print(corpus_word_frequency_sylph)
sorted_corpus_word_frequency_sylph = sorted(corpus_word_frequency_sylph.items(), key=lambda x:x[1],reverse=True)
print(sorted_corpus_word_frequency_sylph)
print('*********************')
