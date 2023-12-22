"""Poem analysis tools"""
import getopt
import sys
import poemstruct

def analyze_poem(thispoem):
  """Analyze stanza syllable line info and word and letter frequencies"""
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
  """Analyze poem and spit out to a given json file"""
#  f = open(filename,'w')
#  f.write(thispoem.dump_poem_hash())
#  f.close()
  with open(filename,'w',encoding="utf-8") as thisoutfile:
    thisoutfile.write(thispoem.dump_poem_hash())

def read_poem(poem_file):
  """Read in a poem and spit out as individual lines"""
  with open(poem_file,'r',encoding="utf-8") as my_poem:
    lines = my_poem.read().splitlines()
    thispoem = poemstruct.Poem(lines)
    return thispoem

def main(argv):
  """Main script method for analyzing poems"""
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
  if inputfile and outputfile:
    this_poem = read_poem(inputfile)
    analyze_poem_to_json(this_poem,outputfile)
  else:
    print("Usage: single_analyze.py -i <inputfile> -o <outputfile>")

if __name__ == "__main__":
  main(sys.argv[1:])
