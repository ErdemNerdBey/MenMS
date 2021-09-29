import random
MenMs = ['oranje', 'blauw', 'groen', 'bruin']
zak = []
zakDict = {'oranje': 0, 'blauw': 0,'groen': 0, 'bruin':0,}
hoeveelkleuren = 0

def sorteersysteem():
    if kleur == 'oranje':
        zakDict['oranje'] += 1
    elif kleur == 'blauw':
        zakDict['blauw'] += 1
    elif kleur == 'groen':
        zakDict['groen'] += 1
    elif kleur == 'bruin':
        zakDict['bruin'] += 1

def randomkleur():
    global hoeveelkleuren
    f = True
    while f:
        try:
            hoeveelkleuren = int(input("Hoeveel M&M's moeten er aan deze zak worden toegevoegd?\n"))
            if int(hoeveelkleuren) <= 0:
                print('Dat is geen getal boven nul!')
        except ValueError:
            print('Dat is geen geldige invoer!')
        if hoeveelkleuren > 0:
            f = False

    for i in range(hoeveelkleuren):
        global getal
        getal = random.choice(range(0, 4))
        global kleur
        kleur = MenMs[getal]
        zak.append(kleur)
        sorteersysteem()

randomkleur()

print(zak)
for key, value in zakDict.items():
    print(key, value)
print(len(zak))