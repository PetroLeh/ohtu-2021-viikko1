import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uuden_varaston_tilavuus_ei_voi_olla_negatiivinen(self):
        nega = Varasto(-1)
        self.assertAlmostEqual(nega.tilavuus, 0)

    def test_alkusaldo_ei_voi_olla_negatiivinen(self):
        nega = Varasto(0, -1)
        self.assertAlmostEqual(nega.saldo, 0)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-1)
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

    def test_varastoon_ei_voi_laittaa_liikaa(self):
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_varastosta_ei_voi_oottaa_liikaa(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(3)
        self.assertAlmostEqual(saatu_maara, 3)

        saatu_maara = self.varasto.ota_varastosta(3)
        self.assertAlmostEqual(saatu_maara, 2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varastosta_ei_voi_ottaa_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(5)

        maara = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(maara, 0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_stringtesti(self):
        self.varasto.lisaa_varastoon(5)
        
        self.assertEqual(self.varasto.__str__(), "saldo = 5, vielä tilaa 5")