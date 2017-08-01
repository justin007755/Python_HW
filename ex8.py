# -*- coding: utf-8 -*-
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter,)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
print "%s" % u"好"

# Study Drills

# Do your checks, write down your mistakes, and try not to make the same mistakes on the next exercise.
# A: Ok

# Notice that the last line of output uses both single-quotes and double-quotes for individual pieces.
# Why do you think that is?
# A: 双引号里可以带单引号
