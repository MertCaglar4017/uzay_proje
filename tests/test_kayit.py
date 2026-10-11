from uzay_oyunu.kayit import gorev_kaydi


def test_gorev_kaydi_tam():
    sonuc = gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al",
        oncelik="yüksek",
        sorumlu="Mert",
    )
    beklenen = (
        "[YÜKSEK] Kara deliğe atla\n"
        " 1. Kredi kazan\n"
        " 2. Pilot bul\n"
        " 3. Hiperdrive al\n"
        " sorumlu: Mert"
    )
    assert sonuc == beklenen


def test_gorev_kaydi_varsayilan_oncelik():
    assert gorev_kaydi("Dinlen") == "[NORMAL] Dinlen"


def test_gorev_kaydi_acilmis_argumanlar():
    adimlar = ["Kredi kazan", "Pilot bul"]
    ekler = {"sorumlu": "Mert"}
    sonuc = gorev_kaydi("Yola çık", *adimlar, **ekler)
    assert sonuc == "[NORMAL] Yola çık\n 1. Kredi kazan\n 2. Pilot bul\n sorumlu: Mert"