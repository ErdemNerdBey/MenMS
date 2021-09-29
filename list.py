import random

kleuren = ["oranje" , "blauw" , "groen" , "bruin"]
zakMenMs = list()
aantalMenMs = 0


def vulzak():
        try:
            global aantalMenMs
            aantalMenMs = int(input(f"Hoeveel M&M's wilt u?\n"))
            if int(aantalMenMs) < 0:
                print("Kies een hogere getal dan 0.")
                vulzak(1)
            else:
                for i in range(aantalMenMs):
                    randomKleur = random.choices(kleuren)
                    zakMenMs.append(randomKleur)
        except ValueError:
            print("Dit is geen geldige invoer.\nVoer een hele getal in")
            vulzak()
    

vulzak()

print(zakMenMs)
if len(zakMenMs) == 0:
    print(f"u heeft {len(zakMenMs)} M&M's in uw zak.\nDat is wel een hele kleine zak!!")
else:
    print(f"u heeft {len(zakMenMs)} M&M's in uw zak")
