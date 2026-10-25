from functools import lru_cache

from uzay_oyunu.dekoratorler import hafiza, say


def test_hafiza_sonuclar_lru_cache_ile_ayni():
    @hafiza()
    def fib_h(n):
        return n if n < 2 else fib_h(n - 1) + fib_h(n - 2)

    @lru_cache(maxsize=None)
    def fib_l(n):
        return n if n < 2 else fib_l(n - 1) + fib_l(n - 2)

    for n in range(26):
        assert fib_h(n) == fib_l(n)


def test_hafiza_cagri_sayisi_lru_cache_ile_ayni():
    @hafiza()
    @say
    def fib_h(n):
        return n if n < 2 else fib_h(n - 1) + fib_h(n - 2)

    @lru_cache(maxsize=None)
    @say
    def fib_l(n):
        return n if n < 2 else fib_l(n - 1) + fib_l(n - 2)

    assert fib_h(20) == fib_l(20) == 6765
    assert fib_h.__wrapped__.cagri == fib_l.__wrapped__.cagri == 21


def test_hafiza_ayni_argumanla_tekrar_hesaplamaz():
    @hafiza()
    @say
    def kare(n):
        return n * n

    assert kare(5) == 25
    assert kare(5) == 25
    assert kare.__wrapped__.cagri == 1


def test_hafiza_maxsize_en_eskiyi_siler():
    @hafiza(maxsize=2)
    @say
    def kare(n):
        return n * n

    kare(1)
    kare(2)
    kare(3)
    assert len(kare.onbellek) == 2
    assert kare.__wrapped__.cagri == 3
    kare(3)
    assert kare.__wrapped__.cagri == 3
    kare(1)
    assert kare.__wrapped__.cagri == 4


def test_hafiza_maxsize_none_sinirsiz():
    @hafiza()
    def kare(n):
        return n * n

    for n in range(50):
        kare(n)
    assert len(kare.onbellek) == 50


def test_hafiza_adli_arguman():
    @hafiza()
    def kare(n):
        return n * n

    assert kare(3) == 9
    assert kare(n=3) == 9


def test_hafiza_ad_ve_belge_korunur():
    @hafiza(maxsize=3)
    def kare(n):
        """Karesini alır."""
        return n * n

    assert kare.__name__ == "kare"
    assert kare.__doc__ == "Karesini alır."