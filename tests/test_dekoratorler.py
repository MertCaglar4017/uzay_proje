import re

from uzay_oyunu.dekoratorler import say, sure_olc
from uzay_oyunu.fib_deneyi import fib_lru_ustte, fib_say_ustte, fib_yalniz_say


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