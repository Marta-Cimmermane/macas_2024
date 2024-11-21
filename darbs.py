# Uzraksti programmu, kurā  dators izvēlas 100 skaitļus robežās no 101 līdz 500. Izvēlētie skaitļi tiek izvadīti terminālī.
izveletie_skaitli=[]
import random

for i in range(100):
    random_skaitlis=random.randint(101,500,)
    izveletie_skaitli.append(random_skaitlis)    
for skaitli in izveletie_skaitli:
    print(skaitli)
