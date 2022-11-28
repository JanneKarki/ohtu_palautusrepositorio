from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostos_oliot = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        tavarat = 0
        for ostos in self.ostos_oliot:
            tavarat += ostos.lukumaara()

        return tavarat
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0
        for ostos in self.ostos_oliot:
            summa += ostos.hinta()
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
                    self.ostos_oliot.append(Ostos(lisattava))
     
      
            


    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        self.ostos_oliot = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostos_oliot
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
