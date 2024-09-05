from random import randint

anzahl = int(input("Gib die Anzahl der Gäste auf der Party ein: "))

versuche = 0
personen_insg = []

for i in range(10):
    print("Start!")

    gäste = ["Alice", "Bob"]
    for i in range(anzahl):
        gäste.append("nein")

    davor = 1
    runden = 0

    while davor != 0:
        gast = randint(0, len(gäste) - 1)
        while (gast == 0 and runden == 0):
            gast = randint(0, len(gäste) - 1)
        if (gäste[gast] == "ja" or gäste[gast] == "Bob") and runden != 0:
            runden += 1
            print(davor)
            break
        elif gäste[gast] != "ja" and gast != 1 and gast != davor:
            gäste[gast] = "ja"
            davor = gast
            runden += 1
        print(davor)
        print(gäste)
        print()

    print("Das Gerücht wurde " + str(runden) + "-mal weitererzählt.")
    if gäste[0] != "ja":
        print("Es haben " + str(gäste.count("ja")) + " Gäste davon erfahren, ohne dass Alice es mitbekommen hat.")
        personen_insg.append(gäste.count("ja"))
    else:
        print("Alice hat es mitbekommen!")
        print("Vorher konnten es " + str(gäste.count("ja") - 1) + " Gäste erfahren.")
        personen_insg.append(gäste.count("ja") - 1)
    versuche += 1
    print()
    print()

print("Es wird erwartet, dass ungefähr " + str(int(sum(personen_insg) / versuche)) + " Personen davon erfahren.")







