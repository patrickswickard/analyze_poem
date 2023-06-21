import numpy
import re
import json

with open('dict.json') as fd:
    syllable_dict = json.loads(fd.read())

def get_syllable_count(thisword):
  thisword_original = thisword
  this_word_syllable = syllable_dict.get(thisword.lower())
  if not this_word_syllable:
    #print(thisword + ' not in dictionary!!!!!!!')
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
def get_word_frequencies(lines):
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
  line_count = 0
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
        in_stanza = True
        stanza_length += 1
        line_count += 1
      else:
        in_stanza = True
        stanza_length += 1
        line_count += 1
    else:
      if in_stanza:
        in_stanza = False
        stanzas.append(stanza_length)
        stanza_length = 0
      else:
        in_stanza = False
  # one more stanza check at end
  if in_stanza:
    stanzas.append(stanza_length)
  else:
    pass
  stanza_count = len(stanzas)
  nonempty_lines = []
  for thisline in lines:
    if thisline:
      nonempty_lines.append(thisline)
  unique_lengths = numpy.unique(stanzas)

  if stanza_count == 1:
#    print('The poem "' + title + '" consists of a single stanza of length ' + str(line_count))
##    print('The poem "' + title + '" consists of a single stanza of length ' + str(line_count))
    print('MYCOUNTS,' + str(line_count) + ',' + '1' + ',' + str(line_count))
  else:
    if len(unique_lengths) == 1:
#      print('The poem "' + title + '" consists of ' + str(stanza_count) + ' stanzas of length ' + str(stanzas[0])  + ': ' + str(line_count) + ' total.')
##      print('The poem "' + title + '" consists of ' + str(stanza_count) + ' stanzas of length ' + str(stanzas[0])  + ': ' + str(line_count) + ' total.')
      print('MYCOUNTS,' + str(line_count) + ',' + str(stanza_count) + ',' + str(stanzas[0]))
    else:
#      print('The poem "' + title + '" consists of ' + str(stanza_count) + ' stanzas of irregular length.'  + ': ' + str(line_count) + ' total.')
      print('MYCOUNTS,' + str(line_count) + ',' + str(stanza_count) + ',' + '-')


def analyze_poem(lines):
#  get_stanzas(lines)
#  get_letter_frequencies(lines)
  get_word_frequencies(lines)

values = range(40)
for i in values:
  poem_file = '/home/swickape/projects/github/plathagrams/spsidebyside' + str(i+1) + '.txt'
  with open(poem_file) as fd:
      lines = fd.read().splitlines()
      analyze_poem(lines)
##  poem_file = '/home/swickape/projects/github/plathagrams/anagram_' + str(i+1) + '.txt'
##  with open(poem_file) as fd:
##      lines = fd.read().splitlines()
##      analyze_poem(lines)
#print()
sorted_word_hash = sorted(word_hash.items(), key=lambda x:x[1],reverse=True)
#print(sorted_word_hash)
#print()
sorted_unknown_word_list = sorted(unknown_word_list)
print(sorted_unknown_word_list)
