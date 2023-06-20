This directory contains code used to analyze poetry structure.  Goal is to analyze number of stanzas and stanza length.  Eventually we will also try to count syllables, look for rhymes, give letter frequency breakdown, etc.  This is a spinoff of the Plathagrams project

Note two issues with dictionary:
1.  Many words are missing that are not terribly uncommon
2.  Many words have alternate pronunciations, e.g. "our" can be one or two syllables.  Code only takes the preferred (first) version

I frankensteined together two flawed dictionaries to make one larger flawed dictionary and added code to catch simple +s plurals.  This also affects haikus project.  More information can be found in the haiku project for constructing this dictionary and adding words.
