def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "Sie haben %d Stuecke Kaese!" % cheese_count
    print "Sie haben %d Kaesten Gebaeck!" % boxes_of_crackers
    print "Es ist genug, um Party zu machen!"
    print "Das machen wir!\n"
    
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or we can use variables from script:"
amt_cheese = 10
amt_crackers = 50

cheese_and_crackers(amt_cheese, amt_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amt_cheese + 100, amt_crackers + 1000)