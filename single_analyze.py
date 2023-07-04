import numpy
import re
import json
import poemstruct
import sys
import getopt

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

def main(argv):
  inputfile = ''
  outputfile = ''
  opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  for opt, arg in opts:
    if opt == '-h':
      print("single_analyze.py -i <inputfile> -o <outputfile>")
      sys.exit()
    elif opt in ('-i', '--ifile'):
      inputfile = arg
    elif opt in ('-o', '--ofile'):
      outputfile = arg
  if True:
    this_poem = read_poem(inputfile)
    analyze_poem_to_json(this_poem,outputfile)
  else:
    print("Usage: single_analyze.py -i <inputfile> -o <outputfile>")

if __name__ == "__main__":
  main(sys.argv[1:])
