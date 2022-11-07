import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_tilavuus_ei_ole_negatiivinen(self):
        self.varasto = Varasto(-10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)
    
    def test_saldo_on_suurempi_kuin_nolla(self):
        self.varasto = Varasto(10, -5)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_saldo_on_pienempi_kuin_tilavuus(self):
        self.varasto = Varasto(10, 20)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_varastoon_ei_voi_laittaa_liikaa(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_varastosta_ei_voi_ottaa_liikaa(self):
        self.varasto.lisaa_varastoon(10)
        maara = self.varasto.ota_varastosta(20)
        self.assertAlmostEqual(maara, 10)

    def test_varastoon_ei_voi_lisata_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_varastosta_ei_voi_ottaa_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(5)
        maara = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(maara, 0)

    def test_varasto_tulostuu(self):
        self.varasto.lisaa_varastoon(5)
        esimerkki = "saldo = 5, vielä tilaa 5"
        tulos = str(self.varasto.__str__())
        self.assertEqual(tulos, esimerkki)