from sys import argv

script, user_name, food = argv
prompt = '# '

print "Hi %s, I'm the %s script, and I'm eating %s" % (user_name, script, food)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

# Study Drills

# Find out what Zork and Adventure were. Try to fi nd a copy and play it.
# A: Done

# Change the prompt variable to something else entirely.
# A: Done as above

# Add another argument and use it in your script.
# A: Done as above

# Make sure you understand how I combined a """ style multiline string with the % format
# activator as the last print.
# A: Remember that
