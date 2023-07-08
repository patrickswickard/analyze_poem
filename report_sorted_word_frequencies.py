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
  opts, args = getopt.getopt(argv,"hi:",["ifile="])
  for opt, arg in opts:
    if opt == '-h':
      print("report_sorted_word_frequencies.py -i <inputfile>")
      sys.exit()
    elif opt in ('-i', '--ifile'):
      inputfile = arg
  if inputfile:
    with open(inputfile) as fd:
      this_json = json.load(fd)
      poem_word_frequencies_hash = this_json['poem_word_frequencies_hash']
      # sort by value (high to low, thus negative) then by alphabetical as tiebreaker
      # the negatives are so we don't do reverse
      poem_word_frequencies_hash_sorted = sorted(poem_word_frequencies_hash.items(), key=lambda x:(-x[1],x),reverse=False)
      print(json.dumps(poem_word_frequencies_hash_sorted))
      #print(poem_word_frequencies_hash_sorted)
  else:
    print("Usage: report_sorted_word_frequencies.py -i <inputfile>")

if __name__ == "__main__":
  main(sys.argv[1:])
