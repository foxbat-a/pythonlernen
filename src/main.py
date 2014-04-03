from sys import argv
from os.path import exists

script, from_datei, to_datei = argv

in_datei = open(from_datei)
indata = in_datei.read()

print "Die Datei ist %d Bytes gross" % len(indata)

print "Ob die Ausgabedatei verfuegbar ist? %r" % exists(to_datei)

print "Fertig, druecken Sie Enter um fortzufahren oder druecken Sie Strg+C um abzubrechen."

raw_input()

out_datei = open(to_datei, 'w')
out_datei.write(indata)

print "Gut gemacht, alles ist erledigt."

out_datei.close()
in_datei.close()