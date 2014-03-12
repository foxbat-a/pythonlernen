from sys import argv

script, user_name = argv
prompt = '> '

print "Hi, %s, I'm %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Na, gut, Sie hat gesagt dass Sie %r moegen mir.
Sie wohnen in %r. Not sure where that is.
Und Sie haben der %r computer. Wunderbar!
""" % (likes, lives, computer)
