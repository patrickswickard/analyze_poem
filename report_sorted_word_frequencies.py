"""Script to report word frequencies of a poem that has been parsed to a json file"""
import json
import sys
import getopt
import poemstruct

def analyze_poem(thispoem):
  """Analyze poem stanza syllable line info and word and letter frequencies"""
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
  """Dump the poem hash to external file"""
#  f = open(filename,'w')
#  f.write(thispoem.dump_poem_hash())
#  f.close()
  with open(filename,'w',encoding='utf-8') as outfile:
    outfile.write(thispoem.dump_poem_hash())

def read_poem(poem_file):
  """Read in a poem from a file"""
  with open(poem_file,'r',encoding='utf-8') as myfile:
    lines = myfile.read().splitlines()
  thispoem = poemstruct.Poem(lines)
  return thispoem

def main(argv):
  """Main script"""
  inputfile = ''
  opts, args = getopt.getopt(argv,"hi:",["ifile="])
  for opt, arg in opts:
    if opt == '-h':
      print("report_sorted_word_frequencies.py -i <inputfile>")
      sys.exit()
    elif opt in ('-i', '--ifile'):
      inputfile = arg
  if inputfile:
    with open(inputfile,'r',encoding='utf-8') as myfile:
      this_json = json.load(myfile)
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
