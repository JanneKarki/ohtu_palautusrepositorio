KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self.aseta_kapasiteetti(kapasiteetti)
        self.kasvatuskoko = self.aseta_kasvatuskoko(kasvatuskoko)
        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def aseta_kapasiteetti(self, kapasiteetti):
        if not kapasiteetti:
            return KAPASITEETTI
        elif not self.kelvollinen_syote(kapasiteetti):
            raise Exception("Epäkelpo kapasiteetti")
        else:
            return kapasiteetti

    def aseta_kasvatuskoko(self, kasvatuskoko):
        if not kasvatuskoko:
            return OLETUSKASVATUS
        elif not self.kelvollinen_syote(kasvatuskoko):
            raise Exception("Epäkelpo kasvatuskoko")
        else:
            return kasvatuskoko

    def kelvollinen_syote(self, input):
        if not isinstance(input, int) or input < 0:
            return False
        return True

    def kuuluu(self, luku):
        if luku in self.lukujono:
            return True
        return False

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return False
        else:
            self.lukujono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm = self.alkioiden_lkm + 1
        if self.alkioiden_lkm == len(self.lukujono):
            self.kasvata()
            return True

    def kasvata(self):
        taulukko_old = self.lukujono
        self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_taulukko(taulukko_old, self.lukujono)

    def poista(self, luku):
        if self.kuuluu(luku):
            self.lukujono.remove(luku)
            self.alkioiden_lkm -= 1
            return True
        return False
    

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm
        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]
        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            yhdiste.lisaa(luku)

        for luku in b_taulu:
            yhdiste.lisaa(luku)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for a in a_taulu:
            for b in b_taulu:
                if a == b:
                    leikkaus.lisaa(b)

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            erotus.lisaa(luku)

        for luku in b_taulu:
            erotus.poista(luku)

        return erotus

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tulos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tulos += str(self.lukujono[i])
                tulos += ", "
            tulos += str(self.lukujono[self.alkioiden_lkm - 1])
            tulos +=  "}"
            return tulos
