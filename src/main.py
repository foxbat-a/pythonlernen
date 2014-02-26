from sys import argv

tmp_array=argv
if len(argv) < 4:
    for i in range(len(argv), 4):
        tmp_array.append(raw_input("Enter argument #%d" % i))
elif len(argv) > 4:
    tmp_array=tmp_array[0:4]
    
script, erste, zweite, dritte = tmp_array

print "Das skript wird bearbeitet: ", script
print "Ihre erste Variable: ", erste
print "Ihre zweite Variable: ", zweite
print "Und Ihre dritte Variable: ", dritte