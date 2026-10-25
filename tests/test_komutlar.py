import pytest

from uzay_oyunu.komutlar import KOMUTLAR, envanter, harita, komut, yardim
from uzay_oyunu.oyun import travel

DURUM = {
    "konum": "sirius",
    "baglantilar": {"sirius": ["orion", "dünya", "kara_delik"]},
    "credits": True,
    "engines": False,
    "copilot": True,
}


def test_uc_komut_kayitli():
    assert sorted(KOMUTLAR) == ["envanter", "harita", "yardim"]


def test_komut_fonksiyonu_degistirmez():
    assert KOMUTLAR["yardim"][0] is yardim
    assert KOMUTLAR["envanter"] == (envanter, "eşyalarını gösterir")
    assert KOMUTLAR["harita"] == (harita, "gidebileceğin gezegenleri gösterir")


def test_yardim_komutlari_listeler():
    beklenen = (
        "envanter eşyalarını gösterir\n"
        "harita gidebileceğin gezegenleri gösterir\n"
        "yardim komutları listeler"
    )
    assert yardim(DURUM) == beklenen


def test_envanter_komutu():
    assert envanter(DURUM) == "Sende: bol kredi, yetenekli bir pilot"
    bos = {**DURUM, "credits": False, "copilot": False}
    assert envanter(bos) == "Hiçbir eşyan yok."


def test_harita_komutu():
    assert harita(DURUM) == "orion, dünya, kara_delik"


def test_ayni_ad_iki_kez_kullanilamaz():
    @komut("deneme", "ilk")
    def ilk(durum):
        return "ilk"

    try:
        with pytest.raises(ValueError):

            @komut("deneme", "ikinci")
            def ikinci(durum):
                return "ikinci"

    finally:
        del KOMUTLAR["deneme"]
    assert "deneme" not in KOMUTLAR


def test_travel_komutlari_calistirir(monkeypatch, capsys):
    cevaplar = iter(["yardim", "harita", "2", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(cevaplar))
    assert travel() == "kara_delik"
    cikti = capsys.readouterr().out
    assert "yardim komutları listeler" in cikti
    assert "centauri, sirius" in cikti
    assert cikti.count("[1] centauri\n[2] sirius") == 3
    assert "Oyunu 2 hamlede bitirdin!" in cikti