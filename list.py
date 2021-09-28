import random

kleuren = ["oranje" , "blauw" , "groen" , "bruin"]
aantalMenMs = input(f"heeveel verschillende soort M&M's wilt u.\nkies tussen 1 en {len(kleuren)}")
randomKleur = random.choices(kleuren, k=aantalMenMs)

print(kleuren)
print(len(kleuren))
print(randomKleur)

