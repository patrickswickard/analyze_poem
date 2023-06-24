import numpy
import re
import json

with open('dict.json') as fd:
  syllable_dict = json.loads(fd.read())

class Book:
  def __init__(self):
    self.title = ''
    self.author = ''
    self.poem_list = []

class Poem:
  #def __init__(self,title,dedicatee,lines):
  def __init__(self,lines):
    #self.title = title
    #self.dedicatee = dedicatee
    self.lines = lines
    self.get_firstline()
    self.word_hash = {}
    self.unknown_word_list = []
    self.body = self.get_body()
    self.get_stanzas()

  def length(self):
    return len(self.lines)

  def get_firstline(self):
    lines = self.lines
    if lines[0] and not lines[1] and lines[2]:
      self.title = lines[0]
      self.dedicatee = ''
      self.firstline = 2
    elif lines[0] and lines[1] and not lines[2] and lines[3]:
      self.title = lines[0]
      self.dedicatee = lines[1]
      self.firstline = 3
    else:
      raise 'This does not fit the format'

  def get_body(self):
    lines = self.lines
    #firstvals = self.get_firstline()
    #title = firstvals[0]
    title = self.title
    #dedicatee = firstvals[1]
    dedicatee = self.dedicatee
    #firstline = firstvals[2]
    firstline = self.firstline
    poem_text = lines
    return poem_text[firstline:]

  def print_stanza_info(self):
    if self.stanza_count == 1:
      print('MYCOUNTS,' + str(self.line_count) + ',' + '1' + ',' + str(self.line_count))
    else:
      if len(self.stanza_unique_lengths) == 1:
        print('MYCOUNTS,' + str(self.line_count) + ',' + str(self.stanza_count) + ',' + str(self.stanzas[0]))
      else:
        print('The poem "' + self.title + '" consists of ' + str(self.stanza_count) + ' stanzas of irregular length.'  + ': ' + str(self.line_count) + ' total.')
        print('MYCOUNTS,' + str(self.line_count) + ',' + str(self.stanza_count) + ',' + '-')

  def get_stanzas(self):
    lines = self.lines
    stanza_count = 0
    stanza_length = 0
    line_count = 0
    stanzas = []
    in_stanza = False
    poem_body = self.body
    for thisline in poem_body:
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
    self.nonempty_lines = []
    for thisline in lines:
      if thisline:
        self.nonempty_lines.append(thisline)
    self.stanza_count = stanza_count
    self.stanza_unique_lengths = numpy.unique(stanzas)
    self.line_count = line_count
    self.stanzas = stanzas
    #self.print_stanza_info()

  def get_letter_frequencies(self):
    lines = self.lines
    for thisline in lines:
      print(thisline)
      letters_only = re.sub(r"\W",'',thisline).upper()
      letters_sorted = ''.join(sorted(letters_only))
      print(letters_only)
      letter_count = len(letters_only)
      print(letter_count)
      print(letters_sorted)

  def get_syllable_count(self,thisword):
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
      self.unknown_word_list.append(thisword_original)
      return None

  def get_word_frequencies(self):
    lines = self.lines
    total_syllables = 0
    for thisline in lines:
      words_only = re.sub(r"[^\w\s]",' ',thisline).upper()
      word_list = words_only.split()
      for thisword in word_list:
        if self.word_hash.get(thisword):
          self.word_hash[thisword] = self.word_hash[thisword] + 1
        else:
          self.word_hash[thisword] = 1
      syllable_list = list(map(lambda x: self.get_syllable_count(x), word_list))
      if (None in syllable_list):
        print('Word with unknown syllable count found in list.')
        print(thisline)
        print(syllable_list)
      else:
        print(str(sum(syllable_list)) + ' syllables in line for recommended pronunciation')
        print(thisline)
        print(syllable_list)
    #sorted_word_hash = sorted(self.word_hash.items(), key=lambda x:x[1],reverse=True)
    #print(sorted_word_hash)
    #sorted_unknown_word_list = sorted(self.unknown_word_list)
    #print(sorted_unknown_word_list)

  def get_syllable_data(self):
    lines = self.lines
    total_syllables = 0
    nonempty_line_count = 0
    title = lines[0]
    for thisline in lines:
      if thisline:
        nonempty_line_count += 1
        words_only = re.sub(r"[^\w\s]",' ',thisline).upper()
        word_list = words_only.split()
        for thisword in word_list:
          if self.word_hash.get(thisword):
            self.word_hash[thisword] = self.word_hash[thisword] + 1
          else:
            self.word_hash[thisword] = 1
        syllable_list = list(map(lambda x: self.get_syllable_count(x), word_list))
        if (None in syllable_list):
          raise('Word with unknown syllable count found in list.')
        else:
          number_of_syllables = sum(syllable_list)
          total_syllables += number_of_syllables
      else:
        pass
    perline = round(total_syllables/nonempty_line_count,3)
    print(title + ',' + str(total_syllables) + ',' + str(nonempty_line_count))
