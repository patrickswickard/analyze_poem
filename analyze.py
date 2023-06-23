import numpy
import re
import json
import poemstruct

with open('dict.json') as fd:
    syllable_dict = json.loads(fd.read())

def get_syllable_data(thispoem):
  lines = thispoem.lines
  total_syllables = 0
  nonempty_line_count = 0
  title = lines[0]
  for thisline in lines:
    if thisline:
      nonempty_line_count += 1
      words_only = re.sub(r"[^\w\s]",' ',thisline).upper()
      word_list = words_only.split()
      for thisword in word_list:
        if word_hash.get(thisword):
          word_hash[thisword] = word_hash[thisword] + 1
        else:
          word_hash[thisword] = 1
      syllable_list = list(map(lambda x: get_syllable_count(x), word_list))
      if (None in syllable_list):
        raise('Word with unknown syllable count found in list.')
      else:
        number_of_syllables = sum(syllable_list)
        total_syllables += number_of_syllables
    else:
      pass
  perline = round(total_syllables/nonempty_line_count,3)
  print(title + ',' + str(total_syllables) + ',' + str(nonempty_line_count))

def get_syllable_count(thisword):
  thisword_original = thisword
  this_word_syllable = syllable_dict.get(thisword.lower())
  if not this_word_syllable:
    # try dropping the s if ends with s
    if re.findall(r"[^s]s$",thisword.lower()):
      thisword = re.sub(r"(s$)","",thisword.lower())
      this_word_syllable = syllable_dict.get(thisword.lower())
      if not this_word_syllable:
        pass
  if this_word_syllable:
    return this_word_syllable
  else:
    unknown_word_list.append(thisword_original)
    return None
    
word_hash = {}
unknown_word_list = []
def get_word_frequencies(thispoem):
  lines = thispoem.lines
  total_syllables = 0
  for thisline in lines:
    words_only = re.sub(r"[^\w\s]",' ',thisline).upper()
    word_list = words_only.split()
    for thisword in word_list:
      if word_hash.get(thisword):
        word_hash[thisword] = word_hash[thisword] + 1
      else:
        word_hash[thisword] = 1
    syllable_list = list(map(lambda x: get_syllable_count(x), word_list))
    if (None in syllable_list):
      print('Word with unknown syllable count found in list.')
      print(thisline)
      print(syllable_list)
    else:
      print(str(sum(syllable_list)) + ' syllables in line for recommended pronunciation')
      print(thisline)
      print(syllable_list)

def get_letter_frequencies(thispoem):
  lines = thispoem.lines
  for thisline in lines:
    print(thisline)
    letters_only = re.sub(r"\W",'',thisline).upper()
    letters_sorted = ''.join(sorted(letters_only))
    print(letters_only)
    letter_count = len(letters_only)
    print(letter_count)
    print(letters_sorted)

def analyze_poem(thispoem):
  thispoem.get_stanzas()
  #get_letter_frequencies(thispoem)
  #get_word_frequencies(thispoem)
  #get_syllable_data(thispoem)

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
    #return [title, dedicatee, firstline,lines]
    return thispoem
    #analyze_poem(lines)

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
sorted_word_hash = sorted(word_hash.items(), key=lambda x:x[1],reverse=True)
#print(sorted_word_hash)
#print()
sorted_unknown_word_list = sorted(unknown_word_list)
print(sorted_unknown_word_list)
