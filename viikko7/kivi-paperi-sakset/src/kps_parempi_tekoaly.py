from kivi_paperi_sakset import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self, parempi_tekoaly):
        self.tekoaly = parempi_tekoaly

    def _toisen_siirto(self, siirto):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self.tekoaly.aseta_siirto(siirto)
        return siirto
