# The basic syntax is that you need to first create a expression matcher, then search for matches

import re
myRegex = re.compile('fox')
matches = myRegex.search('this is a funky fox and thats another fox')
print(matches.group())                       # returns the first matching group
# More information about the match
print(matches.start())
print(matches.end())
print(matches.span())

# Return all matches

# match() - Determine if the RE matches at the beginning of the string.
# search() - Scan through a string, looking for any location where this RE matches.
# findall() - Find all substrings where the RE matches, and returns them as a list.
# finditer() - Find all substrings where the RE matches, and returns them as an iterator.

