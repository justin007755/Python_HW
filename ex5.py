name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
rate = 0.4535924 # Pound/Kilograms

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "He's %d Kilograms heavy." % (weight * rate)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# Study Drills

# Change all the variables so there is no my_ in front of each one. Make sure you change the name everywhere,
# not just where you used = to set them.
# A: Done

# Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do not just type
# in the measurements. Work out the math in Python.
# A: rate = 0.4535924 # Pound/Kilograms

# Search online for all of the Python format characters.
# A: Done

# Try more format characters. %r is a very useful one. It's like saying "print this no matter what."
# A: Tried this through terminal
