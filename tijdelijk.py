#7.15.2 Dictionary prijzen
prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}
#7.15.3 Factor
korting_factor=0.8
#7.15.3 Aanbieding
aanbieding=(prijzen ["aardbei"]*korting_factor)

#7.15.4 Reclame zin
reclame_tekst= "Vandaag in de aanbieding: aardbeien-ijs, 1 liter - slechts € "
reclame=(f"{reclame_tekst}{aanbieding}")

#7.15.5 Inkorten reclame tekst
reclame_tekst2=reclame[:65]

#7.15.6 Sportvliegtuig banner in HOOFDLETTERS
reclame_tekst3=reclame_tekst2.upper()

#7.15.7 Reclame tekst in een list
reclame_tekst4=reclame_tekst3.split(" ")

#7.15.8 Tekst: woord per regel
#for el in reclame_tekst4:
#    print(el)
#print()

#7.15.9 Tekst: In kleine letters
#for el in reclame_tekst4:
#    el=el.lower()
#    print(el)
#print()

#7.15.10 Tekst: In kleine (<5) en hoofd letters (>=5)
for el in reclame_tekst4:
    x=len(el)
    if len(el) >=5:
        el=el.upper()
        print(el)
    else:
        el=el.lower()
        print(el)