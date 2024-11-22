soke_ord = input("Skriv inn et ord du vil søke i filen: ")
 
with open('b.txt', 'r') as fil:
    funnet = False
    for linje_nr, linje in enumerate(fil, start=1):
        if soke_ord in linje:
            print(f"Jeg fant ordet '{soke_ord}' på linje {linje_nr}: {linje.strip()}")
            funnet = True
    if not funnet:
        print(f"Ordet '{soke_ord}' er ikke her.")
 
def tellOrd(ord):
    
    antall = 0
   
    
    with open('b.txt', 'r') as fil:
        for linje in fil:
            antall += linje.count(ord)
            return antall
 


print(f"Ordet '{soke_ord}' dukker opp {tellOrd(soke_ord)} ganger i b.txt.")