"""Classes for analyzing poetry"""
import re
import json
import numpy

with open('dict.json','r',encoding="utf-8") as fd:
  syllable_dict = json.loads(fd.read())

class Book:
  """Class for holding information about a book, i.e. a collection of poems"""
  def __init__(self):
    self.title = ''
    self.author = ''
    self.poem_list = []

class Line:
  """Methods and attributes for an individual line of a poem"""
  def __init__(self,linetext):
    self.text = linetext.strip()
    self.syllable_list = []
    self.syllable_count = 0
    self.letters_only = ''
    self.sig = ''
    self.length_letters_only = 0

  def build_line_hash(self):
    """Build hash out of information about a particular line"""
    thishash = {}
    thishash['text'] = self.text
    thishash['syllable_list'] = self.syllable_list
    thishash['syllable_count'] = self.syllable_count
    thishash['letters_only'] = self.letters_only
    thishash['sig'] = self.sig
    thishash['length_letters_only'] = self.length_letters_only
    return thishash

class Poem:
  """Class and methods to hold and compute information about a single poem"""
  def __init__(self,lines):
    self.lines = lines
    self.text = ' '.join(self.lines)
    self.linelist = []
    for thisline in lines:
      actual_line = Line(thisline)
      self.linelist.append(actual_line)
    self.get_firstline()
    self.body = self.get_body()
    self.poem_word_hash = {}
    self.unknown_word_list = []
    self.get_stanzas()
    self.poem_line_syllable_list = []
    self.get_syllable_data()
    self.poem_word_frequencies_hash = {}
    self.get_poem_word_frequencies()
    self.letters_only = ''
    self.sig = ''
    self.length_letters_only = 0
    self.get_letter_frequencies()
    poem_hash = self.build_poem_hash()
    self.poem_hash = poem_hash

  def length(self):
    """Method to get the length of the poem"""
    return len(self.lines)

  def get_firstline(self):
    """Get the first line of the poem"""
    lines = self.linelist
    if lines[0].text and not lines[1].text and lines[2].text:
      self.title = lines[0].text
      self.dedicatee = ''
      self.firstline = 2
    elif lines[0].text and lines[1].text and not lines[2].text and lines[3].text:
      self.title = lines[0].text
      self.dedicatee = lines[1].text
      self.firstline = 3
    else:
      raise 'This does not fit the format'

  def get_body(self):
    """Get only the body of the poem"""
    firstline = self.firstline
    return self.linelist[firstline:]

  def get_letter_frequencies(self):
    """Get all letter frequencies in poem"""
    for thisline in self.linelist:
      Poem.get_line_letter_frequencies(thisline)
    self.get_poem_letter_frequencies()

  def get_stanzas(self):
    """Process poem to get stanzas"""
    stanza_count = 0
    stanza_length = 0
    nonempty_line_count = 0
    stanzas = []
    in_stanza = False
    poem_body = self.body
    for thisline in poem_body:
      if thisline.text:
        if in_stanza:
          in_stanza = True
          stanza_length += 1
          nonempty_line_count += 1
        else:
          in_stanza = True
          stanza_length += 1
          nonempty_line_count += 1
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
    self.stanza_count = stanza_count
    self.stanza_unique_lengths = numpy.unique(stanzas)
    self.nonempty_line_count = nonempty_line_count
    self.stanza_structure = stanzas

  @staticmethod
  def get_string_sig(string):
    """Get a signature for a string, i.e. an alphabetical list of all letters used and repeated"""
    letters_only = Poem.get_string_letters(string)
    letters_only_sorted = ''.join(sorted(letters_only))
    return letters_only_sorted

  @staticmethod
  def get_string_letters(string):
    """Get letter count for a given string"""
    letters_only = re.sub(r"\W",'',string).upper()
    return letters_only

  def get_string_syllable_count(self,thisword):
    """Get syllable count for a given string"""
    thisword_original = thisword
    this_word_syllable = syllable_dict.get(thisword.lower())
    alt_word_syllable = syllable_dict.get(thisword.lower())
    if not this_word_syllable:
      # try dropping the s if ends with s
      if re.findall(r"[^s]s$",thisword.lower()):
        altword = re.sub(r"(s$)","",thisword.lower())
        alt_word_syllable = syllable_dict.get(altword.lower())
        if not alt_word_syllable:
          pass
      # try dropping the 's if ends with s
      if re.findall(r"'s$",thisword.lower()):
        altword = re.sub(r"('s$)","",thisword.lower())
        alt_word_syllable = syllable_dict.get(altword.lower())
        if not alt_word_syllable:
          pass
      # try dropping the ed if ends with ed
      if re.findall(r"[^s]ed$",thisword.lower()):
        altword = re.sub(r"(ed$)","",thisword.lower())
        alt_word_syllable = syllable_dict.get(altword.lower())
        if not alt_word_syllable:
          pass
    if this_word_syllable:
      return this_word_syllable
    if alt_word_syllable:
      return alt_word_syllable
    self.unknown_word_list.append(thisword_original)
    print("WARNING: " + thisword + "  does not have syllable")
    return None

  @staticmethod
  def get_word_list(string):
    """Get list of words in a string"""
    # drop single quotes at beginning/end of line
    string = re.sub(r"(^'|'$)",'',string)
    # drop non-whitespace but retain apostrophes
    words_only = re.sub(r"[^\w\s']",' ',string).strip().upper()
    word_list = re.split(r"\s+",words_only)
    return word_list

  @staticmethod
  def get_line_letter_frequencies(thisline):
    """Get letter frequencies for a line"""
    thisline.letters_only = Poem.get_string_letters(thisline.text)
    thisline.sig = Poem.get_string_sig(thisline.text)
    thisline.length_letters_only = len(thisline.letters_only)

  def get_poem_letter_frequencies(self):
    """Get letter frequencies for a poem"""
    self.letters_only = Poem.get_string_letters(self.text)
    self.sig = Poem.get_string_sig(self.text)
    self.length_letters_only = len(self.letters_only)
    for thisline in self.linelist:
      Poem.get_line_letter_frequencies(thisline)

  @staticmethod
  def get_line_word_frequencies(thisline):
    """Get word frequencies for a line"""
    thisline.word_frequencies_hash = Poem.get_string_word_frequencies(thisline.text)

  def get_poem_word_frequencies(self):
    """Get word frequencies for a given poem"""
    total_syllables = 0
    for thisline in self.linelist:
      Poem.get_line_word_frequencies(thisline)
      for thiskey,thisvalue in thisline.word_frequencies_hash.items():
        if self.poem_word_frequencies_hash.get(thiskey):
          self.poem_word_frequencies_hash[thiskey] = self.poem_word_frequencies_hash[thiskey] + thisvalue
        else:
          self.poem_word_frequencies_hash[thiskey] = thisvalue

  @staticmethod
  def get_string_word_frequencies(string):
    """Get word frequencies for a given string"""
    this_word_hash = {}
    word_list = Poem.get_word_list(string)
    for thisword in word_list:
      if this_word_hash.get(thisword):
        this_word_hash[thisword] = this_word_hash[thisword] + 1
      else:
        this_word_hash[thisword] = 1
    return this_word_hash

  def get_string_syllable_list(self,string):
    """Get syllable info for a given string"""
    word_list = Poem.get_word_list(string)
    string_syllable_list = []
    for thisword in word_list:
      this_syllable_count = self.get_string_syllable_count(thisword)
      string_syllable_list.append(this_syllable_count)
    return string_syllable_list

  def get_syllable_data(self):
    """Compute syllable info for the poem"""
    lines = []
    total_syllables = 0
    nonempty_line_count = self.nonempty_line_count
    for thisline in self.linelist:
      if thisline.text:
        word_list = Poem.get_word_list(thisline.text)
        thisline.syllable_list = self.get_string_syllable_list(thisline.text)
        line_syllable_list = thisline.syllable_list
        self.poem_line_syllable_list.append(line_syllable_list)
        if None in line_syllable_list:
          thisline.syllable_count = None
          print(thisline.text)
          #raise('Word with unknown syllable count found in list.')
        else:
          number_of_syllables = sum(line_syllable_list)
          thisline.syllable_count = number_of_syllables
          total_syllables += number_of_syllables
    syllables_per_line = round(total_syllables/nonempty_line_count,3)
    self.total_syllables = total_syllables
    self.nonempty_line_count = nonempty_line_count
    self.syllables_per_line = syllables_per_line

  def print_poem_syllable_info(self):
    """Print syllable information for the poem"""
    print('1 - title, syllables, lines:' + self.title + ',' + str(self.total_syllables) + ',' + str(self.nonempty_line_count))
    print('2 - average syllables per non-blank line:' + str(self.syllables_per_line))

  def print_poem_stanza_info(self):
    """Print stanza structural info for the poem"""
    if self.stanza_count == 1:
      print('The poem "' + self.title + '" consists of ' + '1' + ' stanza of length' + str(self.stanza_unique_lengths) + '.'  + ': ' + str(self.nonempty_line_count) + ' total.')
    else:
      if len(self.stanza_unique_lengths) == 1:
        print('The poem "' + self.title + '" consists of ' + str(self.stanza_count) + ' stanzas of length' + str(self.stanza_unique_lengths) + ': ' + str(self.nonempty_line_count) + ' total.')
      else:
        print('The poem "' + self.title + '" consists of ' + str(self.stanza_count) + ' stanzas of irregular length.'  + ': ' + str(self.nonempty_line_count) + ' total.')
    print('6: stanza structure:' + str(self.stanza_structure))
    print('\n')

  @staticmethod
  def print_line_letter_frequencies(thisline):
    """Print letter frequencies for a line"""
    if thisline.text:
      print('Line text: ' + thisline.text)
      print('Letters:    ' + thisline.letters_only)
      print('Sig:         ' + thisline.sig)
      print('Line length letters only: ' + str(thisline.length_letters_only))
      print()

  def print_poem_letter_frequencies(self):
    """Print letter frequencies for a poem"""
    print('Poem text: ' + self.text)
    print('Letters:    ' + self.letters_only)
    print('Sig:         ' + self.sig)
    print('Poem length letters only: ' + str(self.length_letters_only))
    print('\n')

  def print_poem_word_frequencies(self):
    """Print word frequencies for a poem"""
    print(self.poem_word_frequencies_hash)

  @staticmethod
  def print_line_syllable_list(thisline):
    """Print syllable list for a line"""
    if thisline.text:
      print(thisline.text)
      if None in thisline.syllable_list:
        print('Word with unknown syllable count found in list.')
        print(thisline.syllable_list)
        print()
      else:
        print(str(thisline.syllable_count) + ' syllables in line for recommended pronunciation')
        print('Syllable structure: ' + str(thisline.syllable_list))
        print()

  def print_line_info(self):
    """Print line letter frequencies and syllable list"""
    for thisline in self.linelist:
      if thisline:
        Poem.print_line_letter_frequencies(thisline)
        Poem.print_line_syllable_list(thisline)

  def build_poem_hash(self):
    """Turn attributes into a hash structure"""
    thishash = {}
    thishash['title'] = self.title
    thishash['text'] = self.text
    thishash['nonempty_line_count'] = self.nonempty_line_count
    thishash['stanza_count'] = self.stanza_count
    thishash['stanza_structure'] = self.stanza_structure
    thishash['total_syllables'] = self.total_syllables
    thishash['syllables_per_line'] = self.syllables_per_line
    thishash['poem_word_frequencies_hash'] = self.poem_word_frequencies_hash
    thishash['sig'] = self.sig
    thishash['length_letters_only'] = self.length_letters_only
    linelist = []
    for thisline in self.linelist:
      linehash = thisline.build_line_hash()
      linelist.append(linehash)
    thishash['linelist'] = linelist
    return thishash

  def dump_poem_hash(self):
    """Dump poem hash to json string"""
    return json.dumps(self.build_poem_hash())
