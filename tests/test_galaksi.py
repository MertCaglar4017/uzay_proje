import pytest

from uzay_oyunu.oyun import galaksi_kur, galaksi_yukle


def test_galaksi_dosyadan_kurulur():
    g = galaksi_yukle()
    assert g["konum"] == "dünya"
    assert g["yakit"] == 100


def test_varsayilan_yakit_elli():
    assert galaksi_kur(["mars"], {"mars": []}, "mars")["yakit"] == 50


def test_gecersiz_baslangic_hata_verir():
    with pytest.raises(ValueError):
        galaksi_kur(["mars"], {"mars": []}, "venüs")


def test_baglanti_sirasi_ayni_kaldi():
    g = galaksi_yukle()
    assert g["baglantilar"]["dünya"] == ["orion", "centauri"]
    assert g["baglantilar"]["sirius"] == ["dünya", "orion", "centauri", "kara_delik"]