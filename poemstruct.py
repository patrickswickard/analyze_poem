import numpy

class Book:
  def __init__(self):
    self.title = ''
    self.author = ''
    self.poem_list = []

class Poem:
  def __init__(self,title,dedicatee,lines):
    self.title = title
    self.dedicatee = dedicatee
    self.lines = lines

  def length(self):
    return len(self.lines)

  def get_firstline(self):
    lines = self.lines
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

  def get_body(self):
    lines = self.lines
    firstvals = self.get_firstline()
    title = firstvals[0]
    dedicatee = firstvals[1]
    firstline = firstvals[2]
    poem_text = lines
    return poem_text[firstline:]

  def get_stanzas(self):
    lines = self.lines
    stanza_count = 0
    stanza_length = 0
    line_count = 0
    stanzas = []
    in_stanza = False
    poem_body = self.get_body()
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
    nonempty_lines = []
    for thisline in lines:
      if thisline:
        nonempty_lines.append(thisline)
    unique_lengths = numpy.unique(stanzas)

    if stanza_count == 1:
      print('MYCOUNTS,' + str(line_count) + ',' + '1' + ',' + str(line_count))
    else:
      if len(unique_lengths) == 1:
        print('MYCOUNTS,' + str(line_count) + ',' + str(stanza_count) + ',' + str(stanzas[0]))
      else:
#        print('The poem "' + title + '" consists of ' + str(stanza_count) + ' stanzas of irregular length.'  + ': ' + str(line_count) + ' total.')
        print('MYCOUNTS,' + str(line_count) + ',' + str(stanza_count) + ',' + '-')
