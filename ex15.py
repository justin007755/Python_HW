from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# Study Drills

# Use only raw_input and try the script that way. Think of why one way of getting the
# filename would be better than another.
# A: 用raw_input()函数可以给用户比较高的自由度来选择文件名，但是对于某些不希望用户交互的程序则采用argv
# 获得文件名比较好
