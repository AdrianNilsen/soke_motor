
# Dokumentasjon for Søkemotor i Python

## Oversikt
Dette dokumentet beskriver implementeringen av en enkel tekstbasert søkemotor i Python. Programmet søker etter et bestemt ord i en tekstfil (`b.txt`), viser linjenummeret og linjeinnholdet der ordet finnes, og gir beskjed hvis ordet ikke eksisterer i filen. Det inkluderer også en funksjon for å telle antall forekomster av ordet.

## Prototyper

### Prototype 1
```python
soke_ord = input("enter a word you want to search in file: ")

if soke_ord in open('b.txt').read():
    print("jeg fant ordet", soke_ord)
else:
    print("ordet er ikke her")
```
#### Forklaring:
Denne første prototypen bruker en enkel metode for å søke etter et ord. Hele innholdet i filen lastes inn og kontrolleres for forekomsten av det angitte søkeordet.

#### Begrensninger:
- Den laster inn hele filen i minnet, noe som kan være ineffektivt for store filer.
- Den gir ingen detaljer om hvor i filen ordet finnes.

---

### Prototype 2
```python
import os

print("Current working directory:", os.getcwd())

try:
    with open("a.txt", "r") as f:
        en = f.readlines()
        print(en)

        for linje in en:
            if "eple" in linje:
                print("Jeg fant et eple")
except FileNotFoundError:
    print("File 'a.txt' not found. Ensure it's in the correct directory.")
except Exception as e:
    print(f"An error occurred: {e}")
```
#### Forklaring:
Den andre prototypen bruker `os`-modulen for å vise gjeldende arbeidsmappe og legger til grunnleggende feilhåndtering for filen `a.txt`. Filen leses linje for linje for å finne ordet "eple".

#### Forbedringer:
- Feilhåndtering ble lagt til for å fange opp feil som oppstår når filen ikke finnes.
- Programmet informerer nå om arbeidsmappen og håndterer manglende filer.

---

### 3. Hovedfunksjonalitet: Søkeord og Filbehandling
```python
soke_ord = input("Skriv inn et ord du vil søke i filen: ")

with open('b.txt', 'r') as fil:
    funnet = False
    for linje_nr, linje in enumerate(fil, start=1):
        if soke_ord in linje:
            print(f"Jeg fant ordet '{soke_ord}' på linje {linje_nr}: {linje.strip()}")
            funnet = True
    if not funnet:
        print(f"Ordet '{soke_ord}' er ikke her.")
```
#### Forklaring:
- Brukeren oppgir et søkeord.
- Filen `b.txt` åpnes og leses linje for linje.
- Hvis ordet finnes, skrives linjenummeret og innholdet til terminalen.
- Hvis ordet ikke finnes, får brukeren beskjed.

#### Potensielle utfordringer:
- **Problem:** Filen `b.txt` mangler eller kan ikke åpnes.
  - **Løsning:** Legg til feilhåndtering for å håndtere manglende filer.

---

### 4. Funksjon: `tellOrd(ord)`
```python
def tellOrd(ord):
    antall = 0
    
    with open('b.txt', 'r') as fil:
        for linje in fil:
            antall += linje.count(ord)
    
    return antall

print(f"Ordet '{soke_ord}' dukker opp {tellOrd(soke_ord)} ganger i b.txt.")
```
#### Forklaring:
- Funksjonen `tellOrd()` tar et søkeord som parameter og teller hvor mange ganger det forekommer i `b.txt`.
- Hver linje i filen sjekkes, og `count()` brukes for å finne antall forekomster.

#### Mulige utfordringer:
- **Problem:** Ord med spesialtegn kan gi feil resultat.
  - **Løsning:** Bruk `strip()` og `lower()` for å normalisere dataene før søket.

---

### Eksempel på Kjøring
```plaintext
Skriv inn et ord du vil søke i filen: python
Jeg fant ordet 'python' på linje 3: Dette er et eksempel på python kode.
Ordet 'python' dukker opp 2 ganger i b.txt.
```

## Forbedringer og Mulige Utvidelser
- **Feilhåndtering:** Utvid programmet med mer detaljert håndtering av feil.
- **Brukervennlighet:** Legg til mer informative meldinger for brukeren.
- **Ytelse:** For store filer kan man bruke regex eller multitrådet prosessering for raskere søk.
