import re

from uzay_oyunu.dekoratorler import sure_olc


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