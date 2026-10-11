from uzay_oyunu.araclar import en_bagli_gezegenler, hamle_sayaci, sure_olc
from uzay_oyunu.oyun import galaksi_yukle


def test_hamle_sayaci_artar():
    sayac = hamle_sayaci()
    assert sayac() == 1
    assert sayac() == 2
    assert sayac() == 3


def test_sayaclar_birbirinden_bagimsiz():
    a = hamle_sayaci()
    b = hamle_sayaci()
    a()
    a()
    assert b() == 1


def test_en_bagli_gezegenler():
    g = galaksi_yukle()
    beklenen = ["sirius", "centauri", "dünya", "orion", "kara_delik"]
    assert en_bagli_gezegenler(g) == beklenen


def test_esitlikte_alfabetik_sirala():
    g = {
        "gezegenler": ["b", "a", "c"],
        "baglantilar": {"a": ["b"], "b": ["a"], "c": []},
    }
    assert en_bagli_gezegenler(g) == ["a", "b", "c"]

    

def test_sure_olc_sonucu_degistirmez(capsys):
    olculen = sure_olc(en_bagli_gezegenler)
    g = galaksi_yukle()
    assert olculen(g) == en_bagli_gezegenler(g)
    assert "saniyede çalıştı" in capsys.readouterr().out