from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
weight = raw_input("How much do you weight? ")
print 'Your weight is %r' % weight

# Study Drills

# Try giving fewer than three arguments to your script. See that error you get? See if you can explain it.
# A: ValueError: need more than 3 values to unpack

# Write a script that has fewer arguments and one that has more. Make sure you give the unpacked variables good names.
# A: Done

# Combine raw_input with argv to make a script that gets more input from a user.
# A: See as above

# Remember that modules give you features, Modules, Modules. Remember this because we'll need it late
# A: Ok
