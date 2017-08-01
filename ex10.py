tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
#backslash_cat = "I'm \\ a \\ cat."
backslash_cat = "u'\U0001F47E'"

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\r\t* Grassh
\a
\a
u'\U0001F47E'
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print "This is good \t %r: " % tabby_cat

#while True:
#    for i in ["/","-","|","\\","I"]:
#        print "%r\r" % i,

# Study Drills

# Memorize all the escape sequences by putting them on flash cards.
# A: Ok

# Use ''' (triple- single- quote) instead. Can you see why you might use that instead of """?
# A: the same

# Combine escape sequences and format strings to create a more complex format.
# A: Ok.

# Remember the %r format? Combine %r with double- quote and single- quote escapes and
# print them out. Compare %r with %s. Notice how %r prints it the way you’d write it in
# your fi le, but %s prints it the way you’d like to see it?
# A: Done
