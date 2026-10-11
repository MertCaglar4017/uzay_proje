from uzay_oyunu.araclar import yakit_ekle


def test_yakit_ekle_her_cagri_bagimsiz():
    ilk = yakit_ekle(10)
    ikinci = yakit_ekle(20)
    assert ilk == [10]
    assert ikinci == [20]


def test_yakit_ekle_verilen_liste():
    assert yakit_ekle(5, [1]) == [1, 5]