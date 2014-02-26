tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I\'ll do a list:
\t* Cat food
\t* Fischies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

v_cat = '"\'cat"'
v_dog="Le'\"dog"

print 'Imma %s %r' % (v_cat, v_cat)
print 'Imma %s %r' % (v_dog, v_dog)
print "Imma %s %r" % (v_cat, v_cat)
print "Imma %s %r" % (v_dog, v_dog)