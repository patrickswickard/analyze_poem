"""A script to analyze all poems in a directory I guess, been awhile since I wrote this"""
import re
import os
import poemstruct

def analyze_poem(thispoem):
  """Analyze an individual poem"""
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
  """Spit poem analysis to json"""
  with open(filename,'w',encoding="utf-8") as myoutfile:
    myoutfile.write(thispoem.dump_poem_hash())

def read_poem(poem_file):
  """Read in an individual poem"""
  with open(poem_file,'r',encoding='utf-8') as myinfile:
    lines = myinfile.read().splitlines()
    thispoem = poemstruct.Poem(lines)
    return thispoem

def multi_analyze():
  """Do some various poem analysis and report results, reporting missing dict words in particular"""
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

multi_analyze()
