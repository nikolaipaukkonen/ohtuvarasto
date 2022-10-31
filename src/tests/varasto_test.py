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

    def test_negatiivinen_lisaaminen_ei_toimi(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.saldo, 0)

    def test_negatiivinen_ota_ei_toimi(self):
        self.assertEqual(self.varasto.ota_varastosta(-1), 0)

    def test_str_palauttaa_oikein(self):
        self.assertEqual(self.varasto.__str__(), f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")

    def test_lisaa_liikaa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_ota_varastosta_liikaa(self):
        self.assertEqual(self.varasto.ota_varastosta(100), self.varasto.saldo)

    def test_setUp_negatiivinen_tilavuus(selfia):
        self.varasto_nega = Varasto(-1)
        self.assertEqual(self.varasto_nega.tilavuus, 0)

    def test_setUp_negatiivinen_alkusaldo(self):
        self.varasto_nega_saldo = Varasto(10, -1)
        self.assertEqual(self.varasto_nega_saldo.saldo, 0)
