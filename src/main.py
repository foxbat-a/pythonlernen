C_KILOS_IN_POUND = 0.45359237
C_CMS_IN_FOOT = 30.48

my_name = 'Alex P. Art'
my_age = 30 # keine Luege
my_height = 188
my_weight = 88
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Schwarz'

my_weight_pounds = my_weight / C_KILOS_IN_POUND
my_height_feet = my_height / C_CMS_IN_FOOT


print "Let's talk about %s" % my_name
print "He's %s cm (%s feet) tall" % (my_height, my_height_feet)
print "He's %s kilo (%s pounds) heavy" % (my_weight, my_weight_pounds)
print "Actually, that's not too heavy."
print "he's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s, depending on coffee" % my_teeth

# and now... 
print "If I add %d, %d and %d, I get %d" % (
        my_age, my_height, my_weight, my_age + my_height + my_weight)