"""Code to analyze poem corpuses"""
import poemstruct

def analyze_poem(thispoem):
  """Analyze a single poem"""
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
  """Spit out poem analysis to json"""
  with open(filename,'w',encoding='utf-8') as myoutfile:
    myoutfile.write(thispoem.dump_poem_hash())

def read_poem(poem_file):
  """Read in an individual poem"""
  with open(poem_file,'r',encoding='utf-8') as myinfile:
    lines = myinfile.read().splitlines()
    thispoem = poemstruct.Poem(lines)
    return thispoem

def analyze_corpus_to_json():
  """Analyze a poet's corpus and spit out to json"""
  corpus_word_frequency_plath = {}
  #corpus_word_frequency_sylph = {}

  values = range(40)
  for i in values:
    poem_file = '/home/swickape/projects/github/plathagrams/spsidebyside' + str(i+1) + '.txt'
    this_poem = read_poem(poem_file)
    if i < 10:
      filename = 'sylph/poem_0' + str(i) + '.json'
    else:
      filename = 'sylph/poem_' + str(i) + '.json'
    analyze_poem_to_json(this_poem,filename)
    for thiskey,thisvalue in this_poem.poem_word_frequencies_hash.items():
      if corpus_word_frequency_plath.get(thiskey):
        corpus_word_frequency_plath[thiskey] = corpus_word_frequency_plath[thiskey] + thisvalue
      else:
        corpus_word_frequency_plath[thiskey] = thisvalue
  for i in values:
    poem_file = '/home/swickape/projects/github/plathagrams/anagram_' + str(i+1) + '.txt'
    if i < 10:
      filename = 'plath/poem_0' + str(i) + '.json'
    else:
      filename = 'plath/poem_' + str(i) + '.json'
    analyze_poem_to_json(this_poem,filename)


def analyze_corpus():
  """Analyze a poet's corpus in particular Plath/Sylph"""
  corpus_word_frequency_plath = {}
  corpus_word_frequency_sylph = {}

  values = range(40)
  for i in values:
    poem_file = '/home/swickape/projects/github/plathagrams/spsidebyside' + str(i+1) + '.txt'
    this_poem = read_poem(poem_file)
    analyze_poem(this_poem)
    for thiskey,thisvalue in this_poem.poem_word_frequencies_hash.items():
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
    print(this_poem.poem_word_frequencies_hash)
    for thiskey,thisvalue in this_poem.poem_word_frequencies_hash.items():
      if corpus_word_frequency_sylph.get(thiskey):
        corpus_word_frequency_sylph[thiskey] = corpus_word_frequency_sylph[thiskey] + thisvalue
      else:
        corpus_word_frequency_sylph[thiskey] = thisvalue

  print('*********************')
  print('Plath corpus:')
  sorted_corpus_word_frequency_plath = sorted(corpus_word_frequency_plath.items(), key=lambda x:x[1],reverse=True)
  print(sorted_corpus_word_frequency_plath)
  print('*********************')
  print('Sylph corpus:')
  sorted_corpus_word_frequency_sylph = sorted(corpus_word_frequency_sylph.items(), key=lambda x:x[1],reverse=True)
  print(sorted_corpus_word_frequency_sylph)
  print('*********************')

#analyze_corpus()
analyze_corpus_to_json()
