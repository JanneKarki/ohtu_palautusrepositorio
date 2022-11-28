import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.piima = Tuote("Piimä", 4)

        self.kori_2_eri_tuotetta = Ostoskori()
        self.kori_2_eri_tuotetta.lisaa_tuote(self.maito)
        self.kori_2_eri_tuotetta.lisaa_tuote(self.piima)

        self.kori_2_samaa_tuotetta = Ostoskori()
        self.kori_2_samaa_tuotetta.lisaa_tuote(self.maito)
        self.kori_2_samaa_tuotetta.lisaa_tuote(self.maito)
        

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(),0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_on_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_2_tavaraa(self):
        self.assertEqual(self.kori_2_eri_tuotetta.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hintojen_summa(self):
        self.assertEqual(self.kori_2_eri_tuotetta.hinta(), self.maito._hinta+self.piima._hinta)

    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_2_tavaraa(self):
        self.assertEqual(self.kori_2_samaa_tuotetta.tavaroita_korissa(),2)

    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_sama_kuin_2_x_tuotteen_hinta(self):
        self.assertEqual(self.kori_2_samaa_tuotetta.hinta(),self.maito._hinta*2)

    def test_yhden_tuotteen_lisäämisen_jälkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisäämisen_jälkeen_sis_ostoksen_jolla_sama_nimi_ja_lukumäärä_1(self):
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].hinta(), 3)

    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_kaksi_ostosta(self):
        ostokset = self.kori_2_eri_tuotetta.ostokset()
        self.assertEqual(len(ostokset),2)

  #  def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_yhden_ostoksen(self):
   #     ostokset = self.kori_2_samaa_tuotetta.ostokset()
    #    self.assertEqual(len(ostokset),1)

    def test_kahden_saman_tuotteen_lis_jälk_kori_sis_ostoksen_jolla_sama_nimi_kuin_tuotteella_ja_lukum_2(self):
        ostokset = self.kori_2_samaa_tuotetta.ostokset()
        #self.assertEqual(ostokset)

    def test_tyhjenna_kori(self):
        self.kori_2_eri_tuotetta.tyhjenna()
        self.assertEqual(self.kori_2_eri_tuotetta.ostos_oliot, [])

    