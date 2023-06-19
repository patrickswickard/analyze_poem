import numpy
import re
import json

with open('/home/swickape/projects/github/plathagrams/spsidebyside11.txt') as fd:
    lines = fd.read().splitlines()
with open('dict.json') as fd:
    syllable_dict = json.loads(fd.read())

def get_syllable_count(word):
  return syllable_dict.get(word.lower(),0)
    

word_hash = {}
def get_word_frequencies(lines):
  for thisline in lines:
    words_only = re.sub(r"[^\w\s]",' ',thisline).upper()
    #print(words_only)
    #print('--------------')
    word_list = words_only.split()
    #print(word_list)
    for thisword in word_list:
      this_word_syllable = syllable_dict.get(thisword.lower())
      if not this_word_syllable:
        #print(thisword + ' not in dictionary!!!!!!!')
        # try dropping the s if ends with s
        if re.findall(r"[^s]s$",thisword.lower()):
          thisword2 = thisword
          thisword2 = re.sub(r"(s$)","",thisword2.lower())
          #print(thisword)
          #print(thisword2)
          #print("try without s " + thisword2)
          this_word_syllable2 = syllable_dict.get(thisword2.lower())
          if not this_word_syllable2:
            pass
            #print(thisword2 + ' not in dictionary without s!!!!!!!')
      if word_hash.get(thisword):
        word_hash[thisword] = word_hash[thisword] + 1
      else:
        word_hash[thisword] = 1
    syllable_list = list(map(lambda x: syllable_dict.get(x.lower()), word_list))
    #print('---------')
    #print('hooboy')
    #print('you jerks')
    #print(syllable_list)
    #print('you guys are rolling bums')
    if (None in syllable_list):
      print('Word with unknown syllable count found in list.')
      print(thisline)
      print(syllable_list)
    else:
      print(str(sum(syllable_list)) + ' syllables in line for recommended pronunciation')
      print(thisline)
      print(syllable_list)

def get_letter_frequencies(lines):
  for thisline in lines:
    print(thisline)
    letters_only = re.sub(r"\W",'',thisline).upper()
    letters_sorted = ''.join(sorted(letters_only))
    print(letters_only)
    letter_count = len(letters_only)
    print(letter_count)
    print(letters_sorted)

def get_firstline(lines):
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
  return [title, dedicatee, firstline]

def get_stanzas(lines):
  stanza_count = 0
  stanza_length = 0
  stanzas = []
  in_stanza = False
  firstvals = get_firstline(lines)
  title = firstvals[0]
  dedicatee = firstvals[1]
  firstline = firstvals[2]
  poem_text = lines
  for thisline in poem_text[firstline:]:
    if thisline:
      if in_stanza:
        #print(thisline)
        in_stanza = True
        stanza_length += 1
      else:
        #print('START!!!')
        #print(thisline)
        in_stanza = True
        stanza_length += 1
    else:
      if in_stanza:
        #print('END')
        #print("BLANK!")
        in_stanza = False
        #print(stanza_length)
        stanzas.append(stanza_length)
        stanza_length = 0
      else:
        #print('MOREBLANK')
        in_stanza = False
  # one more stanza check at end
  if in_stanza:
    #print('END')
    #print(stanza_length)
    stanzas.append(stanza_length)
    #print('ENDOFPOEM')
  else:
    pass
    #print('END')
    #print('ENDEDONBLANKLINEIGUESS')
  stanza_count = len(stanzas)
  nonempty_lines = []
  for thisline in lines:
    if thisline:
      nonempty_lines.append(thisline)
  #print(stanzas)
  #print(stanza_count)
  unique_lengths = numpy.unique(stanzas)
  #print(unique_lengths)

  if stanza_count == 1:
    print('The poem "' + title + '" consists of a single stanza"')
  else:
    if len(unique_lengths) == 1:
      print('The poem "' + title + '" consists of ' + str(stanza_count) + ' stanzas of length ' + str(stanzas[0]))
    else:
      print('The poem "' + title + '" consists of ' + str(stanza_count) + ' stanzas of irregular length.')


def analyze_poem(lines):
  get_stanzas(lines)
  get_letter_frequencies(lines)
  get_word_frequencies(lines)

values = range(40)
for i in values:
  poem_file = '/home/swickape/projects/github/plathagrams/spsidebyside' + str(i+1) + '.txt'
  with open(poem_file) as fd:
      lines = fd.read().splitlines()
      analyze_poem(lines)
  poem_file = '/home/swickape/projects/github/plathagrams/anagram_' + str(i+1) + '.txt'
  with open(poem_file) as fd:
      lines = fd.read().splitlines()
      analyze_poem(lines)
  print()
 # print(word_hash)
