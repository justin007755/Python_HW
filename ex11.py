print "How old are you?",
age = input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# Study Drills

# Go online and find out what Python’s raw_input does.
# A: This is not used by Python3

# Can you find other ways to use it? Try some of the samples you find.
# A: mydata = raw_input('Prompt :')

# Write another “form” like this to ask some other questions.
# A: age = input('How old are you? ')

# Related to escape sequences, try to find out why the last line has '6\'2"' with that \'
# sequence. See how the single- quote needs to be escaped because otherwise it would end the string?
# A: 这里用的是raw_input()函数，输出本身有一个单引号，所以输入的单引号被转义了。
