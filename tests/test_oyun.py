from uzay_oyunu.oyun import travel


def test_kara_delige_ulasilir(monkeypatch):
    cevaplar = iter(["2", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(cevaplar))
    assert travel() == "kara_delik"


def test_hamle_sayisi_yazilir(monkeypatch, capsys):
    cevaplar = iter(["2", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(cevaplar))
    travel()
    assert "Oyunu 2 hamlede bitirdin!" in capsys.readouterr().out


def test_yakit_bitince_oyun_kaybedilir(monkeypatch, capsys):
    cevaplar = iter(["1"] * 25)
    monkeypatch.setattr("builtins.input", lambda _: next(cevaplar))
    sonuc = travel()
    assert sonuc != "kara_delik"
    assert "Yakıtın bitti, uzayda sürükleniyorsun…" in capsys.readouterr().out