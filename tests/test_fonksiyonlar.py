from uzay_oyunu.oyun import envanter_metni, hedef_menusu


def test_envanter_kredi_ve_pilot():
    sonuc = envanter_metni(True, False, True)
    assert sonuc == "Sende: bol kredi, yetenekli bir pilot"


def test_envanter_bos():
    assert envanter_metni(False, False, False) == ""


def test_hedef_menusu():
    beklenen = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(["centauri", "sirius"]) == beklenen