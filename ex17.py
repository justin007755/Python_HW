from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copy from %s to %s" % (from_file, to_file)


in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

# Study Drills

# Windows people, fi nd the alternative to cat that Linux/OSX people have. Do not worry
# about man since there is nothing like that.
# A: For Windows we can use powershell and in that man command can be used.

# Find out why you had to do output.close() in the code.
# A: If you don’t explicitly close a file, Python’s garbage collector will eventually destroy
# the object and close the open file for you, but the file may stay open for a while. Another
# risk is that different Python implementations will do this clean-up at different times.
