class Adatok:
    def __init__(self, datum, nagydij, helyezes, befKor, pont, konstruktor, celbaErt, korhatrany, hibaOka):
        self.datum = datum
        self.nagydij = nagydij
        self.helyezes = helyezes
        self.befKor = befKor
        self.pont = pont
        self.konstruktor = konstruktor
        self.celbaErt = celbaErt
        self.korhatrany = korhatrany
        self.hibaOka = hibaOka

adatok = []
sorokszama = 0
hibak = {}
f = open("kimi.csv", "rt", encoding="utf-8")
for sor in f:
    sor = sor.strip().split(";")
    adatok.append(sor)
    
    sorokszama += 1
        
print("3. feladat: adatsorok száma: ", sorokszama - 1)
print(adatok)