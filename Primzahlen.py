# Von Frederik Shull, 2017.
max = input("Suche bis: ") # User kann entscheiden bis welche Zahl gesucht werden soll.
max = int(max) # Eingabe wird in einen int-Wert umgewandelt.
zaehler = 0 # Zaehl-Variable wird initialisiert.
for zahl in range(2, max): # Schleife für das Testen bis zum angegebenen Maximum.
    prim = True # Wenn "prim" am Ende immernoch 1 ist, handelt es sich um eine Primzahl.
    output = "%s" % zahl # Ausgabe enthält die aktuelle Zahl.
    for tprim0 in range(1, zahl): # Schleife zum Testen bis zu aktuellen Zahl.
        tprim1 = zahl / tprim0 # Zahl wird geteilt.
        tprim2 = zahl // tprim0 # Zahl wird gerundet geteilt.
        if tprim1 == tprim2 and tprim0 != 1 and tprim0 != zahl: # Wenn ungerundet und gerundet gleich sind und es sich nicht um 1 oder die aktuelle Zahl handelt..
            prim = False # .. ist es keine Primzahl.
    if prim == True: # Wenn sich herausstelt, dass es sich um eine Primzahl handelt..
        zaehler += 1 # .. wird der Zaehler erhöht und..
        output += " / #%s" % zaehler # .. die Zahl wird als Primzahl markiert und mit Zaehler angezeigt.
    print (output) # Ausgabestring wird angezeigt.
