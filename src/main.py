from sys import argv

# lesen die Parameter...
script, filename = argv

# zeigen die kurze Einladung...
print "Die Datei %r wurde geleernt" % filename
print "Druecken Sie Strg+C wenn Sie keine Lust darauf haben."
print "Druecken Sie Enter andernfalls."

# warten auf die Entscheidung des Benutzers
raw_input("?")

# oeffnen die Datei...
print "Die Datei wird geoeffnet..."
target = open(filename, 'w')

# Jetzt wird die Datei geleernt
print "Die Datei wird geleernt. Auf Wiedersehen!"
target.truncate()

# Noch eine Einladung...
print "Drei Zeilen muessen jetzt eingegeben werden:"

# Hier soll Benutzer drei kurze Zeilen eingeben
line1 = raw_input("Erste Zeile: ")
line2 = raw_input("Zweite Zeile: ")
line3 = raw_input("Dritte Zeile: ")

# Benutzer muss immer informiert werden :)
print "Jetzt sollen wir diese Zeilen in der Datei speichern..."

# Speichern die Zeilen...
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Die Datei wird verschlossen...
print "Schliesslich muss die Datei verschlossen werden."
target.close()