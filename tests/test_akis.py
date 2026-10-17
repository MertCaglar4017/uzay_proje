import inspect
from itertools import islice, takewhile
from pathlib import Path

import pytest

from uzay_oyunu.akis import (
    ayristir,
    fibonacci,
    rota_sayaci,
    rota_sayaci_onbelleksiz,
    satirlari_oku,
    uzun_yolculuklar,
    yakit_gostergesi,
)
from uzay_oyunu.oyun import galaksi_yukle

SEYIR = Path(__file__).parent.parent / "veri" / "seyir.txt"


def test_fibonacci_next_ile_ilk_uc_deger():
    g = fibonacci()
    assert (next(g), next(g), next(g)) == (0, 1, 1)


def test_fibonacci_islice_ile_ilk_12_deger():
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert list(islice(fibonacci(), 12)) == beklenen


def test_fibonacci_takewhile_ile_100den_kucukler():
    kucukler = list(takewhile(lambda x: x < 100, fibonacci()))
    assert kucukler == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_fibonacci_uretec_tek_kullanimlik():
    g = fibonacci()
    ilk = list(islice(g, 5))
    ikinci = list(islice(g, 5))
    assert ilk == [0, 1, 1, 2, 3]
    assert ikinci == [5, 8, 13, 21, 34]
    assert ilk != ikinci


def test_yakit_gostergesi_liste():
    assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]


def test_yakit_gostergesi_bitince_stopiteration():
    g = yakit_gostergesi(10, 10)
    assert next(g) == 0
    with pytest.raises(StopIteration):
        next(g)


def test_satirlari_oku_yorum_satirini_atlar():
    satirlar = list(satirlari_oku(SEYIR))
    assert len(satirlar) == 6
    assert satirlar[0] == "dünya -> sirius 12"
    assert not any(satir.startswith("#") for satir in satirlar)


def test_satirlari_oku_bos_satirlari_atlar(tmp_path):
    dosya = tmp_path / "deneme.txt"
    dosya.write_text("a -> b 1\n\n# not\nb -> a 2\n", encoding="utf-8")
    assert list(satirlari_oku(dosya)) == ["a -> b 1", "b -> a 2"]


def test_ayristir_demet_uretir():
    ilk = next(ayristir(satirlari_oku(SEYIR)))
    assert ilk == ("dünya", "sirius", 12)


def test_toplam_yakit():
    kayitlar = ayristir(satirlari_oku(SEYIR))
    assert sum(y for _, _, y in kayitlar) == 88


def test_uzun_yolculuklar():
    kayitlar = ayristir(satirlari_oku(SEYIR))
    hedefler = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
    assert hedefler == ["sirius", "centauri", "orion", "kara_delik"]


def test_boru_hatti_tembel():
    satirlar = satirlari_oku(SEYIR)
    kayitlar = ayristir(satirlar)
    uzunlar = uzun_yolculuklar(kayitlar, 10)
    assert inspect.isgenerator(satirlar)
    assert inspect.isgenerator(kayitlar)
    assert inspect.isgenerator(uzunlar)


def test_rota_sayisi_pdf_ornekleri():
    say = rota_sayaci(galaksi_yukle()["baglantilar"])
    assert say("dünya", 3) == 9
    assert say("dünya", 10) == 2185
    assert say("dünya", 40) == 16832258606399


def test_rota_sayisi_sifir_adim():
    say = rota_sayaci(galaksi_yukle()["baglantilar"])
    assert say("dünya", 0) == 1


def test_rota_sayisi_kucuk_harita():
    baglantilar = {"a": ["b", "c"], "b": ["c"], "c": ["a"]}
    say = rota_sayaci(baglantilar)
    assert say("a", 2) == 2
    assert say("a", 3) == 3


def test_onbellek_isabet_sayisi_artar():
    say = rota_sayaci(galaksi_yukle()["baglantilar"])
    say("dünya", 10)
    ilk = say.cache_info().hits
    say("dünya", 10)
    assert say.cache_info().hits > ilk


def test_onbellekli_ve_onbelleksiz_ayni_sonuc():
    baglantilar = galaksi_yukle()["baglantilar"]
    onbellekli = rota_sayaci(baglantilar)
    onbelleksiz = rota_sayaci_onbelleksiz(baglantilar)
    assert onbellekli("dünya", 8) == onbelleksiz("dünya", 8)