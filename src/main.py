from sys import argv

script, filename = argv

txt = open(filename)

print "Da ist Ihre Datei, %r:" % filename
print txt.read()

print "Eingeben Sie den Dateinamen noch einmal: "
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()