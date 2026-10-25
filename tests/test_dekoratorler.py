import re

import pytest

from uzay_oyunu.araclar import yakit_harca
from uzay_oyunu.dekoratorler import log_cagri, say, sinirla, sure_olc
from uzay_oyunu.fib_deneyi import fib_lru_ustte, fib_say_ustte, fib_yalniz_say
from uzay_oyunu.oyun import galaksi_kur, hedef_menusu


@sure_olc
def topla(a, b=0):
    """İki sayıyı toplar."""
    return a + b


def test_sure_olc_sonucu_degistirmez(capsys):
    assert topla(2, 3) == 5
    cikti = capsys.readouterr().out.strip()
    assert re.fullmatch(r"topla: \d+\.\d{4} sn", cikti)


def test_sure_olc_adli_argumanlarla_calisir(capsys):
    assert topla(a=2, b=5) == 7
    assert topla(4, b=1) == 5
    assert capsys.readouterr().out.count("topla: ") == 2


def test_sure_olc_ad_ve_belge_korunur():
    assert topla.__name__ == "topla"
    assert topla.__doc__ == "İki sayıyı toplar."


def test_say_cagri_sayar():
    @say
    def selam():
        return "merhaba"

    assert selam.cagri == 0
    assert selam() == "merhaba"
    selam()
    selam()
    assert selam.cagri == 3


def test_say_ad_ve_belge_korunur():
    @say
    def selam():
        """Selam verir."""
        return "merhaba"

    assert selam.__name__ == "selam"
    assert selam.__doc__ == "Selam verir."


def test_fib_yalniz_say_cagri_sayisi():
    assert fib_yalniz_say(20) == 6765
    assert fib_yalniz_say.cagri == 21891


def test_fib_say_ustte_cagri_sayisi():
    assert fib_say_ustte(20) == 6765
    assert fib_say_ustte.cagri == 39


def test_fib_lru_ustte_cagri_sayisi():
    assert fib_lru_ustte(20) == 6765
    assert fib_lru_ustte.__wrapped__.cagri == 21


def test_log_cagri_konumsal_ve_adli_argumanlar(capsys):
    @log_cagri
    def yolculuk(gezegen, hiz=1):
        return f"{gezegen} hiz={hiz}"

    assert yolculuk("orion", hiz=3) == "orion hiz=3"
    satirlar = capsys.readouterr().out.splitlines()
    assert satirlar == ["-> yolculuk('orion', hiz=3)", "<- yolculuk = 'orion hiz=3'"]


def test_log_cagri_sadece_konumsal_argumanlar(capsys):
    @log_cagri
    def carp(a, b):
        return a * b

    assert carp(2, 3) == 6
    assert capsys.readouterr().out.splitlines() == ["-> carp(2, 3)", "<- carp = 6"]


def test_log_cagri_ad_ve_belge_korunur():
    @log_cagri
    def selam():
        """Selam verir."""
        return "merhaba"

    assert selam.__name__ == "selam"
    assert selam.__doc__ == "Selam verir."


def test_log_cagri_hata_yayilir(capsys):
    @log_cagri
    def bol(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        bol(1, 0)
    assert capsys.readouterr().out.splitlines() == ["-> bol(1, 0)"]


def test_hedef_menusu_loglanir(capsys):
    menu = hedef_menusu(["a", "b"])
    cikti = capsys.readouterr().out
    assert "-> hedef_menusu(['a', 'b'])" in cikti
    assert menu == "Nereye gitmek istersin?\n[1] a\n[2] b"
    assert hedef_menusu.__name__ == "hedef_menusu"


def test_galaksi_kur_loglanir(capsys):
    galaksi_kur(["mars"], {"mars": []}, "mars")
    cikti = capsys.readouterr().out
    assert "-> galaksi_kur(['mars'], {'mars': []}, 'mars')" in cikti
    assert "<- galaksi_kur = " in cikti


def test_sinirla_aralik_icinde_calisir():
    assert yakit_harca(30) == 70


def test_sinirla_sinir_degerleri():
    assert yakit_harca(0) == 100
    assert yakit_harca(100) == 0


def test_sinirla_aralik_disi_deger_hata_verir():
    mesaj = "yakit_harca: 150 değeri 0-100 aralığında değil"
    with pytest.raises(ValueError, match=mesaj):
        yakit_harca(150)
    with pytest.raises(ValueError, match="yakit_harca: -1 değeri 0-100 aralığında değil"):
        yakit_harca(-1)
    with pytest.raises(ValueError):
        yakit_harca(101)


def test_sinirla_adli_arguman():
    assert yakit_harca(miktar=30) == 70
    with pytest.raises(ValueError):
        yakit_harca(miktar=150)


def test_sinirla_farkli_aralik():
    @sinirla(1, 5)
    def kare(n):
        return n * n

    assert kare(5) == 25
    with pytest.raises(ValueError, match="kare: 6 değeri 1-5 aralığında değil"):
        kare(6)


def test_sinirla_ad_ve_belge_korunur():
    assert yakit_harca.__name__ == "yakit_harca"
    assert yakit_harca.__doc__ == (
        "Depodaki 100 birimlik yakıttan miktar kadarını harcar, kalanı döndürür."
    )