def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "Sie haben %d Stuecke Kaese!" % cheese_count
    print "Sie haben %d Kaesten Gebaeck!" % boxes_of_crackers
    print "Es ist genug, um Party zu machen!"
    print "Das machen wir!\n"
    
print "Zuerst, koennen wir Zahlen benutzen:"
cheese_and_crackers(20, 30)

print "Dann koennen wir Variable von Skript verwenden:"
amt_cheese = 10
amt_crackers = 50

cheese_and_crackers(amt_cheese, amt_crackers)

print "Dann koennen wir ein bisschen Mathe verwenden:"
cheese_and_crackers(10 + 20, 5 + 6)

print "Endlich, koennen wir Mathe und Variable mischen:"
cheese_and_crackers(amt_cheese + 100, amt_crackers + 1000)