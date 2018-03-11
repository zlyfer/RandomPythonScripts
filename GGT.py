# Von Frederik Shull, 2017.
def blah(zahl1, zahl2, max): # Funktion: Zahl1 Zahl2 KleinereVonBeiden(Maximum)
    zaehler = 0 # Zum zählen aller gemeinsamen Teiler.
    for i in range(1, max): # Schleife von 1 bis zur kleinsten Zahl der beiden angegeben.
        t00 = zahl1 / i # Zahl1 ungerundet.
        t01 = zahl1 // i # Zahl1 gerundet.
        t10 = zahl2 / i # Zahl2 ugnerundet.
        t11 = zahl2 // i # Zahl2 gerundet.
        if t00 == t01 and t10 == t11: # Wenn Zahl1 gerundet und ungerundet gleich sind und Zahl2 gerundet und ungerundet gleich sind..
            gemteiler = i # .. dann Zahl speichern.
            zaehler += 1 # +1 gemeinsamer Teiler.
    print ("Anzahl an gemeinsamen Teilern: %s" % zaehler) # Ausgabe der Anzahl an gemeinsamen Teilern.
    print ("Größter gemeinsamer Teiler: %s" % gemteiler) # Ausgabe des höchsten gemeinsamen Teilers.
zahl1 = int(input("Zahl 1: ")) # Eingabe Zahl1.
zahl2 = int(input("Zahl 2: ")) # Eingabe Zahl2.
if zahl1 < zahl2: # Entscheidung welche der beiden Zahlen am kleinsten ist um sie als Maximum zu setzen.
    blah(zahl1, zahl2, zahl1)
elif zahl2 < zahl1:
    blah(zahl1, zahl2, zahl2)
else:
    blah(zahl1, zahl2, zahl1)
