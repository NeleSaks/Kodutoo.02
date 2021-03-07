# Nele Saks ITT20
# 30.01.2021
# Kodutöö 02

from random import randint

# 1.Bussid
inimesed = int(float(input("Inimeste arv: ")))
kohtadearv = int(float(input("Kohtade arv: ")))
buss = 0
viimases = 0
if (inimesed%kohtadearv==0):
    buss=inimesed // kohtadearv
    viimases = kohtadearv
else:
    buss=inimesed // kohtadearv +1
    viimases = inimesed%kohtadearv
print("Busse vaja", buss)
print("Viimases bussis inimesi:", viimases)
print()

# 2.Äratus
äratus = int(float(input("Sisestage mitu korda äratada: ")))
for i in range(äratus):
    print("Tõuse ja sära!", end=" ")
    print()
print()

# 3.Murelikud lapsevanemad
ringid = int(input("Sisesta ringide arv: "))
loendur = 0
porgandid = 0
while loendur<=ringid:
    if loendur %2 == 0:
        porgandid = porgandid+loendur
    loendur = loendur+1
print("Porgandite koguarv on",porgandid)
    
    

print()

# 4.Täringud
täringud = int(float(input("Täringute arv: ")))
for i in range(täringud):
    value = randint(1,6)
    print(value)
print()
    
# 5.Õunad
pöialpoisid = int(float(input("Mitu pöialpossi tahab õuna? ")))
õunad = 14
lumivalgekeseõun = 0
summa = 0
for i in range(pöialpoisid):
    pöialpoisiõun = randint(1,2)
    summa = summa + pöialpoisiõun
    print(pöialpoisiõun)
lumivalgekeseõun = õunad - summa
print("Lumivalgekesele jäi" ,lumivalgekeseõun)
print()




