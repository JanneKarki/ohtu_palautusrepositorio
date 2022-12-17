from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


class Tehdas:
    def __init__(self):
        self.kps_tekoaly = Tekoaly()
        self.kps_parempi_tekoaly = TekoalyParannettu(10)


    def luo_peli(self, tyyppi):
        if tyyppi == 'a':
            return KPSPelaajaVsPelaaja()
        if tyyppi == 'b':
            return KPSTekoaly(self.kps_tekoaly)
        if tyyppi == 'c':
            return KPSParempiTekoaly(self.kps_parempi_tekoaly)

        return None

    
