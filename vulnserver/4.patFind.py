#!/usr/bin/python2


# script 4.uniqChars.py populates EIP with the value: 396F4338
# 396F4338 is 8 (38), C (43), o (6F), 9 (39)
# we search for 8Co9
# this should positioned 2006 characters into the pattern


pattern = raw_input("Enter complete unique character pattern ")
to_locate = raw_input("Enter pattern to be located ")
results = pattern.find(to_locate)
print "Your pattern is located at",results
