This directory contains code used to analyze poetry structure.  Goal is to analyze number of stanzas and stanza length.  Eventually we will also try to count syllables, look for rhymes, give letter frequency breakdown, etc.  This is a spinoff of the Plathagrams project

Note two issues with dictionary:
1.  Many words are missing that are not terribly uncommon
2.  Many words have alternate pronunciations, e.g. "our" can be one or two syllables.  Code only takes the preferred (first) version

I frankensteined together two flawed dictionaries to make one larger flawed dictionary and added code to catch simple +s plurals.  This also affects haikus project.  More information can be found in the haiku project for constructing this dictionary and adding words.

--------------------------------------------------------------------------------

In its current form, this code analyzes poetry on four different levels.

As input it will read in poems in the following format:
POEM_TITLE
DEDICATEE (optional)
BLANK_LINE
POEM_BODY

In other words, one or two nonempty lines for the title and optional dedicatee, an empty line, and then the body of the poem with empty lines separating stanzas.

First it analyzes a poem at the stanza level.  This reports the title of the poem, the number of stanzas, and the stanza structure and total number of lines.  It will note and report if the poem has a regular number of lines per stanza.

Next it reports the actual (alphabetical) letters used in composing the line.  It then reports a "signature" based on those letters arranged in alphabetical order, then reports the number of letters in the line.  This analysis was used for another rather silly project involving anagrams, but it still counts as quantifiable data about a poem.

It then moves on to syllable count.  Assuming all the words in the poem are in the pronunciation dictionary being used (with some primitive stemming), it will break the line into individual words and count the syllables in each word.  It then reports the syllable structure and the total number of syllables in the line for the pronunciation suggested by the dictionary.  (This is admittedly imperfect.)

Finally it reports a word frequency list for that particular poem.  It also gives a total number of syllables, number of non-empty lines, and average syllable count per nonempty line.

TODO - we aren't directly reporting number of words in the poem or words per line.

An ideal final product for an individual poem would be a json structure containing all of this quantifiable data.

We also may wish to make a json file consisting of an entire corpus (as in group of poems) which quantifies these counts and averages across several individual poems as a group, e.g. all of Plath's poems from "Ariel", all of Shakespeare's sonnets, etc.

We need to deal intelligently with "missing words" from our dictionary.  Current expectation is that the dictionary will contain all words with syllable counts or be "patched" to do so for analysis.  This requires better tools than we currently have.

As a stretch goal, many but not all words in dictionary potentially have a stress pattern for expected pronunciation, which can be useful for analysis.
