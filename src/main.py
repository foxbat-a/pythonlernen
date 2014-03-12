from sys import argv

# hier muss nur ein Parameter sein
script, filename = argv

# offnen die Datei
txt = open(filename)

# zeigen der Inhalt der Datei
print "Da ist Ihre Datei, %r:" % filename
print txt.read()

# verschliessen die Datei...
txt.close()

# fragen den Namen die Datei an...
print "Eingeben Sie den Dateinamen noch einmal: "
file_again = raw_input("> ")

# offnen die Datei noch einmal...
txt_again = open(file_again)

# zeigen der Inhalt der zweiten Datei
print txt_again.read()

# verschliessen die Datei
txt_again.close()