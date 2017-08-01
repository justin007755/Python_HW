x = "There are %d types of people." % 10 # 用占位符定义一个变量，表示有多少类型的人
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" #定义存储字符串的变量

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

# Study Drills

# Go through this program and write a comment above each line explaining it.
# A: See above

# Find all the places where a string is put inside a string. There are four places.
# A: 第4，9，10，13行

# Are you sure there are only four places? How do you know? Maybe I like lying.
# A: Yes

# Explain why adding the two strings w and e with + makes a longer string.
# A: +号应用在字符串上表示append
