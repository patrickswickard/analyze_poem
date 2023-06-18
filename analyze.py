import numpy

with open('/home/swickape/projects/github/plathagrams/spsidebyside11.txt') as fd:
    lines = fd.read().splitlines()

def analyze_poem(lines):
  poem_text = lines
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

  stanza_count = 0
  stanza_length = 0
  stanzas = []
  in_stanza = False
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
  print('\n')
