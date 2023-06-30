A DATA SCIENTIST'S APOLOGY

(with apologies to G. H. Hardy)

Why analyze poetry?  Why bring numbers into the picture at all?  Poetry is pretty, math is ugly, right?  Omar Khayyam never suggested sitting beneath the bough with a book of verses, a jug of wine, a loaf of bread, *an abacus and slide rule*, and thou".  It's bad enough that pretentious idiots analyze poems with words.  Why bring numbers into the picture as well?

I'm going to lead this off with my *least* favorite Walt Whitman poem:

-----

When I Heard the Learn’d Astronomer\
\
When I heard the learn’d astronomer,\
When the proofs, the figures, were ranged in columns before me,\
When I was shown the charts and diagrams, to add, divide, and measure them,\
When I sitting heard the astronomer where he lectured with much applause in the lecture-room,\
How soon unaccountable I became tired and sick,\
Till rising and gliding out I wander’d off by myself,\
In the mystical moist night-air, and from time to time,\
Look’d up in perfect silence at the stars.

-----

There is also a quote by Mark Twain about humor that is somewhat relevant:

"Explaining humor is a lot like dissecting a frog, you learn a lot in the process, but in the end you kill it."

I appreciate the sentiment behind these statements.  Sometimes you want to read a poem just to read a poem.  Sometimes you just want to laugh at a joke.  And sometimes you want to gaze at something beautiful without thinking too hard about what makes it beautiful to you.  There is nothing wrong with that.

There's also the view that there's no reason to care about poetry except for fun.  It is a completely worthless human activity that is unworthy of any thought or reflection.  Just read the poem, and enjoy it.  Or, if it's not the sort of poem you're meant to enjoy, heed it as a call to action and go forth and do something serious to change the world.  Poetry is just pretty prose.  There's no reason to think about what makes it pleasant, it just *is*.

It's almost never necessary to bring math or science to the party when you're reading poetry.  But that's true of everything.  Why care about how flowers grow when you can just look at them?  Why care about how the planets move or how stars are born and die when you can just glance at the sky and enjoy the light show while you smoke a bowl and listen to some Pink Floyd?

I'm a mathematician by training.  People don't go into this field of study unless they find beauty and inspiration in structure and form.  Sometimes this structure is immediately obvious, but sometimes you have to dig beneath the surface to appreciate and understand it more fully.  And sometimes it is found in unexpected places.

The code I am posting here consists of simple tools to analyze poems on various levels.  This means generally means dissecting the poems, breaking them down into their components, and quantifying how they are structured.  These tools will count things like stanzas, lines, individual words, syllables, individual letters, etc.  You can look for patterns in structure, frequencies, and all kinds of other facts about how these poems are built.  You can collect and compare and contrast poems and groups of poems according to these numbers.  I can't guarantee that this will yield value and insight, but it may lead to occasional surprises.

Break down two poets' collected works.  Use these tools to break them down and start comparing them.  How many unique words does Poet A use versus unique words used by Poet B?  Look at the individual words they use.  Which words do both poets use?  Where do they differ?  What are the most frequently used words by Poet A that are *never* used by Poet B, and vice versa?  Who tends to use more unique words, words that they only use one time in one poem and never revisit again?  Who is wordier and *by how much*?  Even crude tools like the ones developed here can give you a way to quickly assess these things and look for patterns and differences that you may not have even suspected exist.

Tools are tools.  There's no obligation to use them, and using them foolishly can be a waste of time.  But they also open you up to being able to do things that would be difficult or impossible without them.  And sometimes they enable you to find beauty where none was expected.  You don't need to look at a flower under a microscope to see its beauty.  But if you do, you may find that flowers are beautiful on a whole other level you weren't expecting.  And if you turn the same microscope on the scummy water that has collected in the rain barrels you use to water your garden, you may find a gorgeous tiny garden teeming with strange life that you wouldn't see with the naked eye.  Unless you're wired very differently than me, this delightful discovery won't rob you of your ability to just enjoy looking at flowers.

Whitman got bored with the learn'd astronomer yammering about his findings.  But if he caught the astronomer on a different night, he'd get to peek through his telescope and see a different view of the sky he found so dazzling, while sharing breaths of the same mystical moist night air with that scholar.  Maybe the astronomer would point his instrument to a different section of the sky that looks empty to the naked eye but is full of thrilling details once you gaze at it through a lens.  Maybe the astronomer would listen to the poet eloquently expressing the beauty of what he was seeing in words, or maybe they'd just stare up at it together in silent appreciation, words and numbers forgotten for the moment.

I humbly submit these tools to the user as an alternative way of seeking beauty and meaning in text.  Let me know if you find anything good.

P.E.S.\
2023-06-30





------------------------------------------------------------------

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
