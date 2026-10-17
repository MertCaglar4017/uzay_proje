from itertools import islice, takewhile

import pytest

from uzay_oyunu.akis import fibonacci, yakit_gostergesi


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