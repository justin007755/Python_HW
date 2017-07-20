tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
#backslash_cat = "I'm \\ a \\ cat."
backslash_cat = "u'\U0001F47E'"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\r\t* Grassh
\a
\a
u'\U0001F47E'
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print "This is good \t %r: " % tabby_cat

#while True:
#    for i in ["/","-","|","\\","I"]:
#        print "%r\r" % i,
